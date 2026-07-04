"""Methods pertaining to the conjugation of verbs"""
from typing import Optional, List, Tuple

from ..enums import Dan, Form, Formality, Gyo, VerbClass, AdjectiveClass
from ..util import (
    remove_furigana,
    promote_furigana
)
from ..adjectives import generate_adjective_forms

from .stems import masu_stem

from .plain import (
    plain_nonpast_positive,
    plain_nonpast_negative,
    plain_past_positive,
    plain_past_negative,
    plain_volitional
)
from .polite import (
    polite_nonpast_positive,
    polite_nonpast_negative,
    polite_past_positive,
    polite_past_negative,
    polite_volitional
)
from .passive import (
    polite_nonpast_positive_passive,
    polite_nonpast_negative_passive,
    polite_past_positive_passive,
    polite_past_negative_passive,
    te_passive,
    plain_nonpast_positive_passive,
    plain_nonpast_negative_passive,
    plain_past_positive_passive,
    plain_past_negative_passive,
)
from .potential import (
    polite_nonpast_positive_potential,
    polite_nonpast_negative_potential,
    polite_past_positive_potential,
    polite_past_negative_potential,
    te_potential,
    plain_nonpast_positive_potential,
    plain_nonpast_negative_potential,
    plain_past_positive_potential,
    plain_past_negative_potential,
)
from .causative import (
    polite_nonpast_positive_causative,
    polite_nonpast_negative_causative,
    polite_past_positive_causative,
    polite_past_negative_causative,
    te_causative,
    plain_nonpast_positive_causative,
    plain_nonpast_negative_causative,
    plain_past_positive_causative,
    plain_past_negative_causative,
)
from .te import te

GODAN_STEM_ENDINGS = set(["う", "く", "す", "つ", "ぬ", "ふ", "む", "る", "ぐ", "ず", "ぶ", "ぷ"])

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
    '返る', # ichidan homophones
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

    if dictionary_form == "です":
        results = [
            ['です', Form.NON_PAST, Formality.POLITE],
            ['じゃないです', Form.NON_PAST_NEG, Formality.POLITE],
            ['でした', Form.PAST, Formality.POLITE],
            ['ませんでした', Form.PAST_NEG, Formality.POLITE],
            ['でしょう', Form.VOLITIONAL, Formality.POLITE],
            ['だ', Form.NON_PAST, Formality.PLAIN],
            ['じゃない', Form.NON_PAST_NEG, Formality.PLAIN],
            ['だった', Form.PAST, Formality.PLAIN],
            ['なかった', Form.PAST_NEG, Formality.PLAIN],
            ['だろう', Form.VOLITIONAL, Formality.PLAIN],
            ['で', Form.TE, None],
        ]
        return results

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
        [plain_volitional, Form.VOLITIONAL, Formality.PLAIN],

        # formality-constant
        [te, Form.TE, None],

        # Polite Potential
        [polite_nonpast_positive_potential, Form.POTENTIAL_NON_PAST, Formality.POLITE],
        [polite_nonpast_negative_potential, Form.POTENTIAL_NON_PAST_NEG, Formality.POLITE],
        [polite_past_positive_potential, Form.POTENTIAL_PAST, Formality.POLITE],
        [polite_past_negative_potential, Form.POTENTIAL_PAST_NEG, Formality.POLITE],

        # Plain Potential
        [plain_nonpast_positive_potential, Form.POTENTIAL_NON_PAST, Formality.PLAIN],
        [plain_nonpast_negative_potential, Form.POTENTIAL_NON_PAST_NEG, Formality.PLAIN],
        [plain_past_positive_potential, Form.POTENTIAL_PAST, Formality.PLAIN],
        [plain_past_negative_potential, Form.POTENTIAL_PAST_NEG, Formality.PLAIN],

        # formality-constant
        [te_potential, Form.POTENTIAL_TE, None],

        # Polite Passive
        [polite_nonpast_positive_passive, Form.PASSIVE_NON_PAST, Formality.POLITE],
        [polite_nonpast_negative_passive, Form.PASSIVE_NON_PAST_NEG, Formality.POLITE],
        [polite_past_positive_passive, Form.PASSIVE_PAST, Formality.POLITE],
        [polite_past_negative_passive, Form.PASSIVE_PAST_NEG, Formality.POLITE],

        # Plain Passive
        [plain_nonpast_positive_passive, Form.PASSIVE_NON_PAST, Formality.PLAIN],
        [plain_nonpast_negative_passive, Form.PASSIVE_NON_PAST_NEG, Formality.PLAIN],
        [plain_past_positive_passive, Form.PASSIVE_PAST, Formality.PLAIN],
        [plain_past_negative_passive, Form.PASSIVE_PAST_NEG, Formality.PLAIN],

        # formality-constant
        [te_passive, Form.PASSIVE_TE, None],

        # Polite Causative
        [polite_nonpast_positive_causative, Form.CAUSATIVE_NON_PAST, Formality.POLITE],
        [polite_nonpast_negative_causative, Form.CAUSATIVE_NON_PAST_NEG, Formality.POLITE],
        [polite_past_positive_causative, Form.CAUSATIVE_PAST, Formality.POLITE],
        [polite_past_negative_causative, Form.CAUSATIVE_PAST_NEG, Formality.POLITE],

        # Plain Causative
        [plain_nonpast_positive_causative, Form.CAUSATIVE_NON_PAST, Formality.PLAIN],
        [plain_nonpast_negative_causative, Form.CAUSATIVE_NON_PAST_NEG, Formality.PLAIN],
        [plain_past_positive_causative, Form.CAUSATIVE_PAST, Formality.PLAIN],
        [plain_past_negative_causative, Form.CAUSATIVE_PAST_NEG, Formality.PLAIN],

        # formality-constant
        [te_causative, Form.CAUSATIVE_TE, None]
    ]

    for conjugate, form, formality in all_forms:
        try:
            results.append([conjugate(dictionary_form, verb_class), form, formality])
        except: # pylint: disable=W0702
            pass

    results.extend(tai_forms(dictionary_form, verb_class))

    return results

def _looks_like_ichidan(dictionary_form: str) -> bool:
    """Classify as looking like an ichidan verb or not

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the verb to be classified

    Returns
    -------
    bool
        True if verb looks like an ichidan. False otherwise."""
    if dictionary_form[-1] == 'る':
        penultimate_char = dictionary_form[-2]
        penultimate_gyo = Gyo.identify(penultimate_char)
        if penultimate_gyo is None:
            return False
        if penultimate_char in (penultimate_gyo.dan(Dan.I), penultimate_gyo.dan(Dan.E)):
            return True

    return False

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


    if any(shaved_dictionary_form.endswith(ending) for ending in \
           ["する", "くる", "来る", "しゃる", "なさる", "下さる"]) \
        or kana_only in ["なさる", "くださる"]:
        return VerbClass.IRREGULAR
    if _looks_like_ichidan(kana_only) and shaved_dictionary_form not in ICHIDAN_EXCEPTIONS:

        return VerbClass.ICHIDAN

    return VerbClass.GODAN

def tai_forms(dictionary_form: str, verb_class: VerbClass) \
    -> List[Tuple[str, Form, Optional[Formality]]]:
    """Generate the -tai form conjugations for a verb

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the verb to be conjugated
    verb_class : VerbClass

    Returns
    -------
    List[Tuple[str, Form, Optional[Formality]]]
        The known i-adjective conjugations for the input verb
    """

    tai_dictionary_form = masu_stem(dictionary_form, verb_class) + 'たい'
    tai_conjugations = []
    for conjugation, form, formality in \
        generate_adjective_forms(tai_dictionary_form, AdjectiveClass.I):

        tai_conjugations.append([conjugation, form.to_tai(), formality])

    return tai_conjugations
