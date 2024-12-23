"""Command Line Interface (CLI) methods"""
import os
import copy
import argparse

import anki.collection
import genanki

from anki_jpn.enums import VerbClass, AdjectiveClass, ModelType, VERB_COMBOS, ADJECTIVE_COMBOS
from anki_jpn.verbs import generate_verb_forms, godan_stem_mapping
from anki_jpn.adjectives import generate_adjective_forms
from anki_jpn.models import get_model

def generate_note(model, deck, note, pos_class, generation_func): # pylint: disable=R0914
    """Generate new note for the specified input note"""
    expression, meaning, reading = note.values()[:3]
    reading = reading.split('<')[0].strip()
    base_fields = [expression, meaning, reading]
    if isinstance(pos_class, VerbClass):
        combo_list = VERB_COMBOS
    else:
        combo_list = ADJECTIVE_COMBOS
    base_fields.extend(['']*len(combo_list))
    if isinstance(pos_class, VerbClass) and expression[-1] in list(godan_stem_mapping.keys()): # pylint: disable=C0201
        pass
    elif isinstance(pos_class, AdjectiveClass) and \
        (expression.endswith('い') or expression.endswith('な')):
        pass
    else:
        note_fields = copy.deepcopy(base_fields)
        known_forms = generation_func(reading, pos_class)

        for conjugation, form, formality in known_forms:
            note_fields[3 + combo_list.index((formality, form))] = conjugation

        new_note = genanki.Note(model=model, fields=note_fields, tags=note.tags)
        deck.add_note(new_note)

def main(args):
    """Main function for generating verb and adjective conjugation decks"""

    # create a mapping from the verb tags to the corresponding VerbClass
    verb_tag2class = {args.ichidan: VerbClass.ICHIDAN,
                      args.godan: VerbClass.GODAN,
                      args.irregular: VerbClass.IRREGULAR}
    adj_tag2class = {args.i_adj: AdjectiveClass.I,
                     args.na_adj: AdjectiveClass.NA}

    deck = anki.collection.Collection(args.input) # pylint: disable=E1101

    verb_model = get_model(args.verb_model_id, args.verb_model_name, model_type=ModelType.VERB)
    adj_model = get_model(args.adj_model_id, args.adj_model_name, model_type=ModelType.ADJECTIVE)

    verb_deck = genanki.Deck(args.verb_deck_id, args.verb_deck_name)
    adj_deck = genanki.Deck(args.adj_deck_id, args.adj_deck_name)

    for verb_tag in [args.ichidan, args.godan, args.irregular]:
        verb_ids = deck.find_notes(f"tag:{verb_tag}")
        for note_id in verb_ids:
            note = deck.get_note(note_id)
            generate_note(verb_model, verb_deck, note,
                           verb_tag2class[verb_tag], generate_verb_forms)

    for adj_tag in [args.i_adj, args.na_adj]:
        adj_ids = deck.find_notes(f"tag:{adj_tag}")
        for note_id in adj_ids:
            note = deck.get_note(note_id)
            generate_note(adj_model, adj_deck, note,
                           adj_tag2class[adj_tag], generate_adjective_forms)

    outdir = os.path.dirname(os.path.abspath(args.output))
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    genanki.Package([verb_deck, adj_deck]).write_to_file(args.output)

def main_cli():
    """Console script for generating verb and adjective decks"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    parser.add_argument('-o', '--output')

    parser.add_argument('--verb-model-id', dest='verb_model_id', default=1942314097)
    parser.add_argument('--verb-model-name', dest='verb_model_name',
                        default='Japanese Verb Conjugations (Recognition)')
    parser.add_argument('--adj-model-id', dest='adj_model_id', default=1942314098)
    parser.add_argument('--adj-model-name', dest='adj_model_name',
                        default='Japanese Adjective Conjugations (Recognition)')
    parser.add_argument('--verb-deck-id', dest='verb_deck_id', default=1632732671)
    parser.add_argument('--verb-deck-name', dest='verb_deck_name',
                        default="Japanese Verb Conjugations")
    parser.add_argument('--adj-deck-id', dest='adj_deck_id', default=1632732681)
    parser.add_argument('--adj-deck-name', dest='adj_deck_name',
                        default="Japanese Adjective Conjugations")

    parser.add_argument('--irregular', default='irregular-verb')
    parser.add_argument('--ichidan', default='ichidan-verb')
    parser.add_argument('--godan', default='godan-verb')
    parser.add_argument('--na-adj', dest='na_adj', default='na-adjective')
    parser.add_argument('--i-adj', dest='i_adj', default='i-adjective')
    args = parser.parse_args()

    main(args)
