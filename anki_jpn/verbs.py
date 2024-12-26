"""Methods pertaining to the conjugation of verbs"""
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
GODAN_STEM_ENDINGS = set(godan_stem_mapping.keys())

def generate_verb_forms(dictionary_form: str, verb_class: VerbClass)\
    -> List[Tuple[str, Form, Optional[Formality]]]:
    """Generate the known conjugations for the provided verb

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the adjective to be conjugated
    verb_class : AdjectiveClass
        Class of adjective to guide how conjugation should be performed

    Returns
    -------
    List of tuples
        Each tuple is the conjugation (string), Form, and Formality. Note that for the Te form,
        the formality will be provided as None
    """
    results = []
    # Polite forms
    results.append([polite_nonpast_positive(dictionary_form, verb_class),
                    Form.NON_PAST, Formality.POLITE])
    results.append([polite_nonpast_negative(dictionary_form, verb_class),
                    Form.NON_PAST_NEG, Formality.POLITE])
    results.append([polite_past_positive(dictionary_form, verb_class),
                    Form.PAST, Formality.POLITE])
    results.append([polite_past_negative(dictionary_form, verb_class),
                    Form.PAST_NEG, Formality.POLITE])
    results.append([polite_volitional(dictionary_form, verb_class),
                    Form.VOLITIONAL, Formality.POLITE])

    # Plain forms
    results.append([plain_nonpast_positive(dictionary_form),
                    Form.NON_PAST, Formality.PLAIN])
    results.append([plain_nonpast_negative(dictionary_form, verb_class),
                    Form.NON_PAST_NEG, Formality.PLAIN])
    results.append([plain_past_positive(dictionary_form, verb_class),
                    Form.PAST, Formality.PLAIN])
    results.append([plain_past_negative(dictionary_form, verb_class),
                    Form.PAST_NEG, Formality.PLAIN])

    # formality-constant
    results.append([te(dictionary_form, verb_class), Form.TE, None])

    return results

def get_godan_stem(dictionary_form: str, formality: Formality) -> str:
    """Get the stem of the provided godan verb

    Parmeters
    ---------
    dictionary_form : str
        Dictionary form of the godan verb for which the stem will be determined

    Returns
    -------
    str
        Stem from onto which (most) conjugations can be appended
    """

    if formality == Formality.POLITE:
        stem = dictionary_form[:-1] + godan_stem_mapping[dictionary_form[-1]]
    else:
        stem = dictionary_form[:-1] + godan_plain_stem_mapping[dictionary_form[-1]]
    return stem

def _masu_stem(dictionary_form: str, v_class: VerbClass,
               formality: Formality = Formality.POLITE) -> str:
    """Get the ~masu stem of the specified verb

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the verb for which the ~masu stem will be determined
    v_class : VerbClass
        Verb class of the requested verb
    formality : Formality
        Formality level of the requested stem

    Returns
    -------
    str
        ~masu stem onto which most conjugation endings can be appended
    """
    stem = None
    if v_class == VerbClass.ICHIDAN:
        stem = dictionary_form[:-1] # drop the る
    elif v_class == VerbClass.GODAN:
        stem = get_godan_stem(dictionary_form, formality)
    elif v_class == VerbClass.IRREGULAR:
        if dictionary_form.endswith('する'):
            stem = dictionary_form[:-2] + 'し'
        elif dictionary_form.endswith('来[く]る'):
            if formality == Formality.POLITE:
                stem = dictionary_form[:-5] + '来[き]'
            else:
                stem = dictionary_form[:-5] + '来[こ]'
    assert stem is not None
    return stem

def polite_nonpast_positive(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Polite Non-Past conjugation

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the verb to be conjugated
    verb_class : VerbClass
        Class of the verb being conjugated
    Returns
    -------
    str
        Conjugated verb
    """

    stem = _masu_stem(dictionary_form, verb_class)
    completion = stem + "ます"

    return completion

def polite_nonpast_negative(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Polite Non-Past Negative conjugation

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the verb to be conjugated
    verb_class : VerbClass
        Class of the verb being conjugated
    Returns
    -------
    str
        Conjugated verb
    """

    stem = _masu_stem(dictionary_form, verb_class)
    completion = stem + "ません"

    return completion

def polite_past_positive(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Polite Past conjugation

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the verb to be conjugated
    verb_class : VerbClass
        Class of the verb being conjugated
    Returns
    -------
    str
        Conjugated verb
    """

    stem = _masu_stem(dictionary_form, verb_class)
    completion = stem + "ました"

    return completion

def polite_past_negative(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Polite Past Negative conjugation

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the verb to be conjugated
    verb_class : VerbClass
        Class of the verb being conjugated
    Returns
    -------
    str
        Conjugated verb
    """

    stem = _masu_stem(dictionary_form, verb_class)
    completion = stem + "ませんでした"

    return completion

def polite_volitional(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Polite Volitional conjugation

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the verb to be conjugated
    verb_class : VerbClass
        Class of the verb being conjugated
    Returns
    -------
    str
        Conjugated verb
    """

    stem = _masu_stem(dictionary_form, verb_class)
    completion = stem + "ましょう"

    return completion

def te(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Te form conjugation

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the verb to be conjugated
    verb_class : VerbClass
        Class of the verb being conjugated
    Returns
    -------
    str
        Conjugated verb
    """
    completion = None
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
    assert completion is not None
    return completion

def plain_nonpast_positive(dictionary_form: str) -> str:
    """Get the Plain Non-Past conjugation

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the verb to be conjugated
    verb_class : VerbClass
        Class of the verb being conjugated
    Returns
    -------
    str
        Conjugated verb
    """

    return dictionary_form

def plain_nonpast_negative(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Plain Non-Past Negative conjugation

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the verb to be conjugated
    verb_class : VerbClass
        Class of the verb being conjugated
    Returns
    -------
    str
        Conjugated verb
    """

    if dictionary_form.endswith('ある'):
        return 'ない'

    stem = _masu_stem(dictionary_form, verb_class, formality=Formality.PLAIN)
    completion = stem + 'ない'
    return completion

def plain_past_positive(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Plain Past conjugation

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the verb to be conjugated
    verb_class : VerbClass
        Class of the verb being conjugated
    Returns
    -------
    str
        Conjugated verb
    """

    te_form = te(dictionary_form, verb_class)
    if te_form.endswith('て'):
        ending = 'た'
    else: # ends with で
        ending = 'だ'
    completion = te_form[:-1] + ending

    return completion

def plain_past_negative(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Plain Past Negative conjugation

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the verb to be conjugated
    verb_class : VerbClass
        Class of the verb being conjugated
    Returns
    -------
    str
        Conjugated verb
    """

    nai_form = plain_nonpast_negative(dictionary_form, verb_class)
    completion = nai_form[:-1] + 'かった'
    return completion
