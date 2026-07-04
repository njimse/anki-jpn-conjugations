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

    # causative forms
    CAUSATIVE_NON_PAST = ('causative indicative', 'positive', 'non-past')
    CAUSATIVE_NON_PAST_NEG = ('causative indicative', 'negative', 'non-past')
    CAUSATIVE_PAST = ('causative indicative', 'positive', 'past')
    CAUSATIVE_PAST_NEG = ('causative indicative', 'negative', 'past')
    CAUSATIVE_TE = ('causative te', 'positive', '')

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
    """Enum for the dan (vowel) columns of a gyojuon table"""
    A = "あ"
    I = "い"
    U = "う"
    E = "え"
    O = "お"

class Gyo(Enum):
    """Base enum class for gyo rows of a gyojuon table"""

    @staticmethod
    def identify(input_str: str): # pylint: disable=R0912
        """Identify the correct Gyo and return the approprite subclass"""
        if len(input_str) != 1:
            raise ValueError("Gyo.identify() input must be a single character")

        return_value = None
        if input_str in ("あいうえお"):
            return_value = AGyo
        elif input_str in ("かきくけこ"):
            return_value = KaGyo
        elif input_str in ("がぎぐげご"):
            return_value = GaGyo
        elif input_str in ("さしすせそ"):
            return_value = SaGyo
        elif input_str in ("ざじずぜぞ"):
            return_value = ZaGyo
        elif input_str in ("たちつてと"):
            return_value = TaGyo
        elif input_str in ("だぢづでど"):
            return_value = DaGyo
        elif input_str in ("なにぬねの"):
            return_value = NaGyo
        elif input_str in ("はひふへほ"):
            return_value = HaGyo
        elif input_str in ("ばびぶべぼ"):
            return_value = BaGyo
        elif input_str in ("ぱぴぷぺぽ"):
            return_value = PaGyo
        elif input_str in ("まみむめも"):
            return_value = MaGyo
        elif input_str in ("らりるれろ"):
            return_value = RaGyo

        return return_value

    @classmethod
    def dan(cls, target: Dan) -> str:
        """Return the target vowel ending for this gyo
        
        Parameters
        ----------
        target: Dan
            Dan (vowel) for the Gyo (syllable group) that should be returned

        Returns
        -------
        str:
            String of the specified dan for this gyo
        """
        return getattr(cls, target.name).value

class AGyo(Gyo):
    """A Gyo enum"""
    A = "あ"
    I = "い"
    U = "う"
    E = "え"
    O = "お"

class KaGyo(Gyo):
    """Ka Gyo enum"""
    A = "か"
    I = "き"
    U = "く"
    E = "け"
    O = "こ"

class GaGyo(Gyo):
    """Ga Gyo enum"""
    A = "が"
    I = "ぎ"
    U = "ぐ"
    E = "げ"
    O = "ご"

class SaGyo(Gyo):
    """Sa Gyo enum"""
    A = "さ"
    I = "し"
    U = "す"
    E = "せ"
    O = "そ"

class ZaGyo(Gyo):
    """Za Gyo enum"""
    A = "ざ"
    I = "じ"
    U = "ず"
    E = "ぜ"
    O = "ぞ"

class TaGyo(Gyo):
    """Ta Gyo enum"""
    A = "た"
    I = "ち"
    U = "つ"
    E = "て"
    O = "と"

class DaGyo(Gyo):
    """Da Gyo enum"""
    A = "だ"
    I = "ぢ"
    U = "づ"
    E = "で"
    O = "ど"

class NaGyo(Gyo):
    """Na Gyo enum"""
    A = "な"
    I = "に"
    U = "ぬ"
    E = "ね"
    O = "の"

class HaGyo(Gyo):
    """Ha Gyo enum"""
    A = "は"
    I = "ひ"
    U = "ふ"
    E = "へ"
    O = "ほ"

class BaGyo(Gyo):
    """Ba Gyo enum"""
    A = "ば"
    I = "び"
    U = "ぶ"
    E = "べ"
    O = "ぼ"

class PaGyo(Gyo):
    """Pa Gyo enum"""
    A = "ぱ"
    I = "ぴ"
    U = "ぷ"
    E = "ぺ"
    O = "ぽ"

class MaGyo(Gyo):
    """Ma Gyo enum"""
    A = "ま"
    I = "み"
    U = "む"
    E = "め"
    O = "も"

class RaGyo(Gyo):
    """Ra Gyo enum"""
    A = "ら"
    I = "り"
    U = "る"
    E = "れ"
    O = "ろ"
