import os
import sys
import itertools
# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import getText, Qt
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

def get_qt_version():
    """ Return the version of Qt used by Anki.
    """

    qt_ver = 5  # assume 5 for now

    if Qt.__module__ == 'PyQt5.QtCore':
        # PyQt5
        # tested on aqt[qt5]
        qt_ver = 5
    elif Qt.__module__ == 'PyQt6.QtCore':
        # PyQt6
        # tested on aqt[qt6]
        qt_ver = 6

    # NOTE
    # when Anki runs with the temporary Qt5 compatibility
    # shims, Qt.__module__ is 'PyQt6.sip.wrappertype', but
    # then it should also be no problem to defer to 5

    return qt_ver

def customChooseList(msg, choices, startrow=0):
    """ Copy of https://github.com/ankitects/anki/blob/main/
        qt/aqt/utils.py but with a cancel button and title
        parameter added.
    """

    parent = mw.app.activeWindow()
    d = QDialog(parent)
    if get_qt_version() == 6:
        d.setWindowModality(Qt.WindowModality.WindowModal)
    else:
        d.setWindowModality(Qt.WindowModal)
    # d.setWindowTitle('TODO'  # added
    l = QVBoxLayout()
    d.setLayout(l)
    t = QLabel(msg)
    l.addWidget(t)
    c = QListWidget()
    c.addItems(choices)
    c.setCurrentRow(startrow)
    l.addWidget(c)
    if get_qt_version() == 6:
        buts = QDialogButtonBox.StandardButton.Ok | \
               QDialogButtonBox.StandardButton.Cancel
    else:
        buts = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
    bb = QDialogButtonBox(buts)
    l.addWidget(bb)
    bb.accepted.connect(d.accept)
    bb.rejected.connect(d.reject)
    l.addWidget(bb)
    if get_qt_version() == 6:
        ret = d.exec()  # 1 if Ok, 0 if Cancel or window closed
    else:
        ret = d.exec_()  # 1 if Ok, 0 if Cancel or window closed
    if ret == 0:
        return None  # can't be False b/c False == 0
    return c.currentRow()

def create_deck():
    deck_name = getText("What would you like to name the new deck?")
    if deck_name[0]:
        dm = DeckManager(mw.col)
        return dm.add_normal_deck_with_name(deck_name[0]).id, deck_name[0]

def select_deck(msg):
    dm = DeckManager(mw.col)
    all_decks = [d.name for d in dm.all_names_and_ids(skip_empty_default=True)]
    deck_choice = customChooseList(msg, all_decks)
    if deck_choice is None:
        return None, None
    deck_name = all_decks[deck_choice]
    deck_id = dm.id_for_name(deck_name)
    return deck_id, deck_name

def select_tag(msg):
    tm = TagManager(mw.col)
    all_tags = [t for t in tm.all()]
    tag_choice = customChooseList(msg, all_tags)
    if tag_choice is None:
        return None
    tag_name = all_tags[tag_choice]
    return tag_name

def get_field_mapping(model_info):
    for model_details in model_info.values():
        example_list = [f'{field_name}: {field_example}' for field_name, field_example in zip(model_details['fields'], model_details['example'].fields)]
        expression_index = customChooseList(f"For the '{model_details['name']}' note type, Which field contains the expression?", example_list)
        if expression_index is None:
            return
        meaning_index = customChooseList(f"For the '{model_details['name']}' note type, Which field contains the meaning?", example_list)
        if meaning_index is None:
            return
        reading_index = customChooseList(f"For the '{model_details['name']}' note type, Which field contains the reading?", example_list)
        if reading_index is None:
            return
        model_details["expression_index"] = expression_index
        model_details["meaning_index"] = meaning_index
        model_details["reading_index"] = reading_index

def _adjective_update(target_deck_id, target_deck_name):
    source_deck_id, source_deck_name = select_deck("Which deck should be used as the source content?")
    if source_deck_id is None:
        return
    i_tag = select_tag("Which tag is used for i-adjectivess?")
    if i_tag is None:
        return
    na_tag = select_tag("Which tag is used for na-adjectives?")
    if na_tag is None:
        return
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
    for m_info in model_infos.values():
        if any(fi not in m_info for fi in ('expression_index', 'meaning_index', 'reading_index')):
            return
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
    if source_deck_id is None:
        return
    ichidan_tag = select_tag("Which tag is used for ichidan verbs?")
    if ichidan_tag is None:
        return
    godan_tag = select_tag("Which tag is used for godan verbs?")
    if godan_tag is None:
        return
    irregular_tag = select_tag("Which tag is used for irregular verbs?")
    if irregular_tag is None:
        return
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
    for m_info in model_infos.values():
        if any(fi not in m_info for fi in ('expression_index', 'meaning_index', 'reading_index')):
            return
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
    if deck_id is None:
        return
    _verb_update(deck_id, deck_name)

def update_adjective_deck():
    deck_id, deck_name = select_deck("Which deck would you like to update?")
    if deck_id is None:
        return
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
