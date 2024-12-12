import os
import copy
import argparse
import anki.collection
import genanki

from anki_jpn.verbs import generate_forms, godan_stem_mapping, VerbClass
from anki_jpn.util import delta_split

CARD_CSS = """.card {
  font-family: arial;
  font-size: 25px;
  text-align: center;
  color: black;
  background-color: white;
}
.jp { font-size: 40px }
.win .jp { font-family: "MS Mincho", "ＭＳ 明朝"; }
.mac .jp { font-family: "Hiragino Mincho Pro", "ヒラギノ明朝 Pro"; }
.linux .jp { font-family: "Kochi Mincho", "東風明朝"; }
.mobile .jp { font-family: "Hiragino Mincho ProN"; }
table {
border: 1px solid black;
border-collapse: collapse;
}
td {
border: 1px solid black;
}
table td{
padding: 10px;
}
.ending {color: red}
.nightMode .ending {color: red}
.nightMode table tr td {border: 1px solid white}"""

def generate_verb_notes(model, deck, note, verb_class):
    expression, meaning, reading = note.values()
    reading = reading.split('<')[0].strip()
    if expression[-1] in godan_stem_mapping.keys():
        known_forms = generate_forms(reading, verb_class)
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

    new_model = genanki.Model(args.model_id, args.model_name, css=CARD_CSS)
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
         "qfmt": '<br><table align="center"><tr><td colspan=2><div class=jp>{{expression}}</div></td></tr><tr><td align="right">Formality</td><td align="left">{{formality}}</td></tr><tr><td align="right">Form</td><td align="left">{{form}}</td></tr></table>',
         "afmt": "{{FrontSide}}<br><div class=jp>{{furigana:conjugation base}}<span class=ending>{{furigana:conjugation ending}}</span></div><br>{{meaning}}<br>"}
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