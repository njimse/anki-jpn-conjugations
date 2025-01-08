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
