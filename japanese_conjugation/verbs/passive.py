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
from .te import te

def _passive_stem(dictionary_form: str) -> str: # pylint: disable=R0912
    """Get the passive stem of the specified verb

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the verb for which the ~masu stem will be determined
    v_class : VerbClass
        Verb class of the requested verb

    Returns
    -------
    str
        stem onto which passive conjugation endings can be appended
    """
    if dictionary_form.endswith('する'):
        stem = dictionary_form[:-2] + 'され'
    elif dictionary_form.endswith('来[く]る'):
        stem = dictionary_form[:-5] + '来[こ]られ'
    elif dictionary_form.endswith('来る'):
        if len(dictionary_form) == 2:
            buffer = ''
        else:
            buffer = ' '
        ending = '来[こ]られ'
        stem = dictionary_form[:-2] + buffer + ending
    elif dictionary_form.endswith('くる'):
        stem = dictionary_form[:-2] + 'こられ'
    else:
        ending_gyo = Gyo.identify(dictionary_form[-1])
        if ending_gyo == AGyo:
            passive_ending = 'わ'
        else:
            passive_ending = ending_gyo.dan(Dan.a)
        stem = dictionary_form[:-1] + passive_ending + 'れ'
    return stem

def polite_nonpast_positive_passive(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Polite Non-Past Passive conjugation

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
    plain_passive = plain_nonpast_positive_passive(dictionary_form, verb_class)
    completion = polite_nonpast_positive(plain_passive, VerbClass.ICHIDAN)

    return completion

def polite_nonpast_negative_passive(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Polite Non-Past Negative Passive conjugation

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

    plain_passive = plain_nonpast_positive_passive(dictionary_form, verb_class)
    completion = polite_nonpast_negative(plain_passive, VerbClass.ICHIDAN)

    return completion

def polite_past_positive_passive(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Polite Past Passive conjugation

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

    plain_passive = plain_nonpast_positive_passive(dictionary_form, verb_class)
    completion = polite_past_positive(plain_passive, VerbClass.ICHIDAN)

    return completion

def polite_past_negative_passive(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Polite Past Negative Passive conjugation

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

    plain_passive = plain_nonpast_positive_passive(dictionary_form, verb_class)
    completion = polite_past_negative(plain_passive, VerbClass.ICHIDAN)

    return completion

def te_passive(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Te Passive form conjugation

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

    plain_passive = plain_nonpast_positive_passive(dictionary_form, verb_class)
    completion = te(plain_passive, VerbClass.ICHIDAN)

    return completion

def plain_nonpast_positive_passive(dictionary_form: str, verb_class: VerbClass) -> str: # pylint: disable=W0613
    """Get the Plain Non-Past Passive conjugation

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the verb to be conjugated
    verb_class : VerbClass
        Class of the verb being conjugated. Note that it does not get used in this function,
        but we include it for API consistency with the other conjugation functions

    Returns
    -------
    str
        Conjugated verb
    """

    stem = _passive_stem(dictionary_form)
    completion = stem + "る"
    return completion

def plain_nonpast_negative_passive(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Plain Non-Past Negative Passive conjugation

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

    plain_passive = plain_nonpast_positive_passive(dictionary_form, verb_class)
    completion = plain_nonpast_negative(plain_passive, VerbClass.ICHIDAN)

    return completion

def plain_past_positive_passive(dictionary_form: str, verb_class: VerbClass) -> str: # pylint: disable=W0613
    """Get the Plain Non-Past Passive conjugation

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the verb to be conjugated
    verb_class : VerbClass
        Class of the verb being conjugated. Note that it does not get used in this function,
        but we include it for API consistency with the other conjugation functions

    Returns
    -------
    str
        Conjugated verb
    """

    plain_passive = plain_nonpast_positive_passive(dictionary_form, verb_class)
    completion = plain_past_positive(plain_passive, VerbClass.ICHIDAN)

    return completion

def plain_past_negative_passive(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Plain Past Negative Passive Passive conjugation

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

    plain_passive = plain_nonpast_positive_passive(dictionary_form, verb_class)
    completion = plain_past_negative(plain_passive, VerbClass.ICHIDAN)

    return completion
