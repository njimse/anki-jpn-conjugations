"""Methods pertaining to the conjugation of adjectives
"""
from typing import List, Tuple, Optional
from anki_jpn.enums import AdjectiveClass, Form, Formality
from anki_jpn.util import (
    promote_furigana
)

def generate_adjective_forms(dictionary_form: str, adjective_class: AdjectiveClass)\
              -> List[Tuple[str, Form, Optional[Formality]]]:
    """Generate the known conjugations for the provided adjective

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the adjective to be conjugated
    adjective_class : AdjectiveClass
        Class of adjective to guide how conjugation should be performed

    Returns
    -------
    List of tuples
        Each tuple is the conjugation (string), Form, and Formality. Note that for the Te form,
        the formality will be provided as None
    """

    if adjective_class == AdjectiveClass.GENERAL:
        adjective_class = classify_adjective(dictionary_form)

    if adjective_class == AdjectiveClass.NA and not dictionary_form.endswith("な"):
        dictionary_form = dictionary_form + "な"

    results = []
    # Polite forms
    results.append([polite_nonpast_positive(dictionary_form, adjective_class),
                    Form.NON_PAST, Formality.POLITE])
    results.append([polite_nonpast_negative(dictionary_form, adjective_class),
                    Form.NON_PAST_NEG, Formality.POLITE])
    results.append([polite_past_positive(dictionary_form, adjective_class),
                    Form.PAST, Formality.POLITE])
    results.append([polite_past_negative(dictionary_form, adjective_class),
                    Form.PAST_NEG, Formality.POLITE])

    # Plain forms
    results.append([plain_nonpast_positive(dictionary_form, adjective_class),
                    Form.NON_PAST, Formality.PLAIN])
    results.append([plain_nonpast_negative(dictionary_form, adjective_class),
                    Form.NON_PAST_NEG, Formality.PLAIN])
    results.append([plain_past_positive(dictionary_form, adjective_class),
                    Form.PAST, Formality.PLAIN])
    results.append([plain_past_negative(dictionary_form, adjective_class),
                    Form.PAST_NEG, Formality.PLAIN])

    # formality-constant
    results.append([te(dictionary_form, adjective_class), Form.TE, None])

    return results

def classify_adjective(dictionary_form: str) -> AdjectiveClass:
    """Classify an adjective as either an i-adjective or na-adjective
    
    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the adjective to be classified
        
    Returns
    -------
    AdjectiveClass
        Returns the adjective classification"""

    kana_only = promote_furigana(dictionary_form)
    if dictionary_form.endswith('い') and kana_only not in ['きれい', 'きらい', 'さいわい']:
        return AdjectiveClass.I

    return AdjectiveClass.NA

def get_stem(dictionary_form: str) -> str:
    """Get the stem of the provided adjective

    Parmeters
    ---------
    dictionary_form : str
        Dictionary form of the adjective for which the stem will be determined

    Returns
    -------
    str
        Stem from onto which (most) conjugations can be appended
    """

    if dictionary_form.endswith('いい'):
        stem = dictionary_form[:-2] + 'よ'
    else:
        stem = dictionary_form[:-1]
    return stem

def polite_nonpast_positive(dictionary_form: str, adj_class: AdjectiveClass) -> str:
    """Get the Polite Non-Past conjugation

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the adjective to be conjugated
    adj_class : AdjectiveClass
        Class of the adjective being conjugated
    Returns
    -------
    str
        Conjugated adjective
    """

    if adj_class == AdjectiveClass.NA:
        ending = 'です'
        completion = dictionary_form[:-1] + ending
    else:
        ending = 'です'
        completion = dictionary_form + ending
    return completion

def polite_nonpast_negative(dictionary_form: str, adj_class: AdjectiveClass) -> str:
    """Get the Polite Non-Past Negative conjugation

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the adjective to be conjugated
    adj_class : AdjectiveClass
        Class of the adjective being conjugated
    Returns
    -------
    str
        Conjugated adjective
    """

    stem = get_stem(dictionary_form)
    if adj_class == AdjectiveClass.NA:
        ending = 'じゃないです'
    else:
        ending = 'くないです'
    completion = stem + ending
    return completion

def polite_past_positive(dictionary_form: str, adj_class: AdjectiveClass) -> str:
    """Get the Polite Past conjugation

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the adjective to be conjugated
    adj_class : AdjectiveClass
        Class of the adjective being conjugated
    Returns
    -------
    str
        Conjugated adjective
    """

    stem = get_stem(dictionary_form)
    if adj_class == AdjectiveClass.NA:
        ending = 'でした'
    else:
        ending = 'かったです'
    completion = stem + ending
    return completion

def polite_past_negative(dictionary_form: str, adj_class: AdjectiveClass) -> str:
    """Get the Polite Past Negative conjugation

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the adjective to be conjugated
    adj_class : AdjectiveClass
        Class of the adjective being conjugated
    Returns
    -------
    str
        Conjugated adjective
    """

    stem = get_stem(dictionary_form)
    if adj_class == AdjectiveClass.NA:
        ending = 'じゃなかったです'
    else:
        ending = 'くなかったです'
    completion = stem + ending
    return completion

def te(dictionary_form: str, adj_class: AdjectiveClass) -> str:
    """Get the Te-form conjugation

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the adjective to be conjugated
    adj_class : AdjectiveClass
        Class of the adjective being conjugated
    Returns
    -------
    str
        Conjugated adjective
    """

    stem = get_stem(dictionary_form)
    if adj_class == AdjectiveClass.NA:
        ending = 'で'
    else:
        ending = 'くて'
    completion = stem + ending
    return completion

def plain_nonpast_positive(dictionary_form: str, adj_class: AdjectiveClass) -> str:
    """Get the Plain Non-Past conjugation

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the adjective to be conjugated
    adj_class : AdjectiveClass
        Class of the adjective being conjugated
    Returns
    -------
    str
        Conjugated adjective
    """

    stem = dictionary_form[:-1]
    if adj_class == AdjectiveClass.NA:
        ending = 'だ'
    else:
        ending = 'い'
    completion = stem + ending
    return completion

def plain_nonpast_negative(dictionary_form: str, adj_class: AdjectiveClass) -> str:
    """Get the Plain Non-Past Negative conjugation

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the adjective to be conjugated
    adj_class : AdjectiveClass
        Class of the adjective being conjugated
    Returns
    -------
    str
        Conjugated adjective
    """

    stem = get_stem(dictionary_form)
    if adj_class == AdjectiveClass.NA:
        ending = 'じゃない'
    else:
        ending = 'くない'
    completion = stem + ending
    return completion

def plain_past_positive(dictionary_form: str, adj_class: AdjectiveClass) -> str:
    """Get the Plain Past conjugation

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the adjective to be conjugated
    adj_class : AdjectiveClass
        Class of the adjective being conjugated
    Returns
    -------
    str
        Conjugated adjective
    """

    stem = get_stem(dictionary_form)
    if adj_class == AdjectiveClass.NA:
        ending = 'だった'
    else:
        ending = 'かった'
    completion = stem + ending
    return completion

def plain_past_negative(dictionary_form: str, adj_class: AdjectiveClass) -> str:
    """Get the Plain Past Negative conjugation

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the adjective to be conjugated
    adj_class : AdjectiveClass
        Class of the adjective being conjugated
    Returns
    -------
    str
        Conjugated adjective
    """

    stem = get_stem(dictionary_form)
    if adj_class == AdjectiveClass.NA:
        ending = 'じゃなかった'
    else:
        ending = 'くなかった'
    completion = stem + ending
    return completion
