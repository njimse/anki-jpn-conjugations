from ..enums import AGyo, Dan, Formality, Gyo, VerbClass
from .stems import masu_stem
from .te import te

def plain_nonpast_positive(dictionary_form: str, verb_class: VerbClass) -> str: # pylint: disable=W0613
    """Get the Plain Non-Past conjugation

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
    if dictionary_form.endswith("来る"):
        ending = "来[く]る"
        if len(dictionary_form) == 2:
            completion = ending
        else:
            completion = dictionary_form[:-2] + ' ' + ending
        return completion

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
        return dictionary_form[:-2] + 'ない'

    if dictionary_form.endswith('しゃる') \
        or dictionary_form.endswith('なさる') \
        or dictionary_form.endswith('くださる') \
        or dictionary_form.endswith('下[くだ]さる') \
        or dictionary_form.endswith('下さる'):

        stem = dictionary_form[:-1] + 'ら'
    else:
        stem = masu_stem(dictionary_form, verb_class, formality=Formality.PLAIN)
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

def plain_volitional(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Plain Volitional conjugation

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
        completion = dictionary_form[:-1] + 'よう'
    elif verb_class == VerbClass.GODAN:
        ending_gyo = Gyo.identify(dictionary_form[-1])
        completion = dictionary_form[:-1] + ending_gyo.dan(Dan.o) + 'う'
    elif verb_class == VerbClass.IRREGULAR:
        if dictionary_form.endswith('する'):
            completion = dictionary_form[:-2] + 'しよう'

        elif dictionary_form.endswith('来[く]る'):
            completion = dictionary_form[:-5] + '来[こ]よう'
        elif dictionary_form.endswith('来る'):
            if len(dictionary_form) == 2:
                buffer = ''
            else:
                buffer = ' '
            ending = '来[こ]よう'
            completion = dictionary_form[:-2] + buffer + ending
        elif dictionary_form.endswith('くる'):
            completion = dictionary_form[:-2] + 'こよう'
        elif dictionary_form.endswith('しゃる') \
            or dictionary_form.endswith('なさる') \
            or dictionary_form.endswith('くださる') \
            or dictionary_form.endswith('下[くだ]さる') \
            or dictionary_form.endswith('下さる'):

            completion = dictionary_form[:-1] + 'ろう'
    assert completion is not None
    return completion