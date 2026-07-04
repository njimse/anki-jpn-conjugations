"""Functions for determining causative form conjugations"""
from ..enums import AGyo, Dan, Gyo, VerbClass
from .plain import (
    plain_nonpast_negative,
    plain_past_positive,
    plain_past_negative
)
from .polite import (
    polite_nonpast_positive,
    polite_nonpast_negative,
    polite_past_positive,
    polite_past_negative
)
from .stems import kuru_reading_stem
from .te import te

def _causative_stem(dictionary_form: str, verb_class: VerbClass) -> str: # pylint: disable=R0912
    """Get the causative stem of the specified verb

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the verb for which the causative stem will be determined
    verb_class : VerbClass
        Verb class of the requested verb

    Returns
    -------
    str
        stem onto which causative conjugation endings can be appended
    """
    if dictionary_form.endswith('する'):
        stem = dictionary_form[:-2] + 'させ'
    elif dictionary_form.endswith('来[く]る'):
        stem = dictionary_form[:-5] + '来[こ]させ'
    elif dictionary_form.endswith('来る'):
        stem = kuru_reading_stem(dictionary_form, '来[こ]させ')
    elif dictionary_form.endswith('くる'):
        stem = dictionary_form[:-2] + 'こさせ'
    elif verb_class == VerbClass.ICHIDAN:
        stem = dictionary_form[:-1] + 'させ'
    else:
        ending_gyo = Gyo.identify(dictionary_form[-1])
        if ending_gyo == AGyo:
            causative_ending = 'わ'
        else:
            causative_ending = ending_gyo.dan(Dan.A)
        stem = dictionary_form[:-1] + causative_ending + 'せ'
    return stem

def polite_nonpast_positive_causative(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Polite Non-Past Causative conjugation

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
    plain_causative = plain_nonpast_positive_causative(dictionary_form, verb_class)
    completion = polite_nonpast_positive(plain_causative, VerbClass.ICHIDAN)

    return completion

def polite_nonpast_negative_causative(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Polite Non-Past Negative Causative conjugation

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

    plain_causative = plain_nonpast_positive_causative(dictionary_form, verb_class)
    completion = polite_nonpast_negative(plain_causative, VerbClass.ICHIDAN)

    return completion

def polite_past_positive_causative(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Polite Past Causative conjugation

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

    plain_causative = plain_nonpast_positive_causative(dictionary_form, verb_class)
    completion = polite_past_positive(plain_causative, VerbClass.ICHIDAN)

    return completion

def polite_past_negative_causative(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Polite Past Negative Causative conjugation

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

    plain_causative = plain_nonpast_positive_causative(dictionary_form, verb_class)
    completion = polite_past_negative(plain_causative, VerbClass.ICHIDAN)

    return completion

def te_causative(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Te Causative form conjugation

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

    plain_causative = plain_nonpast_positive_causative(dictionary_form, verb_class)
    completion = te(plain_causative, VerbClass.ICHIDAN)

    return completion

def plain_nonpast_positive_causative(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Plain Non-Past Causative conjugation

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

    stem = _causative_stem(dictionary_form, verb_class)
    completion = stem + "る"
    return completion

def plain_nonpast_negative_causative(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Plain Non-Past Negative Causative conjugation

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

    plain_causative = plain_nonpast_positive_causative(dictionary_form, verb_class)
    completion = plain_nonpast_negative(plain_causative, VerbClass.ICHIDAN)

    return completion

def plain_past_positive_causative(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Plain Past Causative conjugation

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

    plain_causative = plain_nonpast_positive_causative(dictionary_form, verb_class)
    completion = plain_past_positive(plain_causative, VerbClass.ICHIDAN)

    return completion

def plain_past_negative_causative(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Plain Past Negative Causative conjugation

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

    plain_causative = plain_nonpast_positive_causative(dictionary_form, verb_class)
    completion = plain_past_negative(plain_causative, VerbClass.ICHIDAN)

    return completion
