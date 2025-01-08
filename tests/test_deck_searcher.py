"""Tests focused on the updating of target decks with new notes"""
import os
import tempfile

import pytest

import anki.collection
import anki.notes
from anki_jpn.enums import VerbClass, AdjectiveClass
from anki_jpn.decks import DeckSearcher
from anki_jpn.config import ConfigManager
from anki_jpn.models import add_or_update_verb_model, add_or_update_adjective_model

SOURCE_DECK = 'source'
VERB_MODEL_NAME = 'verb model'
ADJ_MODEL_NAME = 'adj model'
SIMPLE_MODEL_NAME = 'simple model'
REALLY_SIMPLE_MODEL_NAME = "super simple model"

@pytest.fixture(name="anki_col")
def fixture_anki_col():
    """Fixture for providing a basically empty collection that has source
    and target decks as well as the verb conjugation model"""
    fd, fn = tempfile.mkstemp(suffix=".anki2")
    os.close(fd)
    col = anki.collection.Collection(fn)
    col.decks.add_normal_deck_with_name(SOURCE_DECK)

    basic_model = col.models.new(SIMPLE_MODEL_NAME)
    for field_name in ["note name", "exp", "rdng", "pitch", "translation"]:
        field_dict = col.models.new_field(field_name)
        col.models.add_field(basic_model, field_dict)
    col.models.add_template(basic_model, {
        "name": "Simple",
        "qfmt": "{{exp}}",
        "afmt": "{{rdng}}<br>{{pitch}}<br>{{translation}}"
    })
    col.models.add(basic_model)
    really_basic_model = col.models.new(REALLY_SIMPLE_MODEL_NAME)
    for field_name in ["exp", "rdng", "translation"]:
        field_dict = col.models.new_field(field_name)
        col.models.add_field(really_basic_model, field_dict)
    col.models.add_template(really_basic_model, {
        "name": "Simple",
        "qfmt": "{{exp}}",
        "afmt": "{{rdng}}<br>{{translation}}"
    })
    col.models.add(really_basic_model)

    add_or_update_verb_model(col.models, VERB_MODEL_NAME)
    add_or_update_adjective_model(col.models, ADJ_MODEL_NAME)

    note = anki.notes.Note(col, col.models.by_name(SIMPLE_MODEL_NAME))
    note.fields = ["First Note", '食べる', '食[た]べる', "LHL", 'to eat']
    note.add_tag('ichidan-verb')
    col.add_note(note, col.decks.id(SOURCE_DECK))

    note = anki.notes.Note(col, col.models.by_name(SIMPLE_MODEL_NAME))
    note.fields = ["First Note", '借りる', '借[か]りる', "LHH", 'to borrow']
    note.add_tag('ichidan')
    col.add_note(note, col.decks.id(SOURCE_DECK))

    note = anki.notes.Note(col, col.models.by_name(VERB_MODEL_NAME))
    note.fields[:3] = ['帰る', 'to return', '帰[かえ]る']
    note.add_tag('godan')
    col.add_note(note, col.decks.id(SOURCE_DECK))

    note = anki.notes.Note(col, col.models.by_name(SIMPLE_MODEL_NAME))
    note.fields = ["First Note", '来る', '来[く]る', "LH", 'to come']
    note.add_tag('irregular-verb')
    col.add_note(note, col.decks.id(SOURCE_DECK))

    note = anki.notes.Note(col, col.models.by_name(SIMPLE_MODEL_NAME))
    note.fields = ["First Note", '行く', '行[い]く', "HL", 'to go']
    note.add_tag('verb')
    col.add_note(note, col.decks.id(SOURCE_DECK))

    note = anki.notes.Note(col, col.models.by_name(SIMPLE_MODEL_NAME))
    note.fields = ["First Note", '良い', '良[yo]い', "LH", 'good']
    note.add_tag('adj')
    col.add_note(note, col.decks.id(SOURCE_DECK))
    
    note = anki.notes.Note(col, col.models.by_name(SIMPLE_MODEL_NAME))
    note.fields = ["First Note", '有名な', '有名[ゆうめい]な', "LHL", 'famous']
    note.add_tag('na-adjective')
    col.add_note(note, col.decks.id(SOURCE_DECK))
    
    note = anki.notes.Note(col, col.models.by_name(REALLY_SIMPLE_MODEL_NAME))
    note.fields = ['難しい', '難[むずか]しい', 'difficult']
    note.add_tag('i-adjective')
    col.add_note(note, col.decks.id(SOURCE_DECK))
    
    note = anki.notes.Note(col, col.models.by_name(ADJ_MODEL_NAME))
    note.fields[:3] = ['小さい', 'small', '小[ちい]さい']
    note.add_tag('i-adjective')
    col.add_note(note, col.decks.id(SOURCE_DECK))

    yield col
    col.close()
    os.unlink(fn)


@pytest.fixture(name="config_manager")
def fixture_config_manager():
    """Fixture for getting a ConfigManager object"""
    cfg = {
        "tags": {
            SOURCE_DECK: {
                VerbClass.ICHIDAN.value: ['ichidan', 'ichidan-verb'],
                VerbClass.GODAN.value: ['godan', 'godan-verb'],
                VerbClass.IRREGULAR.value: ['irregular-verb'],
                VerbClass.GENERAL.value: ['verb'],
                AdjectiveClass.I.value: ['i-adjective'],
                AdjectiveClass.NA.value: ['na-adjective'],
                AdjectiveClass.GENERAL.value: ['adjective', 'adj']
            }
        },
        "note_types": {
            SIMPLE_MODEL_NAME: {
                "expression": "exp",
                "meaning": "translation",
                "reading": "rdng"
            },
            REALLY_SIMPLE_MODEL_NAME: {
                "expression": "exp",
                "meaning": "translation",
                "reading": "rdng"
            }
        }
    }
    return ConfigManager(cfg)

@pytest.fixture(name="deck_searcher")
def fixture_deck_updater(config_manager, anki_col):
    """Fixture for getting the DeckSearcher to be tested"""
    searcher = DeckSearcher(anki_col, anki_col.decks.id(SOURCE_DECK), config_manager)
    return searcher

def get_note_expression(col, id_list, config_mgr):
    """Helper function to convert note IDs to the expressions for each note"""
    expressions = []
    for note_id in id_list:
        note = col.get_note(note_id)
        model = col.models.get(note.mid)
        model_fields = col.models.field_map(model)
        relevant_fields = config_mgr.get_model_fields(model['name'])

        expressions.append(note.fields[model_fields[relevant_fields[0]][0]])

    return expressions

def test_search_for_verbs(anki_col, config_manager, deck_searcher):
    """Test our ability to search for verbs"""
    verbs, models = deck_searcher.find_verbs(VERB_MODEL_NAME)

    assert models == [SIMPLE_MODEL_NAME]

    ichidan_verbs = get_note_expression(anki_col, verbs[VerbClass.ICHIDAN], config_manager)
    assert ichidan_verbs == ['食べる', '借りる']
    assert VerbClass.GODAN not in verbs
    irregular_verbs = get_note_expression(anki_col, verbs[VerbClass.IRREGULAR], config_manager)
    assert irregular_verbs == ['来る']
    general_verbs = get_note_expression(anki_col, verbs[VerbClass.GENERAL], config_manager)
    assert general_verbs == ['行く']

def test_search_for_adjectives(anki_col, config_manager, deck_searcher):
    """Test our ability to search for adjectives"""
    adjs, models = deck_searcher.find_adjectives(ADJ_MODEL_NAME)

    models.sort()
    assert models == [SIMPLE_MODEL_NAME, REALLY_SIMPLE_MODEL_NAME]

    i_adjectives = get_note_expression(anki_col, adjs[AdjectiveClass.I], config_manager)
    assert i_adjectives == ['難しい']
    na_adjectives = get_note_expression(anki_col, adjs[AdjectiveClass.NA], config_manager)
    assert na_adjectives == ['有名な']
    general_adjectives = get_note_expression(
        anki_col, adjs[AdjectiveClass.GENERAL], config_manager)
    assert general_adjectives == ['良い']
