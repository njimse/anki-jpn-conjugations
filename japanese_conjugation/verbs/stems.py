"""Functions for getting stems used for subsequent conjugations"""
from ..enums import AGyo, Dan, Formality, Gyo, VerbClass

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
    ending_gyo = Gyo.identify(dictionary_form[-1])
    if formality == Formality.POLITE:
        stem = dictionary_form[:-1] + ending_gyo.dan(Dan.I)
    else:
        if ending_gyo == AGyo:
            ending = "わ"
        else:
            ending = ending_gyo.dan(Dan.A)
        stem = dictionary_form[:-1] + ending
    return stem

def looks_like_honorific(dictionary_form: str) -> bool:
    """Determine if the provided dictionary form appears to be an honorific verb
    
        Parmeters
    ---------
    dictionary_form : str
        Dictionary form of the godan verb for which the stem will be determined

    Returns
    -------
    bool
        True if dictionary form appears to be honorific, False otherwise"""
    if dictionary_form.endswith('しゃる') \
        or dictionary_form.endswith('なさる') \
        or dictionary_form.endswith('くださる') \
        or dictionary_form.endswith('下[くだ]さる') \
        or dictionary_form.endswith('下さる'):

        return True
    return False

def masu_stem(dictionary_form: str, v_class: VerbClass, # pylint: disable=R0912
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
        ~masu stem onto which many/most conjugation endings can be appended
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
        elif dictionary_form.endswith('来る'):
            if len(dictionary_form) == 2:
                buffer = ''
            else:
                buffer = ' '
            if formality == Formality.POLITE:
                ending = '来[き]'
            else:
                ending = '来[こ]'
            stem = dictionary_form[:-2] + buffer + ending
        elif dictionary_form.endswith('くる'):
            if formality == Formality.POLITE:
                stem = dictionary_form[:-2] + 'き'
            else:
                stem = dictionary_form[:-2] + 'こ'
        elif looks_like_honorific(dictionary_form):
            stem = dictionary_form[:-1] + 'い'

    assert stem is not None
    return stem
