"""Tests focused on the updating of target decks with new notes"""
import os
import copy
import tempfile

import pytest

import anki.collection
from anki_jpn.verbs import generate_verb_forms, VerbClass
from anki_jpn.decks import DeckUpdater
from anki_jpn.models import combo_to_field_name, add_or_update_verb_model

TARGET_DECK = 'target'
SOURCE_DECK = 'source'
VERB_MODEL_NAME = 'verb model'

@pytest.fixture(name="anki_col")
def fixture_anki_col():
    """Fixture for providing a basically empty collection that has source
    and target decks as well as the verb conjugation model"""
    fd, fn = tempfile.mkstemp(suffix=".anki2")
    os.close(fd)
    col = anki.collection.Collection(fn)
    col.decks.add_normal_deck_with_name(SOURCE_DECK)
    col.decks.add_normal_deck_with_name(TARGET_DECK)
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

@pytest.fixture(name="deck_updater")
def fixture_deck_updater(anki_col, target_deck_id, verb_model):
    """Fixture for getting the DeckUpdater to be tested"""
    updater = DeckUpdater(anki_col, target_deck_id, verb_model)
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
    base_note = MockNote('食べる', 'to eat', '食[た]べる')
    conjugations = generate_verb_forms(base_note.fields[2], VerbClass.ICHIDAN)
    query = f'"Expression:食べる" "Meaning:to eat" "Reading:食[た]べる" "deck:{TARGET_DECK}"'
    deck_updater.add_note_to_deck(
        base_note, {'expression_index': 4, 'meaning_index': 1, 'reading_index': 2}, conjugations)

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
    base_note = MockNote('食べる', 'to eat', '食[た]べる')
    full_conjugations = generate_verb_forms(base_note.fields[2], VerbClass.ICHIDAN)
    limited_conjugations = copy.deepcopy(full_conjugations[:-4])
    limited_conjugations[-1][0] = "foobar"
    query = f'"Expression:食べる" "Meaning:to eat" "Reading:食[た]べる" "deck:{TARGET_DECK}"'

    # First, add the note using a limited set of conjugations
    deck_updater.add_note_to_deck(
        base_note, {'expression_index': 4, 'meaning_index': 1, 'reading_index': 2},
        limited_conjugations)

    initial_result_note_ids = anki_col.find_notes(query)
    assert len(initial_result_note_ids) == 1
    note = anki_col.get_note(initial_result_note_ids[0])
    ref_fields = _compose_ref_field_values(anki_col.models.field_map(verb_model),
                                           '食べる', 'to eat', '食[た]べる', limited_conjugations)
    for index, ref_value in enumerate(ref_fields):
        assert note.fields[index] == ref_value

    # Now add the same word but with the full (and correct) set of conjugations
    deck_updater.add_note_to_deck(
        base_note, {'expression_index': 4, 'meaning_index': 1, 'reading_index': 2},
        full_conjugations)
    update_result_note_ids = anki_col.find_notes(query)
    # we should still only get a single result
    assert len(update_result_note_ids) == 1
    assert initial_result_note_ids == update_result_note_ids
    note = anki_col.get_note(update_result_note_ids[0])
    ref_fields = _compose_ref_field_values(anki_col.models.field_map(verb_model),
                                           '食べる', 'to eat', '食[た]べる', full_conjugations)
    for index, ref_value in enumerate(ref_fields):
        assert note.fields[index] == ref_value
