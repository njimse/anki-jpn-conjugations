"""Addon for creating notes focused on Japanese conjugation"""
import os
import sys
from typing import List
# import the main window object (mw) from aqt
from aqt import mw
from aqt.forms.taglimit import Ui_Dialog
# import the "show info" tool from utils.py
from aqt.utils import showInfo, Qt, disable_help_button, restoreGeom, saveGeom, showWarning, tr
from aqt.filtered_deck import FilteredDeckConfigDialog
# from aqt.taglimit import TagLimit
# import all of the Qt GUI library
from aqt.qt import *

from anki.decks import DeckManager
from anki.tags import TagManager
# from anki.scheduler.base import CustomStudyDefaults
from anki.buildinfo import version as anki_version

# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from .version import __version__ as anki_jpn_version
from .models import (
    add_or_update_verb_model, add_or_update_adjective_model
)
from .enums import VerbClass, AdjectiveClass
from .decks import DeckUpdater, DeckSearcher
from .config import ConfigManager
anki_version_info = tuple(int(x) for x in anki_version.split('.'))
config = ConfigManager(mw.addonManager.getConfig(__name__))

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

    solution copied from https://github.com/IllDepence/anki_add_pitch_plugin/
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

def get_relevant_model_fields(model_name):
    field_names = [f['name'] for f in mw.col.models.by_name(model_name)['flds']]
    expression_index = customChooseList(f"For the '{model_name}' note type, Which field contains the expression?", field_names)
    if expression_index is None:
        return None, None, None
    meaning_index = customChooseList(f"For the '{model_name}' note type, Which field contains the meaning?", field_names)
    if meaning_index is None:
        return None, None, None
    reading_index = customChooseList(f"For the '{model_name}' note type, Which field contains the reading?", field_names)
    if reading_index is None:
        return None, None, None
    
    return field_names[expression_index], field_names[meaning_index], field_names[reading_index]


def update_adjectives():
    target_deck_id, target_deck_name = select_deck("Which deck would you like to update?")
    if target_deck_id is None:
        return
    source_deck_id, source_deck_name = select_deck("Which deck should be used as the source content?")
    if source_deck_id is None:
        return
    
    if config.adjective_tags_empty(source_deck_name):
        i_tag = select_tag("Which tag is used for i-adjectives?")
        config.add_tag(source_deck_name, i_tag, AdjectiveClass.I)
        na_tag = select_tag("Which tag is used for na-adjectives?")
        config.add_tag(source_deck_name, na_tag, AdjectiveClass.NA)
        general_tag = select_tag("Which tag is used for adjectives in general?")
        config.add_tag(source_deck_name, general_tag, AdjectiveClass.GENERAL)

        if config.adjective_tags_empty(source_deck_name):
            showInfo("At least one tag must be specified for i-adjectives, na-adjectives, or general adjectives")
            return

        mw.addonManager.writeConfig(__name__, config.dump())

    adj_model_name = config.adjective_model_name()
    add_or_update_adjective_model(mw.col.models, adj_model_name, config.get_colors())
    mw.col.fix_integrity()
    dest_model = mw.col.models.by_name(adj_model_name)
    deck_updater = DeckUpdater(mw.col, target_deck_id, dest_model, config)

    deck_searcher = DeckSearcher(mw.col, source_deck_id, config)
    note_ids, relevant_models = deck_searcher.find_adjectives(dest_model['name'])
    
    for model_name in relevant_models:
        if config.model_fields_empty(model_name):
            relevant_fields = get_relevant_model_fields(model_name)
            if any(not f for f in relevant_fields):
                showInfo("Expression, meaning, and reading fields must be specified for all relevant note types")
            config.add_model_fields(model_name, *relevant_fields)

    mw.addonManager.writeConfig(__name__, config.dump())

    for adj_type, note_id_list in note_ids.items():
        for note_id in note_id_list:
            note = mw.col.get_note(note_id)
            deck_updater.add_note_to_deck(note, adj_type)

    new_notes, modified_notes, failed_notes = deck_updater.summary()
    showInfo(f"Added {new_notes} new note(s)\nModified {modified_notes} note(s)\nFailed to conjugate {failed_notes} note(s)")

def update_verbs():
    target_deck_id, target_deck_name = select_deck("Which deck would you like to update?")
    if target_deck_id is None:
        return
    source_deck_id, source_deck_name = select_deck("Which deck should be used as the source content?")
    if source_deck_id is None:
        return
    
    if config.verb_tags_empty(source_deck_name):
        ichidan_tag = select_tag("Which tag is used for ichidan verbs?")
        config.add_tag(source_deck_name, ichidan_tag, VerbClass.ICHIDAN)
        godan_tag = select_tag("Which tag is used for godan verbs?")
        config.add_tag(source_deck_name, godan_tag, VerbClass.GODAN)
        irregular_tag = select_tag("Which tag is used for irregular verbs?")
        config.add_tag(source_deck_name, irregular_tag, VerbClass.IRREGULAR)
        general_tag = select_tag("Which tag is used for verbs in general?")
        config.add_tag(source_deck_name, general_tag, VerbClass.GENERAL)

        if config.verb_tags_empty(source_deck_name):
            showInfo("At least one tag must be specified for ichidan, godan, irregular, or general adjectives")
            return

        mw.addonManager.writeConfig(__name__, config.dump())

    verb_model_name = config.verb_model_name()
    add_or_update_verb_model(mw.col.models, verb_model_name, config.get_colors())
    mw.col.fix_integrity()
    dest_model = mw.col.models.by_name(verb_model_name)
    deck_updater = DeckUpdater(mw.col, target_deck_id, dest_model, config)

    deck_searcher = DeckSearcher(mw.col, source_deck_id, config)
    note_ids, relevant_models = deck_searcher.find_verbs(dest_model['name'])

    for model_name in relevant_models:
        if config.model_fields_empty(model_name):
            relevant_fields = get_relevant_model_fields(model_name)
            if any(not f for f in relevant_fields):
                showInfo("Expression, meaning, and reading fields must be specified for all relevant note types")
            config.add_model_fields(model_name, *relevant_fields)

    mw.addonManager.writeConfig(__name__, config.dump())

    for verb_type, note_id_list in note_ids.items():
        for note_id in note_id_list:
            note = mw.col.get_note(note_id)
            card_ids = mw.col.find_cards(f"nid:{note_id}")
            deck_updater.add_note_to_deck(note, verb_type)

    new_notes, modified_notes, failed_notes = deck_updater.summary()
    showInfo(f"Added {new_notes} new note(s)\nModified {modified_notes} note(s)\nFailed to conjugate {failed_notes} note(s)")

class CardLimitItem:
    name: str
    include: bool
    exclude: bool

    def __init__(self, name: str, include: bool = False, exclude: bool = False):
        self.name = name
        self.include = include
        self.exclude = exclude

class CardLimit(QDialog):
    def __init__(
        self,
        parent: QWidget,
        tags: List[CardLimitItem]
    ) -> None:
        "Ask user to select tags. on_success() will be called with selected included and excluded tags."
        QDialog.__init__(self, parent, Qt.WindowType.Window)
        self.tags = tags
        self.form = Ui_Dialog()
        self.form.setupUi(self)
        self.form.activeCheck.setText("Select one or more of these conjugations to include")
        self.form.label.setText("Select conjugations to exclude")
        self.include_list = None
        self.exclude_list = None
        disable_help_button(self)
        s = QShortcut(
            QKeySequence("ctrl+d"),
            self.form.activeList,
            context=Qt.ShortcutContext.WidgetShortcut,
        )
        qconnect(s.activated, self.form.activeList.clearSelection)
        s = QShortcut(
            QKeySequence("ctrl+d"),
            self.form.inactiveList,
            context=Qt.ShortcutContext.WidgetShortcut,
        )
        qconnect(s.activated, self.form.inactiveList.clearSelection)
        self.build_tag_lists()
        restoreGeom(self, "cardLimit")
        self.open()

    def build_tag_lists(self) -> None:
        def add_tag(tag: str, select: bool, list: QListWidget) -> None:
            item = QListWidgetItem(tag.replace("_", " "))
            list.addItem(item)
            if select:
                idx = list.indexFromItem(item)
                list_selection_model = list.selectionModel()
                assert list_selection_model is not None
                list_selection_model.select(
                    idx, QItemSelectionModel.SelectionFlag.Select
                )

        had_included_tag = False

        for tag in self.tags:
            if tag.include:
                had_included_tag = True
            add_tag(tag.name, tag.include, self.form.activeList)
            add_tag(tag.name, tag.exclude, self.form.inactiveList)

        if had_included_tag:
            self.form.activeCheck.setChecked(True)

    def reject(self) -> None:
        QDialog.reject(self)

    def accept(self) -> None:
        include_tags = []
        exclude_tags = []
        want_active = self.form.activeCheck.isChecked()
        for c, tag in enumerate(self.tags):
            # active
            if want_active:
                item = self.form.activeList.item(c)
                idx = self.form.activeList.indexFromItem(item)
                active_list_selection_model = self.form.activeList.selectionModel()
                assert active_list_selection_model is not None
                if active_list_selection_model.isSelected(idx):
                    include_tags.append(tag.name)
            # inactive
            item = self.form.inactiveList.item(c)
            idx = self.form.inactiveList.indexFromItem(item)
            inactive_list_selection_model = self.form.inactiveList.selectionModel()
            assert inactive_list_selection_model is not None
            if inactive_list_selection_model.isSelected(idx):
                exclude_tags.append(tag.name)

        if (len(include_tags) + len(exclude_tags)) > 100:
            showWarning(with_collapsed_whitespace(tr.errors_100_tags_max()))
            return

        saveGeom(self, "cardLimit")
        QDialog.accept(self)
        self.include_list = include_tags
        self.exclude_list = exclude_tags

def create_filtered_deck():
    target_deck_id, target_deck_name = select_deck("Which deck has the conjugation notes to be filtered?")
    if target_deck_id is None:
        return
    
    adj_model_name = config.adjective_model_name()
    verb_model_name = config.verb_model_name()
    add_or_update_verb_model(mw.col.models, verb_model_name, config.get_colors())
    mw.col.fix_integrity()
    add_or_update_adjective_model(mw.col.models, adj_model_name, config.get_colors())
    mw.col.fix_integrity()

    conjugation_template_names = set()
    verb_model = mw.col.models.by_name(verb_model_name)
    conjugation_template_names.update(t['name'] for t in verb_model['tmpls'])
    adj_model = mw.col.models.by_name(adj_model_name)
    conjugation_template_names.update(t['name'] for t in adj_model['tmpls'])
    card_list = []
    for conjugation_template in sorted(conjugation_template_names):
        card_list.append(CardLimitItem(name=conjugation_template))

    cl = CardLimit(mw, card_list)
    cl.exec()
    if cl.include_list is None or cl.exclude_list is None:
        return

    if len(cl.include_list) > 1:
        include_query = "(" + " OR ".join(f'"card:{card_name}"' for card_name in cl.include_list) + ")"
    elif len(cl.include_list) == 1:
        include_query = f'"card:{cl.include_list[0]}"'
    else:
        include_query = ""
    
    if len(cl.exclude_list) > 1:
        exclude_query = "-(" + " OR ".join(f'"card:{card_name}"' for card_name in cl.exclude_list) + ")"
    elif len(cl.exclude_list) == 1:
        exclude_query = f'-"card:{cl.exclude_list[0]}"'
    else:
        exclude_query = ""
    
    query = f'"deck:{target_deck_name}" {include_query} {exclude_query}'.strip()

    FilteredDeckConfigDialog(mw, search=query)

def about_addon():
    showInfo(f"Version: {anki_jpn_version}")

# Create the menu items
conj_menu = QMenu("Japanese Conjugation", mw)
update_adjective_deck_action = conj_menu.addAction("Create/Update Adjectives")
update_verb_deck_action = conj_menu.addAction("Create/Update Verbs")
create_filtered_deck_action = conj_menu.addAction("Create Filtered Deck")
about_action = conj_menu.addAction("About Add-on")

# Add the triggers
update_verb_deck_action.triggered.connect(update_verbs)
update_adjective_deck_action.triggered.connect(update_adjectives)
create_filtered_deck_action.triggered.connect(create_filtered_deck)
about_action.triggered.connect(about_addon)

# Add the menu button to the "Tools" menu
mw.form.menuTools.addMenu(conj_menu)
