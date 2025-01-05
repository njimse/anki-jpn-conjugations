"""Tests pertaining to the creation and updating of model definitions"""
import os
import tempfile
import pytest

import anki.collection
from anki_jpn.enums import Formality, Form
from anki_jpn.models import VERB_COMBOS, add_or_update_verb_model, _create_model

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

def test_removed_combos(anki_col):
    """Test the logic for when the model has fewer fields"""
    extra_combos = VERB_COMBOS + [(Formality.POLITE, Form.TE)]
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
