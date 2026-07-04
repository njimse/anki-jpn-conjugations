"""Functions for determining causative-passive form conjugations"""
from ..enums import VerbClass
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
from .stems import godan_a_stem, kuru_reading_stem
from .te import te

def _causative_passive_stem(dictionary_form: str, verb_class: VerbClass) -> str: # pylint: disable=R0912
    """Get the causative-passive stem of the specified verb

    Following the presentation in Genki II lesson 23, godan verbs whose stem does
    not end in す use the contracted ~される form, while ichidan verbs, godan
    verbs ending in す, and the irregular verbs use the full ~させられる form.

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the verb for which the causative-passive stem will be
        determined
    verb_class : VerbClass
        Verb class of the requested verb

    Returns
    -------
    str
        stem onto which causative-passive conjugation endings can be appended
    """
    if dictionary_form.endswith('する'):
        stem = dictionary_form[:-2] + 'させられ'
    elif dictionary_form.endswith('来[く]る'):
        stem = dictionary_form[:-5] + '来[こ]させられ'
    elif dictionary_form.endswith('来る'):
        stem = kuru_reading_stem(dictionary_form, '来[こ]させられ')
    elif dictionary_form.endswith('くる'):
        stem = dictionary_form[:-2] + 'こさせられ'
    elif verb_class == VerbClass.ICHIDAN:
        stem = dictionary_form[:-1] + 'させられ'
    elif dictionary_form.endswith('す'):
        # godan verbs ending in す keep the uncontracted ~させられ form
        stem = dictionary_form[:-1] + 'させられ'
    else:
        # other godan verbs use the contracted ~され form
        stem = godan_a_stem(dictionary_form) + 'され'
    return stem

def polite_nonpast_positive_causative_passive(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Polite Non-Past Causative-Passive conjugation

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
    plain_causative_passive = plain_nonpast_positive_causative_passive(dictionary_form, verb_class)
    completion = polite_nonpast_positive(plain_causative_passive, VerbClass.ICHIDAN)

    return completion

def polite_nonpast_negative_causative_passive(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Polite Non-Past Negative Causative-Passive conjugation

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

    plain_causative_passive = plain_nonpast_positive_causative_passive(dictionary_form, verb_class)
    completion = polite_nonpast_negative(plain_causative_passive, VerbClass.ICHIDAN)

    return completion

def polite_past_positive_causative_passive(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Polite Past Causative-Passive conjugation

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

    plain_causative_passive = plain_nonpast_positive_causative_passive(dictionary_form, verb_class)
    completion = polite_past_positive(plain_causative_passive, VerbClass.ICHIDAN)

    return completion

def polite_past_negative_causative_passive(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Polite Past Negative Causative-Passive conjugation

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

    plain_causative_passive = plain_nonpast_positive_causative_passive(dictionary_form, verb_class)
    completion = polite_past_negative(plain_causative_passive, VerbClass.ICHIDAN)

    return completion

def te_causative_passive(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Te Causative-Passive form conjugation

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

    plain_causative_passive = plain_nonpast_positive_causative_passive(dictionary_form, verb_class)
    completion = te(plain_causative_passive, VerbClass.ICHIDAN)

    return completion

def plain_nonpast_positive_causative_passive(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Plain Non-Past Causative-Passive conjugation

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

    stem = _causative_passive_stem(dictionary_form, verb_class)
    completion = stem + "る"
    return completion

def plain_nonpast_negative_causative_passive(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Plain Non-Past Negative Causative-Passive conjugation

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

    plain_causative_passive = plain_nonpast_positive_causative_passive(dictionary_form, verb_class)
    completion = plain_nonpast_negative(plain_causative_passive, VerbClass.ICHIDAN)

    return completion

def plain_past_positive_causative_passive(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Plain Past Causative-Passive conjugation

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

    plain_causative_passive = plain_nonpast_positive_causative_passive(dictionary_form, verb_class)
    completion = plain_past_positive(plain_causative_passive, VerbClass.ICHIDAN)

    return completion

def plain_past_negative_causative_passive(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Plain Past Negative Causative-Passive conjugation

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

    plain_causative_passive = plain_nonpast_positive_causative_passive(dictionary_form, verb_class)
    completion = plain_past_negative(plain_causative_passive, VerbClass.ICHIDAN)

    return completion
