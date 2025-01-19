"""Various enumerated objects for use throughout the rest of the module"""
from enum import Enum

class Form(Enum):
    """Enumeration of known conjugation forms"""
    NON_PAST = 'non-past'
    NON_PAST_NEG = 'negative'
    PAST = 'past'
    PAST_NEG = 'past negative'
    TE = 'te'
    VOLITIONAL = 'volitional'

    # tai forms
    TAI_NON_PAST = 'tai non-past'
    TAI_NON_PAST_NEG = 'tai negative'
    TAI_PAST = 'tai past'
    TAI_PAST_NEG = 'tai past negative'
    TAI_TE = 'tai te'

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
