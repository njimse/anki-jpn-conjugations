"""Command Line Interface (CLI) methods"""
import os
import shutil
import tempfile
import argparse
from typing import List, Tuple, Optional

import anki.collection
import anki.stdmodels
import anki.notes
import anki.exporting

from anki_jpn.enums import Formality, Form, VerbClass, AdjectiveClass
from anki_jpn.verbs import generate_verb_forms, GODAN_STEM_ENDINGS
from anki_jpn.adjectives import generate_adjective_forms
from anki_jpn.models import (
    add_or_update_verb_model, add_or_update_adjective_model,
    VERB_COMBOS, ADJECTIVE_COMBOS
)



def rollover_note(old_note: anki.notes.Note, new_note: anki.notes.Note,
                  expression_index: int, meaning_index: int, reading_index: int) -> None:
    """Copy relevant fields from an old note into a new note

    Parameters
    ----------
    old_note : anki.notes.Note
        Old note from which information will be copied
    new_note : anki.notes.Note
        New note where information will be added
    expression_index : int
        Index in the old note for the "expression" field
    meaning_index : int
        Index in the old note for the "meaning" field
    reading_index : int
        Index in the old note for the "reading" field
    """

    new_note.fields = [
        old_note.fields[expression_index],
        old_note.fields[meaning_index],
        old_note.fields[reading_index]
    ]

def expand_note(note: anki.notes.Note, combo_list: List[Tuple[Optional[Formality], Form]],
                forms: List[Tuple[str, Optional[Formality], Form]]) -> None:
    """Expand a note with the provided conjugations

    Parameters
    ----------
    note : anki.notes.Note
        Note to be expanded with conjugations
    combo_list : List[Tuple[Optional[Formality], Form]]
        List of combos. The expectation is that the combo_list follows the same order as the fields
        that are expected for the target Note type
    forms : List[Tuple[str, Optional[Formality], Form]]
        List of conjugations and their corresponding formality and form information.
    """

    note_fields = ['']*len(combo_list)

    for conjugation, form, formality in forms:
        note_fields[combo_list.index((formality, form))] = conjugation

    note.fields.extend(note_fields)
    for t in note.tags:
        note.add_tag(t)

def looks_like_a_verb(note: anki.notes.Note, expression_index: int) -> bool:
    """Check a note to see if it looks like a verb

    Parameters
    ----------
    note : anki.notes.Note
        Note to be inspected
    expression_index : int
        Index of the expression field

    Returns
    -------
    bool
        True if the input note seems like a verb. False otherwise
    """

    expression = note.values()[expression_index]
    if expression[-1] in GODAN_STEM_ENDINGS:
        return True
    return False

def looks_like_an_adjective(note: anki.notes.Note, expression_index: int) -> bool:
    """Check a note to see if it looks like an adjective

    Parameters
    ----------
    note : anki.notes.Note
        Note to be inspected
    expression_index : int
        Index of the expression field

    Returns
    -------
    bool
        True if the input note seems like an adjective. False otherwise
    """

    expression = note.values()[expression_index]
    if expression.endswith('い') or expression.endswith('な'):
        return True
    return False

def main(args): # pylint: disable=R0914
    """Main function for generating verb and adjective conjugation decks"""

    # create a mapping from the verb tags to the corresponding VerbClass
    verb_tag2class = {}
    adj_tag2class = {}
    verb_tag2class[args.ichidan] = VerbClass.ICHIDAN
    verb_tag2class[args.godan] = VerbClass.GODAN
    verb_tag2class[args.irregular] = VerbClass.IRREGULAR
    adj_tag2class[args.i_adj] = AdjectiveClass.I
    adj_tag2class[args.na_adj] = AdjectiveClass.NA

    col = anki.collection.Collection(args.input) # pylint: disable=E1101
    temp_dir_name = tempfile.mkdtemp()
    os.makedirs(os.path.join(temp_dir_name, 'collection.media'))
    new_collection_file = os.path.join(temp_dir_name, "collection.anki2")

    new_col = anki.collection.Collection(new_collection_file)
    add_or_update_verb_model(new_col.models, "Verb Conjugations")
    add_or_update_adjective_model(new_col.models, "Adjective Conjugations")
    verb_model = new_col.models.by_name("Verb Conjugations")
    adj_model = new_col.models.by_name("Adjective Conjugations")
    verb_deck_id = new_col.decks.id(args.verb_deck_name, create=True)
    adj_deck_id = new_col.decks.id(args.adj_deck_name, create=True)

    for verb_tag in [args.ichidan, args.godan, args.irregular]:
        verb_ids = col.find_notes(f"tag:{verb_tag}")
        for note_id in verb_ids:
            old_note = col.get_note(note_id)
            if looks_like_a_verb(old_note, args.expression_index):
                reading = old_note.fields[args.reading_index].split('<')[0].strip()
                known_forms = generate_verb_forms(reading, verb_tag2class[verb_tag])
                new_note = anki.notes.Note(new_col, verb_model)
                rollover_note(old_note, new_note,
                              args.expression_index, args.meaning_index, args.reading_index)
                expand_note(new_note, VERB_COMBOS, known_forms)
                new_col.add_note(new_note, verb_deck_id)

    for adj_tag in [args.i_adj, args.na_adj]:
        adj_ids = col.find_notes(f"tag:{adj_tag}")
        for note_id in adj_ids:
            old_note = col.get_note(note_id)
            if looks_like_an_adjective(old_note, args.expression_index):
                reading = old_note.fields[args.reading_index].split('<')[0].strip()
                known_forms = generate_adjective_forms(reading, adj_tag2class[adj_tag])
                new_note = anki.notes.Note(new_col, adj_model)
                rollover_note(old_note, new_note,
                              args.expression_index, args.meaning_index, args.reading_index)
                expand_note(new_note, ADJECTIVE_COMBOS, known_forms)
                new_col.add_note(new_note, adj_deck_id)

    outdir = os.path.dirname(os.path.abspath(args.output))
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    exporter = anki.exporting.AnkiPackageExporter(new_col)
    exporter.exportInto(args.output)
    new_col.close()
    shutil.rmtree(temp_dir_name)

def main_cli():
    """Console script for generating verb and adjective decks"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    parser.add_argument('-o', '--output')

    parser.add_argument('--verb-deck-name', dest='verb_deck_name',
                        default="Japanese Verb Conjugations")
    parser.add_argument('--adj-deck-name', dest='adj_deck_name',
                        default="Japanese Adjective Conjugations")

    parser.add_argument('--expression-index', dest='expression_index', default=0, type=int)
    parser.add_argument('--meaning-index', dest='meaning_index', default=1, type=int)
    parser.add_argument('--reading-index', dest='reading_index', default=2, type=int)

    parser.add_argument('--irregular', default='irregular-verb')
    parser.add_argument('--ichidan', default='ichidan-verb')
    parser.add_argument('--godan', default='godan-verb')
    parser.add_argument('--na-adj', dest='na_adj', default='na-adjective')
    parser.add_argument('--i-adj', dest='i_adj', default='i-adjective')
    args = parser.parse_args()

    main(args)
