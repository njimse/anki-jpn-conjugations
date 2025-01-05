import os
import sys
import itertools
# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect, getText, chooseList
# import all of the Qt GUI library
from aqt.qt import *

from anki.decks import DeckManager
from anki.tags import TagManager

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from anki_jpn.models import (
    VERB_MODEL_NAME, ADJECTIVE_MODEL_NAME,
    add_or_update_verb_model
)
from anki_jpn.enums import VerbClass, AdjectiveClass
from anki_jpn.verbs import generate_verb_forms
from anki_jpn.adjectives import generate_adjective_forms
from anki_jpn.decks import DeckUpdater

def create_deck():
    deck_name = getText("What would you like to name the new deck?")
    if deck_name[0]:
        dm = DeckManager(mw.col)
        return dm.add_normal_deck_with_name(deck_name[0]).id, deck_name[0]

def select_deck(msg):
    dm = DeckManager(mw.col)
    all_decks = [d.name for d in dm.all_names_and_ids(skip_empty_default=True)]
    deck_choice = chooseList(msg, all_decks)
    deck_name = all_decks[deck_choice]
    deck_id = dm.id_for_name(deck_name)
    return deck_id, deck_name

def select_tag(msg):
    tm = TagManager(mw.col)
    all_tags = [t for t in tm.all()]
    tag_choice = chooseList(msg, all_tags)
    tag_name = all_tags[tag_choice]
    return tag_name

def get_field_mapping(model_info):
    for model_details in model_info.values():
        example_list = [f'{field_name}: {field_example}' for field_name, field_example in zip(model_details['fields'], model_details['example'].fields)]
        expression_index = chooseList(f"For the '{model_details['name']}' note type, Which field contains the expression?", example_list)
        meaning_index = chooseList(f"For the '{model_details['name']}' note type, Which field contains the meaning?", example_list)
        reading_index = chooseList(f"For the '{model_details['name']}' note type, Which field contains the reading?", example_list)
        model_details["expression_index"] = expression_index
        model_details["meaning_index"] = meaning_index
        model_details["reading_index"] = reading_index

def _adjective_update(target_deck_id, target_deck_name):
    source_deck_id, source_deck_name = select_deck("Which deck should be used as the source content?")
    i_tag = select_tag("Which tag is used for i-adjectivess?")
    na_tag = select_tag("Which tag is used for na-adjectives?")
    i_notes = mw.col.find_notes(f'tag:{i_tag} "deck:{source_deck_name}"')
    na_notes = mw.col.find_notes(f'tag:{na_tag} "deck:{source_deck_name}"')
    model_infos = {}
    for note_id in itertools.chain(i_notes, na_notes):
        note = mw.col.get_note(note_id)
        if note.mid not in model_infos:
            model = mw.col.models.get(note.mid)
            model_infos[note.mid] = {
                'fields': [f['name'] for f in model['flds']],
                'name': model['name'],
                'example': note
            }
    get_field_mapping(model_infos)
    add_or_update_verb_model(mw.col.models, ADJECTIVE_MODEL_NAME)
    dest_model = mw.col.models.by_name(ADJECTIVE_MODEL_NAME)
    deck_updater = DeckUpdater(mw.col, target_deck_id, dest_model)
    for verb_type, note_id_list in [(AdjectiveClass.I, i_notes), (AdjectiveClass.NA, na_notes)]:
        for note_id in note_id_list:
            note = mw.col.get_note(note_id)
            m_info = model_infos[note.mid]
            note_reading = note.fields[m_info['reading_index']].split('<')[0].strip()
            conjugations = generate_verb_forms(note_reading, verb_type)
            deck_updater.add_note_to_deck(note, m_info, conjugations)


def _verb_update(target_deck_id, target_deck_name):
    source_deck_id, source_deck_name = select_deck("Which deck should be used as the source content?")
    ichidan_tag = select_tag("Which tag is used for ichidan verbs?")
    godan_tag = select_tag("Which tag is used for godan verbs?")
    irregular_tag = select_tag("Which tag is used for irregular verbs?")
    ichidan_notes = mw.col.find_notes(f'tag:{ichidan_tag} "deck:{source_deck_name}"')
    godan_notes = mw.col.find_notes(f'tag:{godan_tag} "deck:{source_deck_name}"')
    irregular_notes = mw.col.find_notes(f'tag:{irregular_tag} "deck:{source_deck_name}"')
    model_infos = {}
    for note_id in itertools.chain(ichidan_notes, godan_notes, irregular_notes):
        note = mw.col.get_note(note_id)
        if note.mid not in model_infos:
            model = mw.col.models.get(note.mid)
            model_infos[note.mid] = {
                'fields': [f['name'] for f in model['flds']],
                'name': model['name'],
                'example': note
            }
    get_field_mapping(model_infos)
    add_or_update_verb_model(mw.col.models, VERB_MODEL_NAME)
    dest_model = mw.col.models.by_name(VERB_MODEL_NAME)
    deck_updater = DeckUpdater(mw.col, target_deck_id, dest_model)
    for verb_type, note_id_list in [(VerbClass.ICHIDAN, ichidan_notes), (VerbClass.GODAN, godan_notes), (VerbClass.IRREGULAR, irregular_notes)]:
        for note_id in note_id_list:
            note = mw.col.get_note(note_id)
            m_info = model_infos[note.mid]
            note_reading = note.fields[m_info['reading_index']].split('<')[0].strip()
            conjugations = generate_verb_forms(note_reading, verb_type)
            deck_updater.add_note_to_deck(note, m_info, conjugations)


def create_verb_deck():
    deck_id, deck_name = create_deck()
    _verb_update(deck_id, deck_name)

def create_adjective_deck():
    deck_id, deck_name = create_deck()
    _adjective_update(deck_id, deck_name)
    
def update_verb_deck():
    deck_id, deck_name = select_deck("Which deck would you like to update?")
    _verb_update(deck_id, deck_name)

def update_adjective_deck():
    deck_id, deck_name = select_deck("Which deck would you like to update?")
    _adjective_update(deck_id, deck_name)

# Create the menu items
conj_menu = QMenu("Conjugation Decks", mw)
create_verb_deck_action = conj_menu.addAction("Create Verb Conjugation Deck")
create_adjective_deck_action = conj_menu.addAction("Create Adjective Conjugation Deck")
update_verb_deck_action = conj_menu.addAction("Update Verb Conjugation Deck")
update_adjective_deck_action = conj_menu.addAction("Update Adjective Conjugation Deck")

# Add the triggers
create_verb_deck_action.triggered.connect(create_verb_deck)
create_adjective_deck_action.triggered.connect(create_adjective_deck)
update_verb_deck_action.triggered.connect(update_verb_deck)
update_adjective_deck_action.triggered.connect(update_adjective_deck)

# Add the menu button to the "Tools" menu
mw.form.menuTools.addMenu(conj_menu)
