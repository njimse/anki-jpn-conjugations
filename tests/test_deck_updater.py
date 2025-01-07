"""Tests focused on the updating of target decks with new notes"""
import os
import copy
import tempfile

import pytest

import anki.collection
import anki.notes
from anki_jpn.verbs import generate_verb_forms, VerbClass
from anki_jpn.decks import DeckUpdater
from anki_jpn.config import ConfigManager
from anki_jpn.models import combo_to_field_name, add_or_update_verb_model

TARGET_DECK = 'target'
SOURCE_DECK = 'source'
VERB_MODEL_NAME = 'verb model'
SOURCE_MODEL_NAME = 'simple model'

@pytest.fixture(name="anki_col")
def fixture_anki_col():
    """Fixture for providing a basically empty collection that has source
    and target decks as well as the verb conjugation model"""
    fd, fn = tempfile.mkstemp(suffix=".anki2")
    os.close(fd)
    col = anki.collection.Collection(fn)
    col.decks.add_normal_deck_with_name(SOURCE_DECK)
    col.decks.add_normal_deck_with_name(TARGET_DECK)

    basic_model = col.models.new(SOURCE_MODEL_NAME)
    for field_name in ["note name", "exp", "rdng", "pitch", "translation"]:
        field_dict = col.models.new_field(field_name)
        col.models.add_field(basic_model, field_dict)
    col.models.add_template(basic_model, {
        "name": "Simple",
        "qfmt": "{{exp}}",
        "afmt": "{{rdng}}<br>{{pitch}}<br>{{translation}}"
    })
    col.models.add(basic_model)
    add_or_update_verb_model(col.models, VERB_MODEL_NAME)
    yield col
    col.close()
    os.unlink(fn)

@pytest.fixture(name="target_deck_id")
def fixture_target_deck_id(anki_col):
    """Fixture for getting the deck id of the 'target' deck"""
    target_deck_id = anki_col.decks.id(TARGET_DECK)
    return target_deck_id

@pytest.fixture(name="verb_model")
def fixture_verb_model(anki_col):
    """Fixture for getting the verb conjugation model"""
    return anki_col.models.by_name(VERB_MODEL_NAME)

@pytest.fixture(name="config_manager")
def fixture_config_manager():
    cfg = {
        "note_types": {
            SOURCE_MODEL_NAME: {
                "expression": "exp",
                "meaning": "translation",
                "reading": "rdng"
            }
        }
    }
    return ConfigManager(cfg)

@pytest.fixture(name="deck_updater")
def fixture_deck_updater(config_manager, anki_col, target_deck_id, verb_model):
    """Fixture for getting the DeckUpdater to be tested"""
    updater = DeckUpdater(anki_col, target_deck_id, verb_model, config_manager)
    return updater

class MockNote: # pylint: disable=R0903
    """Mock class object to be used as a source note"""
    def __init__(self, expression, meaning, reading):
        self.fields = ['', meaning, reading, '', expression]
        self.tags = []

def _compose_ref_field_values(field_map, expression, meaning, reading, conjugations):
    """Translate the base fields and conjugations into a list of expected values"""
    ref_values = ['']*len(field_map)

    ref_values[field_map["Expression"][0]] = expression
    ref_values[field_map["Meaning"][0]] = meaning
    ref_values[field_map["Reading"][0]] = reading

    for conj, form, formality in conjugations:
        field_name = combo_to_field_name(form, formality)
        if field_name in field_map:
            field_index = field_map[field_name][0]
            ref_values[field_index] = conj

    return ref_values

def test_add_new_note_to_deck(anki_col, verb_model, deck_updater):
    """Test that we create a new note when the word is not present in the target deck"""
    base_note = anki.notes.Note(anki_col, anki_col.models.by_name(SOURCE_MODEL_NAME))
    base_note.fields = ["First Note", '食べる', '食[た]べる', "LHL", 'to eat']
    anki_col.add_note(base_note, anki_col.decks.id(SOURCE_DECK))
    conjugations = generate_verb_forms(base_note.fields[2], VerbClass.ICHIDAN)
    query = f'"Expression:食べる" "Meaning:to eat" "Reading:食[た]べる" "deck:{TARGET_DECK}"'

    deck_updater.add_note_to_deck(base_note, VerbClass.ICHIDAN)

    result_note_ids = anki_col.find_notes(query)
    assert len(result_note_ids) == 1
    note = anki_col.get_note(result_note_ids[0])
    ref_fields = _compose_ref_field_values(anki_col.models.field_map(verb_model),
                                           '食べる', 'to eat', '食[た]べる', conjugations)
    for index, ref_value in enumerate(ref_fields):
        assert note.fields[index] == ref_value

def test_update_note_in_deck(anki_col, verb_model, deck_updater):
    """Test that when an existing word is in the deck, we update the note rather than
    create a brand new note
    """
    base_note = anki.notes.Note(anki_col, anki_col.models.by_name(SOURCE_MODEL_NAME))
    base_note.fields = ["First Note", '食べる', '食[た]べる', "LHL", 'to eat']
    anki_col.add_note(base_note, anki_col.decks.id(SOURCE_DECK))

    starting_note = anki.notes.Note(anki_col, verb_model)
    starting_note.fields[0] = '食べる'
    starting_note.fields[1] = 'to eat'
    starting_note.fields[2] = '食[た]べる'
    starting_note.fields[-2] = 'foobar'
    starting_note.fields[-3] = 'foobuzz'
    anki_col.add_note(starting_note, anki_col.decks.id(TARGET_DECK))

    conjugations = generate_verb_forms(base_note.fields[2], VerbClass.ICHIDAN)
    query = f'"Expression:食べる" "Meaning:to eat" "Reading:食[た]べる" "deck:{TARGET_DECK}"'
    initial_result_note_ids = anki_col.find_notes(query)

    assert len(initial_result_note_ids) == 1
    note = anki_col.get_note(initial_result_note_ids[0])

    # Now add the same word but with the full (and correct) set of conjugations
    deck_updater.add_note_to_deck(base_note, VerbClass.ICHIDAN)
    update_result_note_ids = anki_col.find_notes(query)

    # we should still only get a single result
    assert len(update_result_note_ids) == 1
    assert initial_result_note_ids == update_result_note_ids
    note = anki_col.get_note(update_result_note_ids[0])
    ref_fields = _compose_ref_field_values(anki_col.models.field_map(verb_model),
                                           '食べる', 'to eat', '食[た]べる', conjugations)
    for index, ref_value in enumerate(ref_fields):
        assert note.fields[index] == ref_value
