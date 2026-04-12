from ..enums import Dan, Gyo, VerbClass
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

def _potential_stem(dictionary_form: str, v_class: VerbClass) -> str: # pylint: disable=R0912
    """Get the potential stem of the specified verb

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the verb for which the ~masu stem will be determined
    v_class : VerbClass
        Verb class of the requested verb

    Returns
    -------
    str
        stem onto which potential conjugation endings can be appended
    """
    stem = None
    if v_class == VerbClass.ICHIDAN:
        stem = dictionary_form[:-1] + 'られ'
    elif v_class == VerbClass.GODAN:
        ending_gyo = Gyo.identify(dictionary_form[-1])
        stem = dictionary_form[:-1] + ending_gyo.dan(Dan.e)
    elif v_class == VerbClass.IRREGULAR:
        if dictionary_form.endswith('する'):
            stem = dictionary_form[:-2] + 'でき'

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
        elif dictionary_form.endswith('しゃる') \
            or dictionary_form.endswith('なさる') \
            or dictionary_form.endswith('くださる') \
            or dictionary_form.endswith('下[くだ]さる') \
            or dictionary_form.endswith('下さる'):

            stem = dictionary_form[:-1] + 'れ'
    assert stem is not None
    stem = stem.replace('を', 'が')
    return stem

def polite_nonpast_positive_potential(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Polite Non-Past Potential conjugation

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
    plain_potential = plain_nonpast_positive_potential(dictionary_form, verb_class)
    completion = polite_nonpast_positive(plain_potential, VerbClass.ICHIDAN)

    return completion

def polite_nonpast_negative_potential(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Polite Non-Past Negative Potential conjugation

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

    plain_potential = plain_nonpast_positive_potential(dictionary_form, verb_class)
    completion = polite_nonpast_negative(plain_potential, VerbClass.ICHIDAN)

    return completion

def polite_past_positive_potential(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Polite Past Potential conjugation

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

    plain_potential = plain_nonpast_positive_potential(dictionary_form, verb_class)
    completion = polite_past_positive(plain_potential, VerbClass.ICHIDAN)

    return completion

def polite_past_negative_potential(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Polite Past Negative Potential conjugation

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

    plain_potential = plain_nonpast_positive_potential(dictionary_form, verb_class)
    completion = polite_past_negative(plain_potential, VerbClass.ICHIDAN)

    return completion

def te_potential(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Te Potential form conjugation

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

    plain_potential = plain_nonpast_positive_potential(dictionary_form, verb_class)
    completion = te(plain_potential, VerbClass.ICHIDAN)

    return completion

def plain_nonpast_positive_potential(dictionary_form: str, verb_class: VerbClass) -> str: # pylint: disable=W0613
    """Get the Plain Non-Past Potential conjugation

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

    stem = _potential_stem(dictionary_form, verb_class)
    completion = stem + "る"
    return completion

def plain_nonpast_negative_potential(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Plain Non-Past Negative Potential conjugation

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

    plain_potential = plain_nonpast_positive_potential(dictionary_form, verb_class)
    completion = plain_nonpast_negative(plain_potential, VerbClass.ICHIDAN)

    return completion

def plain_past_positive_potential(dictionary_form: str, verb_class: VerbClass) -> str: # pylint: disable=W0613
    """Get the Plain Non-Past Potential conjugation

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

    plain_potential = plain_nonpast_positive_potential(dictionary_form, verb_class)
    completion = plain_past_positive(plain_potential, VerbClass.ICHIDAN)

    return completion

def plain_past_negative_potential(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Plain Past Negative Potential Potential conjugation

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

    plain_potential = plain_nonpast_positive_potential(dictionary_form, verb_class)
    completion = plain_past_negative(plain_potential, VerbClass.ICHIDAN)

    return completion
