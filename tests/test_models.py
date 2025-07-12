"""Tests pertaining to the creation and updating of model definitions"""
import os
import tempfile
from copy import deepcopy

import pytest
import cssutils

from anki.buildinfo import version as anki_version
import anki.collection
from japanese_conjugation.enums import Formality, Form
from japanese_conjugation.models import (
    VERB_COMBOS, ADJECTIVE_COMBOS, COMBO_HASHES, add_or_update_verb_model,
    add_or_update_adjective_model, _create_model
)

anki_version_info = tuple(int(x) for x in anki_version.split('.'))

@pytest.fixture(name="anki_col")
def fixture_anki_col():
    """Fixture for providing an empty collection"""
    fd, fn = tempfile.mkstemp(suffix=".anki2")
    os.close(fd)
    col = anki.collection.Collection(fn)
    yield col
    col.close()
    os.unlink(fn)


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

@pytest.mark.skipif(anki_version_info <= (23, 10), reason="'id' attribute of templates not present")
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
    mocker.patch("japanese_conjugation.models.COMBO_HASHES", mock_hashes)
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

custom_colors_data = [
    (None, ('#4DB01C', '#4DB01C', '#2A6DEC', '#2A6DEC')),
    ({}, ('#4DB01C', '#4DB01C', '#2A6DEC', '#2A6DEC')),
    ({"day": {"polite": '#30B10F'}}, ('#30B10F', '#4DB01C', '#2A6DEC', '#2A6DEC')),
    ({"day": {"plain": '#30B10F'}}, ('#4DB01C', '#4DB01C', '#30B10F', '#2A6DEC')),
    ({"night": {"polite": '#30B10F'}}, ('#4DB01C', '#30B10F', '#2A6DEC', '#2A6DEC')),
    ({"night": {"plain": '#30B10F'}}, ('#4DB01C', '#4DB01C', '#2A6DEC', '#30B10F')),
    ({"day": {"polite": '#010394', "plain": '#ab0193'},
      "night": {"polite": '#f02dc1', "plain": "#32df01"}},
      ('#010394', '#f02dc1', '#ab0193', "#32df01"))
]
@pytest.mark.parametrize("color_dict, ref_colors", custom_colors_data)
def test_custom_colors(anki_col, color_dict, ref_colors):
    """Test that the configuration can be used to customize colors for the cards"""
    model_name = "verb model"
    add_or_update_adjective_model(anki_col.models, model_name, color_dict)
    model = anki_col.models.by_name(model_name)

    css = cssutils.parseString(model['css'])
    day_plain_rules = [r for r in css.cssRules if r.selectorText == '.plain']
    night_plain_rules = [r for r in css.cssRules if r.selectorText == '.nightMode .plain']
    day_polite_rules = [r for r in css.cssRules if r.selectorText == '.polite']
    night_polite_rules = [r for r in css.cssRules if r.selectorText == '.nightMode .polite']
    assert day_polite_rules[-1].style.color == ref_colors[0]
    assert night_polite_rules[-1].style.color == ref_colors[1]
    assert day_plain_rules[-1].style.color == ref_colors[2]
    assert night_plain_rules[-1].style.color == ref_colors[3]

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
    'n6Nx': (Formality.PLAIN, Form.VOLITIONAL),
    '9Rq6': (Formality.POLITE, Form.TAI_NON_PAST),
    'MZD6': (Formality.POLITE, Form.TAI_NON_PAST_NEG),
    'F3Ve': (Formality.POLITE, Form.TAI_PAST),
    'mwjc': (Formality.POLITE, Form.TAI_PAST_NEG),
    'kHaM': (None, Form.TAI_TE),
    '1lct': (Formality.PLAIN, Form.TAI_NON_PAST),
    'L0D7': (Formality.PLAIN, Form.TAI_NON_PAST_NEG),
    'uRpq': (Formality.PLAIN, Form.TAI_PAST),
    'EgRi': (Formality.PLAIN, Form.TAI_PAST_NEG),
    'asc6': (Formality.POLITE, Form.POTENTIAL_NON_PAST),
    'TqmV': (Formality.POLITE, Form.POTENTIAL_NON_PAST_NEG),
    'r5s9': (Formality.POLITE, Form.POTENTIAL_PAST),
    '1Ut6': (Formality.POLITE, Form.POTENTIAL_PAST_NEG),
    'mUs0': (None, Form.POTENTIAL_TE),
    'fJQR': (Formality.PLAIN, Form.POTENTIAL_NON_PAST),
    '0uSU': (Formality.PLAIN, Form.POTENTIAL_NON_PAST_NEG),
    'h8MI': (Formality.PLAIN, Form.POTENTIAL_PAST),
    'xisC': (Formality.PLAIN, Form.POTENTIAL_PAST_NEG),
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
