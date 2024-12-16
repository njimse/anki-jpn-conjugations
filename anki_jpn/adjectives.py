from typing import List, Tuple, Optional
from anki_jpn.enums import AdjectiveClass, Form, Formality

def generate_adjective_forms(dictionary_form: str, verb_class: AdjectiveClass) -> List[Tuple[str, Form, Optional[Formality]]]:
    results = []
    # Polite forms
    results.append([polite_nonpast_positive(dictionary_form, verb_class), Form.NON_PAST, Formality.POLITE])
    results.append([polite_nonpast_negative(dictionary_form, verb_class), Form.NON_PAST_NEG, Formality.POLITE])
    results.append([polite_past_positive(dictionary_form, verb_class), Form.PAST, Formality.POLITE])
    results.append([polite_past_negative(dictionary_form, verb_class), Form.PAST_NEG, Formality.POLITE])

    # Plain forms
    results.append([plain_nonpast_positive(dictionary_form, verb_class), Form.NON_PAST, Formality.PLAIN])
    results.append([plain_nonpast_negative(dictionary_form, verb_class), Form.NON_PAST_NEG, Formality.PLAIN])
    results.append([plain_past_positive(dictionary_form, verb_class), Form.PAST, Formality.PLAIN])
    results.append([plain_past_negative(dictionary_form, verb_class), Form.PAST_NEG, Formality.PLAIN])

    # formality-constant
    results.append([te(dictionary_form, verb_class), Form.TE, None])

    return results

def get_stem(dictionary_form: str) -> str:
    if dictionary_form.endswith('いい'):
        stem = dictionary_form[:-2] + 'よ'
    else:
        stem = dictionary_form[:-1]
    return stem

def polite_nonpast_positive(dictionary_form: str, adj_class: AdjectiveClass):
    if adj_class == AdjectiveClass.NA:
        ending = 'です'
        completion = dictionary_form[:-1] + ending
    else:
        ending = 'です'
        completion = dictionary_form + ending
    return completion

def polite_nonpast_negative(dictionary_form: str, adj_class: AdjectiveClass):
    stem = get_stem(dictionary_form)
    if adj_class == AdjectiveClass.NA:
        ending = 'じゃないです'
    else:
        ending = 'くないです'
    completion = stem + ending
    return completion

def polite_past_positive(dictionary_form: str, adj_class: AdjectiveClass):
    stem = get_stem(dictionary_form)
    if adj_class == AdjectiveClass.NA:
        ending = 'でした'
    else:
        ending = 'かったです'
    completion = stem + ending
    return completion

def polite_past_negative(dictionary_form: str, adj_class: AdjectiveClass):
    stem = get_stem(dictionary_form)
    if adj_class == AdjectiveClass.NA:
        ending = 'じゃなかったです'
    else:
        ending = 'くなかったです'
    completion = stem + ending
    return completion

def te(dictionary_form: str, adj_class: AdjectiveClass):
    stem = get_stem(dictionary_form)
    if adj_class == AdjectiveClass.NA:
        ending = 'で'
    else:
        ending = 'くて'
    completion = stem + ending
    return completion

def plain_nonpast_positive(dictionary_form: str, adj_class: AdjectiveClass):
    stem = dictionary_form[:-1]
    if adj_class == AdjectiveClass.NA:
        ending = 'だ'
    else:
        ending = 'い'
    completion = stem + ending
    return completion

def plain_nonpast_negative(dictionary_form: str, adj_class: AdjectiveClass):
    stem = get_stem(dictionary_form)
    if adj_class == AdjectiveClass.NA:
        ending = 'じゃない'
    else:
        ending = 'くない'
    completion = stem + ending
    return completion

def plain_past_positive(dictionary_form: str, adj_class: AdjectiveClass):
    stem = get_stem(dictionary_form)
    if adj_class == AdjectiveClass.NA:
        ending = 'だった'
    else:
        ending = 'かった'
    completion = stem + ending
    return completion

def plain_past_negative(dictionary_form: str, adj_class: AdjectiveClass):
    stem = get_stem(dictionary_form)
    if adj_class == AdjectiveClass.NA:
        ending = 'じゃなかった'
    else:
        ending = 'くなかった'
    completion = stem + ending
    return completion
