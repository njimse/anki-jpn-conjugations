import os
# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect, getText, chooseList
# import all of the Qt GUI library
from aqt.qt import *

from anki.decks import DeckManager
from anki.models import ModelManager
from anki.tags import TagManager

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def create_deck():
    deck_name = getText("What would you like to name the new deck?")
    if deck_name[0]:
        dm = DeckManager(mw.col)
        return dm.add_normal_deck_with_name(deck_name[0]), deck_name[0]

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

def select_note_type(deck_id):
    note_type_ids = get_note_type_ids(deck_id)
    mm = ModelManager(mw.col)
    if len(note_type_ids) > 1:
        
        note_type_names = [nt.name for nt in mm.all_names_and_ids() if nt.id in note_type_ids]
        note_type_choice = chooseList("Which Note Type is used for the relevant vocabulary?", note_type_names)
        note_type_id = note_type_ids[note_type_choice]
        note_type_name = note_type_names[note_type_choice]
    elif len(note_type_ids) < 1:
        showInfo('No cards found.')
        return
    else:
        note_type_id = note_type_ids[0]
        note_type_name = mm.name(note_type_id)
    return note_type_id, note_type_name
        
def get_note_type_ids(deck_id, ):
    note_type_ids = []
    for row in mw.col.db.execute(
        'SELECT distinct mid FROM notes WHERE id IN (SELECT nid FROM'
        ' cards WHERE did = ?) ORDER BY id', deck_id):
        mid = row[0]
        note_type_ids.append(mid)
    return note_type_ids

def get_note_ids(deck_id, tag):
    note_ids = []
    for row in mw.col.db.execute(
        'SELECT id FROM notes WHERE mid = ? AND id IN (SELECT nid FROM'
        ' cards WHERE did = ?) ORDER BY id', note_type, deck_id):
        nid = row[0]
        note_ids.append(nid)
    return note_ids

def select_note_fields_all(note_id):
    example_row = mw.col.db.first(
        'SELECT flds FROM notes WHERE id = ?', note_id)
    example_flds = example_row[0].split('\x1f')
    choices = ['[{}] {}'.format(i, fld[:20]) for i, fld
               in enumerate(example_flds)]
    expr_idx = chooseList(
        'Which field contains the Japanese expression?', choices
        )
    if expr_idx == None:
        return None, None, None
    reading_idx = chooseList(
        'Which field contains the reading?', choices
        )
    if reading_idx == None:
        return None, None, None
    output_idx = chooseList(
        'Which field should the pitch accent be shown in?', choices
        )
    if output_idx == None:
        return None, None, None
    return expr_idx, reading_idx, output_idx

def select_field(msg, deck_id):
    dm = DeckManager(mw.col)
    deck = dm.get(deck_id)

def ensure_note_types_exist():
    pass

def create_verb_deck():
    deck_id, deck_name = create_deck(deck_name[0])

def create_adjective_deck():
    deck_id, deck_name = create_deck(deck_name[0])

def update_verb_deck():
    deck_id, deck_name = select_deck("Which deck would you like to update?")
    source_deck_id, source_deck_name = select_deck("Which deck should be used as the source content?")
    ichidan_tag = select_tag("Which tag is used for ichidan verbs?")
    godan_tag = select_tag("Which tag is used for godan verbs?")
    irregular_tag = select_tag("Which tag is used for irregular verbs?")
    ichidan_notes = mw.col.find_notes(f"tag:{ichidan_tag}")
    godan_notes = mw.col.find_notes(f"tag:{godan_tag}")
    irregular_notes = mw.col.find_notes(f"tag:{irregular_tag}")
    import genanki
    showInfo(f"Ichidan: {len(ichidan_notes)}")
    ensure_note_types_exist()
    # expr_idx, rdng_idx, out_idx = select_note_fields_all(note_ids[0])
    # if None in [expr_idx, rdng_idx, out_idx]:
    #     return
    

def update_adjective_deck():
    deck_id, deck_name = select_deck("Which deck would you like to update?")

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
