from typing import Optional, List, Tuple
from anki_jpn.enums import Form, Formality, VerbClass


godan_stem_mapping = {
    "う": "い",
    "く": "き",
    "す": "し",
    "つ": "ち",
    "ぬ": "に",
    "ふ": "ひ",
    "む": "み",
    "る": "り",
    "ぐ": "ぎ",
    "ず": "じ",
    "ぶ": "び",
    "ぷ": "ぴ"
}
godan_plain_stem_mapping = {
    "う": "わ",
    "く": "か",
    "す": "さ",
    "つ": "た",
    "ぬ": "な",
    "ふ": "は",
    "む": "ま",
    "る": "ら",
    "ぐ": "が",
    "ず": "ざ",
    "ぶ": "ば",
    "ぷ": "ぱ"
}
godan_te_mapping = {
    "う": "って",
    "つ": "って",
    "る": "って",
    "ぬ": "んで",
    "む": "んで",
    "ぶ": "んで",
    "く": "いて",
    "ぐ": "いで",
    "す": "して",
}

def generate_verb_forms(dictionary_form: str, verb_class: VerbClass) -> List[Tuple[str, Form, Optional[Formality]]]:
    results = []
    # Polite forms
    results.append([polite_nonpast_positive(dictionary_form, verb_class), Form.NON_PAST, Formality.POLITE])
    results.append([polite_nonpast_negative(dictionary_form, verb_class), Form.NON_PAST_NEG, Formality.POLITE])
    results.append([polite_past_positive(dictionary_form, verb_class), Form.PAST, Formality.POLITE])
    results.append([polite_past_negative(dictionary_form, verb_class), Form.PAST_NEG, Formality.POLITE])
    results.append([polite_volitional(dictionary_form, verb_class), Form.VOLITIONAL, Formality.POLITE])

    # Plain forms
    results.append([plain_nonpast_positive(dictionary_form, verb_class), Form.NON_PAST, Formality.PLAIN])
    results.append([plain_nonpast_negative(dictionary_form, verb_class), Form.NON_PAST_NEG, Formality.PLAIN])
    results.append([plain_past_positive(dictionary_form, verb_class), Form.PAST, Formality.PLAIN])
    results.append([plain_past_negative(dictionary_form, verb_class), Form.PAST_NEG, Formality.PLAIN])

    # formality-constant
    results.append([te(dictionary_form, verb_class), Form.TE, None])

    return results

def get_godan_stem(input, formality):
    if formality == Formality.POLITE:
        stem = input[:-1] + godan_stem_mapping[input[-1]]
    else:
        stem = input[:-1] + godan_plain_stem_mapping[input[-1]]
    return stem

def get_stem(dictionary_form: str, verb_class: VerbClass, formality: Formality= Formality.POLITE):
    if verb_class == VerbClass.ICHIDAN:
        stem = dictionary_form[:-1]
    elif verb_class == VerbClass.GODAN:
        stem = get_godan_stem(dictionary_form, formality)
    else:
        if dictionary_form.endswith("する"):
            stem = "し"
        elif dictionary_form.endswith("来[く]る"):
            stem = ""

def _masu_stem(dict: str, v_class: VerbClass, formality: Formality = Formality.POLITE):
    if v_class == VerbClass.ICHIDAN:
        stem = dict[:-1] # drop the る
    elif v_class == VerbClass.GODAN:
        stem = get_godan_stem(dict, formality)
    elif v_class == VerbClass.IRREGULAR:
        if dict.endswith('する'):
            stem = dict[:-2] + 'し'
        elif dict.endswith('来[く]る'):
            if formality == Formality.POLITE:
                stem = dict[:-5] + '来[き]'
            else:
                stem = dict[:-5] + '来[こ]'
    return stem

def polite_nonpast_positive(dictionary_form: str, verb_class: VerbClass):
    stem = _masu_stem(dictionary_form, verb_class)
    completion = stem + "ます"

    return completion

def polite_nonpast_negative(dictionary_form: str, verb_class: VerbClass):
    stem = _masu_stem(dictionary_form, verb_class)
    completion = stem + "ません"

    return completion

def polite_past_positive(dictionary_form: str, verb_class: VerbClass):
    stem = _masu_stem(dictionary_form, verb_class)
    completion = stem + "ました"

    return completion

def polite_past_negative(dictionary_form: str, verb_class: VerbClass):
    stem = _masu_stem(dictionary_form, verb_class)
    completion = stem + "ませんでした"

    return completion

def polite_volitional(dictionary_form: str, verb_class: VerbClass):
    stem = _masu_stem(dictionary_form, verb_class)
    completion = stem + "ましょう"

    return completion

def te(dictionary_form: str, verb_class: VerbClass):
    if verb_class == VerbClass.ICHIDAN:
        completion = dictionary_form[:-1] + "て"
    elif verb_class == VerbClass.GODAN:
        if dictionary_form.endswith('行[い]く'):
            completion = dictionary_form[:-1] + "って"
        else:
            completion = dictionary_form[:-1] + godan_te_mapping[dictionary_form[-1]]
    elif verb_class == VerbClass.IRREGULAR:
        if dictionary_form.endswith("する"):
            completion = dictionary_form[:-2] + "して"
        elif dictionary_form.endswith("来[く]る"):
            completion = dictionary_form[:-5] + "来[き]て"
    return completion

def plain_nonpast_positive(dictionary_form: str, verb_class: VerbClass):
    return dictionary_form

def plain_nonpast_negative(dictionary_form: str, verb_class: VerbClass):
    if dictionary_form.endswith('ある'):
        return 'ない'
    
    stem = _masu_stem(dictionary_form, verb_class, formality=Formality.PLAIN)
    completion = stem + 'ない'
    return completion

def plain_past_positive(dictionary_form: str, verb_class: VerbClass):
    te_form = te(dictionary_form, verb_class)
    if te_form.endswith('て'):
        ending = 'た'
    else: # ends with で
        ending = 'だ'
    completion = te_form[:-1] + ending

    return completion

def plain_past_negative(dictionary_form: str, verb_class: VerbClass):
    nai_form = plain_nonpast_negative(dictionary_form, verb_class)
    completion = nai_form[:-1] + 'かった'
    return completion