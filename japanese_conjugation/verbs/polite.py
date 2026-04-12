from ..enums import VerbClass
from .stems import masu_stem


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

    stem = masu_stem(dictionary_form, verb_class)
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

    stem = masu_stem(dictionary_form, verb_class)
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

    stem = masu_stem(dictionary_form, verb_class)
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

    stem = masu_stem(dictionary_form, verb_class)
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

    stem = masu_stem(dictionary_form, verb_class)
    completion = stem + "ましょう"

    return completion
