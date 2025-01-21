"""Tests pertaining to the creation and updating of model definitions"""
import os
import tempfile
from copy import deepcopy

import pytest

import anki.collection
from anki_jpn.enums import Formality, Form
from anki_jpn.models import (
    VERB_COMBOS, ADJECTIVE_COMBOS, COMBO_HASHES, add_or_update_verb_model,
    add_or_update_adjective_model, _create_model
)

@pytest.fixture(name="anki_col")
def fixture_anki_col():
    """Fixture for providing an empty collection"""
    fd, fn = tempfile.mkstemp(suffix=".anki2")
    os.close(fd)
    col = anki.collection.Collection(fn)
    yield col
    col.close()
    os.unlink(fn)


# @pytest.fixture(name="deck_updater")
# def fixture_deck_updater(anki_col):
#     """Fixture for getting the DeckUpdater to be tested"""
#     TARGET_DECK = 'target'
#     SOURCE_DECK = 'source'
#     VERB_MODEL_NAME = 'verb model'
#     SOURCE_MODEL_NAME = 'simple model'

#     anki_col.decks.add_normal_deck_with_name(SOURCE_DECK)
#     anki_col.decks.add_normal_deck_with_name(TARGET_DECK)

#     basic_model = anki_col.models.new(SOURCE_MODEL_NAME)
#     for field_name in ["note name", "exp", "rdng", "pitch", "translation"]:
#         field_dict = anki_col.models.new_field(field_name)
#         anki_col.models.add_field(basic_model, field_dict)
#     anki_col.models.add_template(basic_model, {
#         "name": "Simple Card Template",
#         "qfmt": "{{exp}}",
#         "afmt": "{{rdng}}<br>{{pitch}}<br>{{translation}}"
#     })
#     anki_col.models.add(basic_model)
#     add_or_update_verb_model(anki_col.models, VERB_MODEL_NAME)

#     updater = DeckUpdater(anki_col, target_deck_id, verb_model, config_manager)
#     return updater

def compare_models(a, b):
    """Compare two models to ensure that they are (sufficiently) equivalent"""
    assert a is not None
    assert b is not None
    assert a['css'] == b['css']
    assert a['name'] == b['name']
    assert len(a['flds']) == len(b['flds'])
    for a_field, b_field in zip(a['flds'], b['flds']):
        assert a_field['name'] == b_field['name']
    assert len(a['tmpls']) == len(b['tmpls'])
    for a_template, b_template in zip(a['tmpls'], b['tmpls']):
        assert a_template['name'] == b_template['name']
        assert a_template['qfmt'] == b_template['qfmt']
        assert a_template['afmt'] == b_template['afmt']

def test_no_remaining_templates_verbs(anki_col):
    """Test that we resolve all of the placeholders in the card templates of verbs"""
    model_name = "verb model"
    add_or_update_verb_model(anki_col.models, model_name)

    model = anki_col.models.by_name(model_name)
    for template in model['tmpls']:
        assert not any(ph in template['qfmt'] for ph in ['FORMALITY', 'FORM_NAME', 'FIELD_NAME'])
        assert not any(ph in template['afmt'] for ph in ['FORMALITY', 'FORM_NAME', 'FIELD_NAME'])

def test_no_remaining_templates_adjectives(anki_col):
    """Test that we resolve all of the placeholders in the card templates of adjectives"""
    model_name = "adjective model"
    add_or_update_adjective_model(anki_col.models, model_name)

    model = anki_col.models.by_name(model_name)
    for template in model['tmpls']:
        assert not any(ph in template['qfmt'] for ph in ['FORMALITY', 'FORM_NAME', 'FIELD_NAME'])
        assert not any(ph in template['afmt'] for ph in ['FORMALITY', 'FORM_NAME', 'FIELD_NAME'])

def test_add_new_model(anki_col):
    """Test the logic for when the model does not yet exist in the collection"""
    model_name = "verb model"
    ref_model = anki_col.models.new(model_name)
    _create_model(anki_col.models, ref_model, VERB_COMBOS)

    start_models = anki_col.models.all_names_and_ids()
    add_or_update_verb_model(anki_col.models, model_name)
    end_models = anki_col.models.all_names_and_ids()

    hyp_model = anki_col.models.by_name(model_name)
    compare_models(ref_model, hyp_model)
    assert len(end_models) - len(start_models) == 1

def test_no_change_needed(anki_col):
    """Test the logic for when the existing model does not need any updating"""
    model_name = "verb model"
    ref_model = anki_col.models.new(model_name)
    _create_model(anki_col.models, ref_model, VERB_COMBOS)

    add_or_update_verb_model(anki_col.models, model_name)
    new_model_id = anki_col.models.by_name(model_name)['id']

    start_models = anki_col.models.all_names_and_ids()
    add_or_update_verb_model(anki_col.models, model_name)
    end_models = anki_col.models.all_names_and_ids()

    # assert that we didn't change the model ID
    assert new_model_id == anki_col.models.by_name(model_name)['id']

    hyp_model = anki_col.models.by_name(model_name)
    compare_models(ref_model, hyp_model)

    assert len(end_models) == len(start_models)

def test_rename_fields(anki_col):
    """Test that we correctly identify changes to field names"""
    ref_model = anki_col.models.new("verb model")
    _create_model(anki_col.models, ref_model, VERB_COMBOS)

    # Create a limited version of our regular verb model
    start_model = anki_col.models.new("verb model")
    limited_combos = [c for i, c in enumerate(VERB_COMBOS) if i % 3 == 0]
    _create_model(anki_col.models, start_model, limited_combos)
    anki_col.models.add(start_model)
    start_model = anki_col.models.by_name("verb model")
    hash_to_template = {}
    hash_to_field = {}
    for card_template in start_model['tmpls']:
        hr_name, field_hash = card_template['name'].rsplit(' ', 1)
        card_template['name'] = hr_name.lower() + " " + field_hash
        hash_to_template[field_hash] = card_template['id']
    for field_dict in start_model['flds']:
        if '<' in field_dict['name']:
            hr_name, field_hash = field_dict['name'].rsplit(' ', 1)
            field_dict['name'] = hr_name.lower() + " " + field_hash
            hash_to_field[field_hash] = field_dict['id']
    anki_col.models.update_dict(start_model)

    start_models = anki_col.models.all_names_and_ids()
    add_or_update_verb_model(anki_col.models, "verb model")
    end_models = anki_col.models.all_names_and_ids()

    hyp_model = anki_col.models.by_name("verb model")
    compare_models(ref_model, hyp_model)

    for field_hash, ref_id in hash_to_template.items():
        matches = 0
        for card_template in hyp_model['tmpls']:
            hr_name, field_hash = card_template['name'].rsplit(' ', 1)
            if ref_id == card_template['id']:
                matches += 1
        assert matches == 1

    for field_hash, ref_id in hash_to_field.items():
        matches = 0
        for field_dict in hyp_model['flds']:
            if '<' in field_dict['name']:
                hr_name, field_hash = field_dict['name'].rsplit(' ', 1)
                if ref_id == field_dict['id']:
                    matches += 1
        assert matches == 1

    assert len(end_models) == len(start_models)

def test_new_combos(anki_col):
    """Test the logic for when the model has new combos"""
    model_name = "verb model"
    ref_model = anki_col.models.new(model_name)
    _create_model(anki_col.models, ref_model, VERB_COMBOS)

    # Create a limited version of our regular verb model
    start_model = anki_col.models.new(model_name)
    limited_combos = [c for i, c in enumerate(VERB_COMBOS) if i % 3 == 0]
    _create_model(anki_col.models, start_model, limited_combos)
    anki_col.models.add(start_model)

    start_models = anki_col.models.all_names_and_ids()
    add_or_update_verb_model(anki_col.models, model_name)
    end_models = anki_col.models.all_names_and_ids()

    hyp_model = anki_col.models.by_name(model_name)
    compare_models(ref_model, hyp_model)

    assert len(end_models) == len(start_models)

def test_removed_combos(mocker, anki_col):
    """Test the logic for when the model has fewer fields"""
    extra_combos = VERB_COMBOS + [(Formality.POLITE, Form.TE)]
    mock_hashes = deepcopy(COMBO_HASHES)
    mock_hashes[(Formality.POLITE, Form.TE)] = "0000"
    mocker.patch("anki_jpn.models.COMBO_HASHES", mock_hashes)
    model_name = "verb model"
    start_model = anki_col.models.new(model_name)
    _create_model(anki_col.models, start_model, extra_combos)
    anki_col.models.add(start_model)

    # Create a limited version of our regular verb model
    ref_model = anki_col.models.new(model_name)
    _create_model(anki_col.models, ref_model, VERB_COMBOS)

    start_models = anki_col.models.all_names_and_ids()
    add_or_update_verb_model(anki_col.models, model_name)
    end_models = anki_col.models.all_names_and_ids()

    hyp_model = anki_col.models.by_name(model_name)
    compare_models(ref_model, hyp_model)

    assert len(end_models) == len(start_models)

def test_changed_style(anki_col):
    """Test the logic for when the style settings have changed"""
    model_name = "verb model"
    ref_model = anki_col.models.new(model_name)
    _create_model(anki_col.models, ref_model, VERB_COMBOS)

    start_model = anki_col.models.new(model_name)
    _create_model(anki_col.models, start_model, VERB_COMBOS)
    start_model['css'] = 'Dummy CSS'
    anki_col.models.add(start_model)

    start_models = anki_col.models.all_names_and_ids()
    add_or_update_verb_model(anki_col.models, model_name)
    end_models = anki_col.models.all_names_and_ids()

    hyp_model = anki_col.models.by_name(model_name)
    compare_models(ref_model, hyp_model)

    assert len(end_models) == len(start_models)

def test_changed_base_templates(anki_col):
    """Test the logic for when the base template changes, triggering a replacement
    of all of the templates"""
    model_name = "verb model"
    ref_model = anki_col.models.new(model_name)
    _create_model(anki_col.models, ref_model, VERB_COMBOS)

    start_model = anki_col.models.new(model_name)
    _create_model(anki_col.models, start_model, VERB_COMBOS)
    for index, template in enumerate(start_model['tmpls']):
        template['qfmt'] = f"Dummy front of card {index}: " + "{{Expression}}"
    anki_col.models.add(start_model)

    start_models = anki_col.models.all_names_and_ids()
    add_or_update_verb_model(anki_col.models, model_name)
    end_models = anki_col.models.all_names_and_ids()


    hyp_model = anki_col.models.by_name(model_name)
    compare_models(ref_model, hyp_model)

    assert len(end_models) == len(start_models)

reference_combo_hashes = {
    'uNCk': (Formality.POLITE, Form.NON_PAST),
    'pyJD': (Formality.POLITE, Form.NON_PAST_NEG),
    'FWhU': (Formality.POLITE, Form.PAST),
    'OfA3': (Formality.POLITE, Form.PAST_NEG),
    'TiKs': (Formality.POLITE, Form.VOLITIONAL),
    'g1G0': (None, Form.TE),
    'AUXG': (Formality.PLAIN, Form.NON_PAST),
    '5hRQ': (Formality.PLAIN, Form.NON_PAST_NEG),
    'wlxY': (Formality.PLAIN, Form.PAST),
    'X9LC': (Formality.PLAIN, Form.PAST_NEG),
    '9Rq6': (Formality.POLITE, Form.TAI_NON_PAST),
    'MZD6': (Formality.POLITE, Form.TAI_NON_PAST_NEG),
    'F3Ve': (Formality.POLITE, Form.TAI_PAST),
    'mwjc': (Formality.POLITE, Form.TAI_PAST_NEG),
    'kHaM': (None, Form.TAI_TE),
    '1lct': (Formality.PLAIN, Form.TAI_NON_PAST),
    'L0D7': (Formality.PLAIN, Form.TAI_NON_PAST_NEG),
    'uRpq': (Formality.PLAIN, Form.TAI_PAST),
    'EgRi': (Formality.PLAIN, Form.TAI_PAST_NEG)
}
def test_field_hashes():
    """Test that we have the expected hash per combo in the model fields"""
    for combo, hash_str in COMBO_HASHES.items():
        assert reference_combo_hashes[hash_str] == combo

def test_combos_have_hashes():
    """Test that we have hashes for all combos"""
    for combo in ADJECTIVE_COMBOS:
        assert combo in COMBO_HASHES
    for combo in VERB_COMBOS:
        assert combo in COMBO_HASHES
