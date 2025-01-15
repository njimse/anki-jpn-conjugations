"""Methods pertaining to the conjugation of verbs"""
from typing import Optional, List, Tuple

from anki_jpn.enums import Form, Formality, VerbClass
from anki_jpn.util import (
    remove_furigana,
    promote_furigana
)

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
ICHIDAN_ENDINGS = set([
    "いる",
    "える",
    "きる", "ぎる",
    "ける", "げる",
    "しる", "じる",
    "せる", "ぜる",
    "ちる",
    "てる", "でる",
    "ひる", "びる", "ぴる",
    "へる", "べる", "ぺる",
    "みる",
    "める",
    "にる",
    "ねる",
    "りる",
    "れる"
])

# Except where otherwise noted with an asterisk, -iru and -eru exceptions obtained from:
# https://www.sljfaq.org/afaq/which-godan.html
# This content is covered by a Creative Commons Attribution-ShareAlike Licence (V4.0)
iru_exceptions = [
    '油ぎる', '脂ぎる', 'あぶらぎる',
    'びびる',
    '打っ千切る', 'ぶっちぎる', # *
    '千切る', 'ちぎる',
    '契る', 'ちぎる', # *
    '散る', 'ちる',
    'どじる',
    '愚痴る', 'ぐちる',
    '引きちぎる', '引き千切る', 'ひきちぎる', # *
    '入る', 'はいる',
    '走る', 'はしる',
    '穿る', # This has an ichidan homophone, therefore hiragana not included
    '褒めちぎる', '誉めちぎる', 'ほめちぎる', # *
    '迸る', 'ほとばしる',
    'いびる',
    '弄る', 'いじる',
    # いる homophones -- Because the animate exist verb いる is so common (and is an ichidan verb),
    # we do not include the hiragana in the expections and require the kanji input
    '熬る',
    '炒る',
    '煎る',
    '要る',
    '煎る',
    '炒る',
    '熬る',
    ## end いる homophones
    '限る', 'かぎる',
    '噛る', 'かじる',
    '嚙み千切る', 'かみちぎる', # *
    '食いちぎる', '食千切る', 'くいちぎる', # *
    '切る', # Due to the common ichidan homophone 着る[きる], do not include the hiragana here
    '軋る', '轢る', '輾る', 'きしる',
    '抉じる', 'こじる',
    '参る', 'まいる',
    '混じる', 'まじる',
    '滅入る', 'めいる',
    '漲る', 'みなぎる',
    '毟る', '挘る', 'むしる',
    '詰る', 'なじる',
    'ねじる',
    '握る', 'にぎる',
    '罵る', 'ののしる',
    '陥る', 'おちいる',
    'せびる',
    '知る', 'しる',
    '謗る', '譏る', '誹る', 'そしる',
    '滾る', '激る', 'たぎる',
    '魂消る', 'たまぎる',
    'やじる',
    '攀じる', # This has an ichidan homophone, therefore hiragana not included
]
eru_exceptions = [
    '焦る', # Due to ichidan homophones, do not include hiragana
    '老ける', # Due to ichidan homophones, do not include hiragana
    '減る', # ichidan homophones
    '捻る', '撚る', # ichidan homophones
    '火照る', 'ほてる',
    '帰る', # ichidan homophones
    '陰る', 'かげる',
    '翔る', # ichidan homophones
    '蹴る', 'ける',
    'くねる',
    '覆る', 'くつがえる',
    '舐める', '嘗める', '甞める', 'なめる',
    '練る', '煉る', # ichidan homophones
    '滑る', 'ぬめる',
    '阿る', '阿ねる', 'おもねる',
    '競る', '糶る', 'せる',
    '迫る','せまる', #*
    '押し迫る', 'おしせまる', #*
    '追い迫る', 'おいせまる', #*
    '差し迫る', 'さしせまる', #*
    '鬼気迫る', 'ききせまる', #*
    '真に迫る', 'しんにせまる', #*
    '旦夕に迫る', 'たんせきにせまる', #*
    '真実に迫る', 'しんじつにせまる', #*
    '辞職を迫る', 'じしょくをせまる', #*
    '万感胸に迫る', 'ばんかんむねにせまる', #*
    '命旦夕に迫る', 'めいたんせきにせまる', #*
    '挵る', 'せせる',
    '喋る', 'しゃべる',
    '茂る', '繁る', '滋る', 'しげる',
    '湿気る', # ichidan homophones
    '滑る', # ichidan homophones
    '猛る', '哮る', # ichidan homophones
    '照る', 'てる',
    '詰める', 'つめる',
    '抓る', 'つねる',
    '畝る', 'うねる',
    '蘇る', '甦る', 'よみがえる'
]
ICHIDAN_EXCEPTIONS = iru_exceptions + eru_exceptions

def generate_verb_forms(dictionary_form: str, verb_class: VerbClass)\
    -> List[Tuple[str, Form, Optional[Formality]]]:
    """Generate the known conjugations for the provided verb

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the verb to be conjugated
    verb_class : VerbClass
        Class of verb to guide how conjugation should be performed

    Returns
    -------
    List of tuples
        Each tuple is the conjugation (string), Form, and Formality. Note that for the Te form,
        the formality will be provided as None
    """
    if not any(dictionary_form.endswith(ending) for ending in GODAN_STEM_ENDINGS):
        # If this doesn't look like a verb, don't try to conjugate it
        return []

    if verb_class == VerbClass.GENERAL:
        verb_class = classify_verb(dictionary_form)

    results = []
    all_forms = [
        [polite_nonpast_positive, Form.NON_PAST, Formality.POLITE],
        [polite_nonpast_negative, Form.NON_PAST_NEG, Formality.POLITE],
        [polite_past_positive, Form.PAST, Formality.POLITE],
        [polite_past_negative, Form.PAST_NEG, Formality.POLITE],
        [polite_volitional, Form.VOLITIONAL, Formality.POLITE],

        # Plain forms
        [plain_nonpast_positive, Form.NON_PAST, Formality.PLAIN],
        [plain_nonpast_negative, Form.NON_PAST_NEG, Formality.PLAIN],
        [plain_past_positive, Form.PAST, Formality.PLAIN],
        [plain_past_negative, Form.PAST_NEG, Formality.PLAIN],

        # formality-constant
        [te, Form.TE, None]
    ]

    for conjugate, form, formality in all_forms:
        try:
            results.append([conjugate(dictionary_form, verb_class), form, formality])
        except: # pylint: disable=W0702
            pass

    return results

def classify_verb(dictionary_form: str) -> VerbClass:
    """Classify a verb as one of ichidan, godan, or irregular type
    
    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the verb to be classified
        
    Returns
    -------
    VerbClass
        Returns the verb classification"""

    shaved_dictionary_form = remove_furigana(dictionary_form)
    kana_only = promote_furigana(dictionary_form)

    if any(shaved_dictionary_form.endswith(ending) for ending in ["する", "くる", "来る"]):
        return VerbClass.IRREGULAR

    if any(kana_only.endswith(ending) for ending in ICHIDAN_ENDINGS) \
        and shaved_dictionary_form not in ICHIDAN_EXCEPTIONS:

        return VerbClass.ICHIDAN

    return VerbClass.GODAN

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

def plain_nonpast_positive(dictionary_form: str, verb_type: VerbClass) -> str: # pylint: disable=W0613
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
