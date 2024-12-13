import os
import copy
import argparse
from importlib import resources as impresources

import anki.collection
import genanki

import anki_jpn.resources.verbs
from anki_jpn.enums import VerbClass, AdjectiveClass
from anki_jpn.verbs import generate_verb_forms, godan_stem_mapping
from anki_jpn.adjectives import generate_adjective_forms
from anki_jpn.util import delta_split
import anki_jpn.resources

def generate_notes(model, deck, note, pos_class, generation_func):
    expression, meaning, reading = note.values()
    reading = reading.split('<')[0].strip()
    if isinstance(pos_class, VerbClass) and expression[-1] in godan_stem_mapping.keys() or \
        isinstance(pos_class, AdjectiveClass) and (expression.endswith('い') or expression.endswith('な')):

        known_forms = generation_func(reading, pos_class)
        for conjugation, form, formality in known_forms:
            conj_base, conj_ending = delta_split(reading, conjugation)
            formality_str = formality.value if formality is not None else ''
            all_tags = copy.deepcopy(note.tags)
            if formality_str:
                all_tags.append(formality_str)
            all_tags.append(form.value.replace(' ', '-'))
            new_note = genanki.Note(model=model, fields=[
                expression, meaning, reading, formality_str, form.value, conj_base, conj_ending
            ], tags=all_tags)
            deck.add_note(new_note)

def main(args):

    # create a mapping from the verb tags to the corresponding VerbClass
    verb_tag2class = {args.ichidan: VerbClass.ICHIDAN,
                      args.godan: VerbClass.GODAN,
                      args.irregular: VerbClass.IRREGULAR}
    adj_tag2class = {args.i_adj: AdjectiveClass.I,
                     args.na_adj: AdjectiveClass.NA}

    deck = anki.collection.Collection(args.input)

    css_file = impresources.files(anki_jpn.resources)/'style.css'
    with css_file.open("rt") as f:
        card_css = f.read()
    front_template_file = impresources.files(anki_jpn.resources)/'front_template.html'
    back_template_file = impresources.files(anki_jpn.resources)/'back_template.html'
    with front_template_file.open('rt') as f:
        front_template = f.read()
    with back_template_file.open('rt') as f:
        back_template = f.read()
    new_model = genanki.Model(args.model_id, args.model_name, css=card_css)
    new_model.set_fields([{"name": "expression"},
                          {"name": "meaning"},
                          {"name": "reading"},
                          {"name": "formality"},
                          {"name": "form"},
                          {"name": "conjugation base"},
                          {"name": "conjugation ending"}
                          ])
    new_model.set_templates([
        {"name": "JapaneseConjugation",
         "qfmt": front_template,
         "afmt": back_template}
    ])
    verb_deck = genanki.Deck(args.verb_deck_id, args.verb_deck_name)
    adj_deck = genanki.Deck(args.adj_deck_id, args.adj_deck_name)

    for verb_tag in [args.ichidan, args.godan, args.irregular]:
        verb_ids = deck.find_notes(f"tag:{verb_tag}")
        for note_id in verb_ids:
            note = deck.get_note(note_id)
            generate_notes(new_model, verb_deck, note, verb_tag2class[verb_tag], generate_verb_forms)

    for adj_tag in [args.i_adj, args.na_adj]:
        adj_ids = deck.find_notes(f"tag:{adj_tag}")
        for note_id in adj_ids:
            note = deck.get_note(note_id)
            generate_notes(new_model, adj_deck, note, adj_tag2class[adj_tag], generate_adjective_forms)

    outdir = os.path.dirname(os.path.abspath(args.output))
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    genanki.Package([verb_deck, adj_deck]).write_to_file(args.output)

def main_cli():

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    parser.add_argument('-o', '--output')

    parser.add_argument('--model-id', dest='model_id', default=1942314097)
    parser.add_argument('--model-name', dest='model_name', default='Japanese Conjugations')
    parser.add_argument('--verb-deck-id', dest='verb_deck_id', default=1632732671)
    parser.add_argument('--verb-deck-name', dest='verb_deck_name', default="Japanese Verb Conjugations")
    parser.add_argument('--adj-deck-id', dest='adj_deck_id', default=1632732672)
    parser.add_argument('--adj-deck-name', dest='adj_deck_name', default="Japanese Adjective Conjugations")

    parser.add_argument('--irregular', default='irregular-verb')
    parser.add_argument('--ichidan', default='ichidan-verb')
    parser.add_argument('--godan', default='godan-verb')
    parser.add_argument('--na-adj', dest='na_adj', default='na-adjective')
    parser.add_argument('--i-adj', dest='i_adj', default='i-adjective')
    args = parser.parse_args()

    main(args)