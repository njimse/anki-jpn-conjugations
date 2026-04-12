"""Various enumerated objects for use throughout the rest of the module"""
from enum import Enum
from typing import Optional

class Form(Enum):
    """Enumeration of known conjugation forms
    
    Parameters
    ----------
    simple_name : str
        text to provide human-friendly description of the core aspect of the form
    polarity : str
        text describing the polarity of the form
    temparality : str
        text describing the temporal aspect of the form
    """
    NON_PAST = ('indicative', 'positive', 'non-past')
    NON_PAST_NEG = ('indicative', 'negative', 'non-past')
    PAST = ('indicative', 'positive', 'past')
    PAST_NEG = ('indicative', 'negative', 'past')
    TE = ('te', 'positive', '')
    VOLITIONAL = ('volitional', '', '')

    # tai forms
    TAI_NON_PAST = ('tai indicative', 'positive', 'non-past')
    TAI_NON_PAST_NEG = ('tai indicative', 'negative', 'non-past')
    TAI_PAST = ('tai indicative', 'positive', 'past')
    TAI_PAST_NEG = ('tai indicative', 'negative', 'past')
    TAI_TE = ('tai te', 'positive', '')

    # potential forms
    POTENTIAL_NON_PAST = ('potential indicative', 'positive', 'non-past')
    POTENTIAL_NON_PAST_NEG = ('potential indicative', 'negative', 'non-past')
    POTENTIAL_PAST = ('potential indicative', 'positive', 'past')
    POTENTIAL_PAST_NEG = ('potential indicative', 'negative', 'past')
    POTENTIAL_TE = ('potential te', 'positive', '')

    # passive forms
    PASSIVE_NON_PAST = ('passive indicative', 'positive', 'non-past')
    PASSIVE_NON_PAST_NEG = ('passive indicative', 'negative', 'non-past')
    PASSIVE_PAST = ('passive indicative', 'positive', 'past')
    PASSIVE_PAST_NEG = ('passive indicative', 'negative', 'past')
    PASSIVE_TE = ('passive te', 'positive', '')

    def __init__(self, simple_name: str, polarity: Optional[bool], temporality: str):
        self.simple_name = simple_name
        self.polarity = polarity
        self.temporality = temporality

    def label(self) -> str:
        """Compose the label for the form

        Returns
        -------
        str
            Label describing relevant attributes of the form
        """

        result = []
        if self.temporality:
            result.append(self.temporality)
        if 'indicative' not in self.simple_name:
            result.append(self.simple_name)
        elif self.simple_name != 'indicative':
            result.append(self.simple_name.replace('indicative', '').strip())
        if self.polarity == 'negative':
            result.append(self.polarity)
        return ' '.join(result)

    def to_tai(self):
        """Map to the tai-form equivalent of this form
        
        Returns
        -------
        Form
            The same form, just in the tai grouping"""

        if self == Form.NON_PAST:
            return Form.TAI_NON_PAST
        if self == Form.NON_PAST_NEG:
            return Form.TAI_NON_PAST_NEG
        if self == Form.PAST:
            return Form.TAI_PAST
        if self == Form.PAST_NEG:
            return Form.TAI_PAST_NEG
        if self == Form.TE:
            return Form.TAI_TE
        return self


class Formality(Enum):
    """Enumeration of known formality levels"""
    POLITE = 'polite'
    PLAIN = 'plain'

class VerbClass(Enum):
    """Enumeration of known verb types"""
    GODAN = 'godan'
    ICHIDAN = 'ichidan'
    IRREGULAR = 'irregular'
    GENERAL = 'general-verb'

class AdjectiveClass(Enum):
    """Enumeration of known adjective types"""
    NA = 'na-adjective'
    I = 'i-adjective'
    GENERAL = 'general-adjective'

class ModelType(Enum):
    """enumeration of model (a.k.a. Note) types"""
    VERB = 'verb'
    ADJECTIVE = 'adjective'

class Dan(Enum):
    a = "あ"
    i = "い"
    u = "う"
    e = "え"
    o = "お"

class Gyo(Enum):

    @staticmethod
    def identify(input_str: str):
        """Identify the correct Gyo and return the approprite subclass"""
        if len(input_str) != 1:
            raise ValueError("Gyo.identify() input must be a single character")
        
        if input_str in ("あいうえお"):
            return AGyo
        elif input_str in ("かきくけこ"):
            return KaGyo
        elif input_str in ("がぎぐげご"):
            return GaGyo
        elif input_str in ("さしすせそ"):
            return SaGyo
        elif input_str in ("ざじずぜぞ"):
            return ZaGyo
        elif input_str in ("たちつてと"):
            return TaGyo
        elif input_str in ("だぢづでど"):
            return DaGyo
        elif input_str in ("なにぬねの"):
            return NaGyo
        elif input_str in ("はひふへほ"):
            return HaGyo
        elif input_str in ("ばびぶべぼ"):
            return BaGyo
        elif input_str in ("ぱぴぷぺぽ"):
            return PaGyo
        elif input_str in ("まみむめも"):
            return MaGyo
        elif input_str in ("らりるれろ"):
            return RaGyo
    
    @classmethod
    def dan(cls, target: Dan):
        return getattr(cls, target.name).value

class AGyo(Gyo):
    a = "あ"
    i = "い"
    u = "う"
    e = "え"
    o = "お"

class KaGyo(Gyo):
    a = "か"
    i = "き"
    u = "く"
    e = "け"
    o = "こ"

class GaGyo(Gyo):
    a = "が"
    i = "ぎ"
    u = "ぐ"
    e = "げ"
    o = "ご"

class SaGyo(Gyo):
    a = "さ"
    i = "し"
    u = "す"
    e = "せ"
    o = "そ"

class ZaGyo(Gyo):
    a = "ざ"
    i = "じ"
    u = "ず"
    e = "ぜ"
    o = "ぞ"

class TaGyo(Gyo):
    a = "た"
    i = "ち"
    u = "つ"
    e = "て"
    o = "と"

class DaGyo(Gyo):
    a = "だ"
    i = "ぢ"
    u = "づ"
    e = "で"
    o = "ど"

class NaGyo(Gyo):
    a = "な"
    i = "に"
    u = "ぬ"
    e = "ね"
    o = "の"

class HaGyo(Gyo):
    a = "は"
    i = "ひ"
    u = "ふ"
    e = "へ"
    o = "ほ"

class BaGyo(Gyo):
    a = "ば"
    i = "び"
    u = "ぶ"
    e = "べ"
    o = "ぼ"

class PaGyo(Gyo):
    a = "ぱ"
    i = "ぴ"
    u = "ぷ"
    e = "ぺ"
    o = "ぽ"

class MaGyo(Gyo):
    a = "ま"
    i = "み"
    u = "む"
    e = "め"
    o = "も"

class RaGyo(Gyo):
    a = "ら"
    i = "り"
    u = "る"
    e = "れ"
    o = "ろ"
