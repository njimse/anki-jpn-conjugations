import argparse
import random
import itertools
import anki.collection
import genanki
from japverbconj.constants.enumerated_types import BaseForm, VerbClass, Formality, Tense, Polarity
from japverbconj.verb_form_gen import generate_japanese_verb_by_str

from anki_jpn.verbs import conjugate_godan, conjugate_ichidan, Conjugation

CSS = """.card {
  font-family: arial;
  font-size: 25px;
  text-align: center;
  color: black;
  background-color: white;
}
.jp { font-size: 30px }
.win .jp { font-family: "MS Mincho", "ＭＳ 明朝"; }
.mac .jp { font-family: "Hiragino Mincho Pro", "ヒラギノ明朝 Pro"; }
.linux .jp { font-family: "Kochi Mincho", "東風明朝"; }
.mobile .jp { font-family: "Hiragino Mincho ProN"; }"""

formality_strings = {
    Formality.POLITE: 'polite',
    Formality.PLAIN: 'plain'
}
tense_strings = {
    Tense.PAST: 'past',
    Tense.NONPAST: 'nonpast'
}
polarity_strings = {
    Polarity.POSITIVE: 'positive',
    Polarity.NEGATIVE: 'negative'
}
form_strings = {
    BaseForm.PLAIN: "pla",
    BaseForm.POLITE: "pol",
    BaseForm.TE: "te",
    BaseForm.TA: "ta",
    BaseForm.TARA: "tara",
    BaseForm.TARI: "tari",
    BaseForm.CONDITIONAL: "cond",
    BaseForm.VOLITIONAL: "vol",
    BaseForm.POTENTIAL: "pot",
    BaseForm.IMPERATIVE: "imp",
    BaseForm.PROVISIONAL: "prov",
    BaseForm.CAUSATIVE: "caus",
    BaseForm.PASSIVE: "pass",
}


def generate_notes(note):
    if 'ichidan-verb' in note.tags:
        verb_class = VerbClass.ICHIDAN
    elif 'godan-verb' in note.tags:
        verb_class = VerbClass.GODAN
    else:
        verb_class = VerbClass.IRREGULAR
    expression, meaning, reading = note.values()
    for formality in formality_strings.keys():
        for tense in tense_strings.keys():
            for polarity in polarity_strings.keys():
                conjugation = generate_japanese_verb_by_str(expression, verb_class, formality, tense, polarity)
                new_note = genanki.Note(model=new_model, fields=[conjugation, expression, meaning, reading, tense, formality, polarity])

    pass

def main(args):
    deck = anki.collection.Collection(args.input)

    new_model = genanki.Model(1942314097, "Japanese Conjugations", css=CSS)
    new_model.set_fields([{"name": "conjugation"},
                          {"name": "expression"},
                          {"name": "meaning"},
                          {"name": "reading"},
                          {"name": "tense"},
                          {"name": "form"},
                          {"name": "polarity"}
                          ])
    new_model.set_templates([
        {"name": "JapaneseConjugation",
         "qfmt": "{{expression}}<hr>{{formality}}<br>{{polarity}}<br>{{tense}}",
         "afmt": "{{FrontSide}}<hr id=answer>{{conjugation}}"}
    ])
    new_deck = genanki.Deck(1632732671, "Japanese Verb Conjugations")

    ichidan_verb_ids = random.sample(deck.find_cards("tag:ichidan-verb"), k=5)
    godan_verb_ids = random.sample(deck.find_cards("tag:godan-verb"), k=5)

    for card_id in ichidan_verb_ids:
        expression, meaning, reading = deck.get_card(card_id).note().values()
        if not expression.endswith('る'):
            continue
        import pdb; pdb.set_trace()
        if '<!--' in reading:
            reading = reading.split('<!-- accent_start')[0]
            
        tense = "non-past"
        posneg = "positive"
        formality = "polite"
        conjugation = conjugate_ichidan(expression, Conjugation.NON_PAST)
        new_note = genanki.Note(model=new_model, fields=[expression, meaning, reading, tense, formality, posneg, conjugation])
        new_deck.add_note(new_note)

        posneg = "negative"
        conjugation = conjugate_ichidan(expression, Conjugation.NON_PAST_NEGATIVE)
        new_note = genanki.Note(model=new_model, fields=[expression, meaning, reading, tense, formality, posneg, conjugation])
        new_deck.add_note(new_note)

    for card_id in godan_verb_ids:
        expression, meaning, reading = deck.get_card(card_id).note().values()
        if not expression.endswith('る'):
            continue
        if '<!-- accent_start' in reading:
            reading = reading.split('<!-- accent_start')[0]
        tense = "non-past"
        posneg = "positive"
        formality = "polite"
        conjugation = conjugate_godan(expression, Conjugation.NON_PAST)
        new_note = genanki.Note(model=new_model, fields=[expression, meaning, reading, tense, formality, posneg, conjugation])
        new_deck.add_note(new_note)

        posneg = "negative"
        conjugation = conjugate_godan(expression, Conjugation.NON_PAST_NEGATIVE)
        new_note = genanki.Note(model=new_model, fields=[expression, meaning, reading, tense, formality, posneg, conjugation])
        new_deck.add_note(new_note)
        
    # ichidan_verbs = [deck.get_card(id).note().values()[0] for id in ichidan_verb_ids]

    # i_results = []
    # for i_verb in ichidan_verbs:
    #     if not i_verb.endswith("る"):
    #         continue
    #     i_results.append((i_verb, conjugate_ichidan(i_verb, Conjugation.NON_PAST), conjugate_ichidan(i_verb, Conjugation.NON_PAST_NEGATIVE)))

    # godan_verb_ids = random.sample(deck.find_cards("tag:godan-verb"), k=5)
    # godan_verbs = [deck.get_card(id).note().values()[0] for id in godan_verb_ids]
    # g_results = []
    # for g_verb in godan_verbs:
    #     g_results.append((g_verb, conjugate_godan(g_verb, Conjugation.NON_PAST), conjugate_godan(g_verb, Conjugation.NON_PAST_NEGATIVE)))

    
    # print ('ichidan verbs')
    # for r in i_results:
    #     print('{: <12}\t{: <12}\t{: <10}'.format(r[0], r[1], r[2]))

    # print ('godan verbs')
    # for r in g_results:
    #     print('{: <12}\t{: <12}\t{: <10}'.format(r[0], r[1], r[2]))


    # for record in itertools.chain(i_results, g_results):
    #     my_note = genanki.Note(model=new_model, fields=[record[0], "positive non-past", record[1]])
    #     new_deck.add_note(my_note)
        
    #     my_note = genanki.Note(model=new_model, fields=[record[0], "negative non-past", record[2]])
    #     new_deck.add_note(my_note)

    genanki.Package(new_deck).write_to_file(args.output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    parser.add_argument('-o', '--output')
    args = parser.parse_args()

    main(args)