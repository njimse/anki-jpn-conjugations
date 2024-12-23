import os
# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect, getText, chooseList
# import all of the Qt GUI library
from aqt.qt import *

from anki.decks import DeckManager

def create_deck():
    deck_name = getText("What would you like to name the new deck?")
    if deck_name[0]:
        dm = DeckManager(mw.col)
        return dm.add_normal_deck_with_name(deck_name[0]), deck_name[0]

def select_deck():
    dm = DeckManager(mw.col)
    all_decks = [d.name for d in dm.all_names_and_ids(skip_empty_default=True)]
    deck_choice = chooseList("Which deck would you like to update?", all_decks)
    deck_name = all_decks[deck_choice]
    deck_id = dm.id_for_name(deck_name)
    return deck_id, deck_name

def create_verb_deck():
    deck_id, deck_name = create_deck(deck_name[0])

def create_adjective_deck():
    deck_id, deck_name = create_deck(deck_name[0])

def update_verb_deck():
    deck_id, deck_name = select_deck()

def update_adjective_deck():
    deck_id, deck_name = select_deck()

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
