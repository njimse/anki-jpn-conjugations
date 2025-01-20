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
        result.append(self.simple_name)
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
