import os
import tempfile

import pytest

import anki.collection
from anki_jpn.verbs import generate_verb_forms, VerbClass
from anki_jpn.enums import VERB_COMBOS
from anki_jpn.decks import DeckUpdater
from anki_jpn.models import add_verb_conjugation_model, add_adjective_conjugation_model, ADJECTIVE_MODEL_NAME, VERB_MODEL_NAME

TARGET_DECK = 'target'
SOURCE_DECK = 'source'

@pytest.fixture
def anki_col():
    fd, fn = tempfile.mkstemp()
    os.close(fd)
    col = anki.collection.Collection(fn)
    col.decks.add_normal_deck_with_name(SOURCE_DECK)
    col.decks.add_normal_deck_with_name(TARGET_DECK)
    verb_model = add_verb_conjugation_model(col)
    col.models.add(verb_model)
    yield col
    col.close()
    os.unlink(fn)

@pytest.fixture
def target_deck_id(anki_col):
    target_deck_id = anki_col.decks.id(TARGET_DECK)
    return target_deck_id

@pytest.fixture
def verb_model(anki_col):
    return anki_col.models.by_name(VERB_MODEL_NAME)

@pytest.fixture
def deck_updater(anki_col, target_deck_id, verb_model):
    updater = DeckUpdater(anki_col, target_deck_id, verb_model, VERB_COMBOS, {'expression': 4, 'meaning': 1, 'reading': 2})
    return updater

class MockNote:
    def __init__(self, expression, meaning, reading):
        self.fields = ['', meaning, reading, '', expression]

def compose_ref_field_values(base_fields, conjugations):
    new_list = base_fields + [''] * len(VERB_COMBOS)
    for conj, form, formality in conjugations:
        field_index = VERB_COMBOS.index((formality, form)) + 3
        new_list[field_index] = conj
    return new_list

def test_add_new_note_to_deck(anki_col, deck_updater):
    base_note = MockNote('食べる', 'to eat', '食[た]べる')
    conjugations = generate_verb_forms(base_note.fields[2], VerbClass.ICHIDAN)
    deck_updater.add_note_to_deck(base_note, conjugations)

    result_note_ids = anki_col.find_notes(f'"Expression:食べる" "Meaning:to eat" "Reading:食[た]べる" "deck:{TARGET_DECK}"')
    assert len(result_note_ids) == 1
    note = anki_col.get_note(result_note_ids[0])
    ref_fields = compose_ref_field_values(['食べる', 'to eat', '食[た]べる'], conjugations)
    for index, ref_value in enumerate(ref_fields):
        assert note.fields[index] == ref_value
