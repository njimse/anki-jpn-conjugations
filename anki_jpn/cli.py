import os
import copy
import argparse
from importlib import resources as impresources

import anki.collection
import genanki

import anki_jpn.resources.verbs
from anki_jpn.verbs import generate_verb_forms, godan_stem_mapping, VerbClass
from anki_jpn.util import delta_split
import anki_jpn.resources

def generate_verb_notes(model, deck, note, verb_class):
    expression, meaning, reading = note.values()
    reading = reading.split('<')[0].strip()
    if expression[-1] in godan_stem_mapping.keys():
        known_forms = generate_verb_forms(reading, verb_class)
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

    deck = anki.collection.Collection(args.input)

    css_file = impresources.files(anki_jpn.resources.verbs)/'style.css'
    with css_file.open("rt") as f:
        card_css = f.read()
    verb_front_template_file = impresources.files(anki_jpn.resources.verbs)/'front_template.html'
    verb_back_template_file = impresources.files(anki_jpn.resources.verbs)/'back_template.html'
    with verb_front_template_file.open('rt') as f:
        verb_front_template = f.read()
    with verb_back_template_file.open('rt') as f:
        verb_back_template = f.read()
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
         "qfmt": verb_front_template,
         "afmt": verb_back_template}
    ])
    new_deck = genanki.Deck(args.deck_id, args.deck_name)

    for verb_tag in [args.ichidan, args.godan, args.irregular]:
        verb_ids = deck.find_notes(f"tag:{verb_tag}")
        for note_id in verb_ids:
            note = deck.get_note(note_id)
            generate_verb_notes(new_model, new_deck, note, verb_tag2class[verb_tag])
    outdir = os.path.dirname(os.path.abspath(args.output))
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    genanki.Package(new_deck).write_to_file(args.output)

def main_cli():

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    parser.add_argument('-o', '--output')

    parser.add_argument('--model-id', dest='model_id', default=1942314097)
    parser.add_argument('--model-name', dest='model_name', default='Japanese Conjugations')
    parser.add_argument('--deck-id', dest='deck_id', default=1632732671)
    parser.add_argument('--deck-name', dest='deck_name', default="Japanese Verb Conjugations")

    parser.add_argument('--irregular', default='irregular-verb')
    parser.add_argument('--ichidan', default='ichidan-verb')
    parser.add_argument('--godan', default='godan-verb')
    parser.add_argument('--na-adj', dest='na_adj', default='na-adjective')
    parser.add_argument('--i-adj', dest='i_adj', default='i-adjective')
    args = parser.parse_args()

    main(args)