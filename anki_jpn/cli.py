"""Command Line Interface (CLI) methods"""
import os
import copy
import shutil
import tempfile
import argparse

import anki.collection
import anki.stdmodels
import anki.notes
import anki.exporting

from anki_jpn.enums import VerbClass, AdjectiveClass, VERB_COMBOS, ADJECTIVE_COMBOS
from anki_jpn.verbs import generate_verb_forms, godan_stem_mapping
from anki_jpn.adjectives import generate_adjective_forms
from anki_jpn.models import add_adjective_conjugation_model, add_verb_conjugation_model

def generate_note(col, model, deck_id, note, pos_class, generation_func): # pylint: disable=R0914
    """Generate new note for the specified input note"""
    expression, meaning, reading = note.values()[:3]
    reading = reading.split('<')[0].strip()
    base_fields = [expression, meaning, reading]
    if isinstance(pos_class, VerbClass):
        combo_list = VERB_COMBOS
    else:
        combo_list = ADJECTIVE_COMBOS
    base_fields.extend(['']*len(combo_list))
    if isinstance(pos_class, VerbClass) and expression[-1] not in list(godan_stem_mapping.keys()): # pylint: disable=C0201
        pass
    elif isinstance(pos_class, AdjectiveClass) and \
        not (expression.endswith('い') or expression.endswith('な')):
        pass
    else:
        note_fields = copy.deepcopy(base_fields)
        known_forms = generation_func(reading, pos_class)

        for conjugation, form, formality in known_forms:
            note_fields[3 + combo_list.index((formality, form))] = conjugation

        new_note = anki.notes.Note(col, model)
        new_note.fields = note_fields
        for t in note.tags:
            new_note.add_tag(t)

        col.add_note(new_note, deck_id)

def main(args):
    """Main function for generating verb and adjective conjugation decks"""

    # create a mapping from the verb tags to the corresponding VerbClass
    verb_tag2class = {args.ichidan: VerbClass.ICHIDAN,
                      args.godan: VerbClass.GODAN,
                      args.irregular: VerbClass.IRREGULAR}
    adj_tag2class = {args.i_adj: AdjectiveClass.I,
                     args.na_adj: AdjectiveClass.NA}

    col = anki.collection.Collection(args.input) # pylint: disable=E1101
    temp_dir_name = tempfile.mkdtemp()
    os.makedirs(os.path.join(temp_dir_name, 'collection.media'))
    new_collection_file = os.path.join(temp_dir_name, "collection.anki2")

    new_col = anki.collection.Collection(new_collection_file)
    verb_model = add_verb_conjugation_model(new_col)
    new_col.models.add(verb_model)
    adj_model = add_adjective_conjugation_model(new_col)
    new_col.models.add(adj_model)

    verb_deck_id = new_col.decks.id(args.verb_deck_name, create=True)
    adj_deck_id = new_col.decks.id(args.adj_deck_name, create=True)


    for verb_tag in [args.ichidan, args.godan, args.irregular]:
        verb_ids = col.find_notes(f"tag:{verb_tag}")
        for note_id in verb_ids:
            note = col.get_note(note_id)
            generate_note(new_col, verb_model, verb_deck_id, note,
                        verb_tag2class[verb_tag], generate_verb_forms)

    for adj_tag in [args.i_adj, args.na_adj]:
        adj_ids = col.find_notes(f"tag:{adj_tag}")
        for note_id in adj_ids:
            note = col.get_note(note_id)
            generate_note(new_col, adj_model, adj_deck_id, note,
                        adj_tag2class[adj_tag], generate_adjective_forms)

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

    parser.add_argument('--irregular', default='irregular-verb')
    parser.add_argument('--ichidan', default='ichidan-verb')
    parser.add_argument('--godan', default='godan-verb')
    parser.add_argument('--na-adj', dest='na_adj', default='na-adjective')
    parser.add_argument('--i-adj', dest='i_adj', default='i-adjective')
    args = parser.parse_args()

    main(args)
