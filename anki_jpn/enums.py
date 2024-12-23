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

class AdjectiveClass(Enum):
    """Enumeration of known adjective types"""
    NA = 'na-adjective'
    I = 'i-adjective'

class ModelType(Enum):
    """enumeration of model (a.k.a. Note) types"""
    VERB = 'verb'
    ADJECTIVE = 'adjective'

VERB_COMBOS = [
    (Formality.POLITE, Form.NON_PAST),
    (Formality.POLITE, Form.NON_PAST_NEG),
    (Formality.POLITE, Form.PAST),
    (Formality.POLITE, Form.PAST_NEG),
    (Formality.POLITE, Form.VOLITIONAL),
    (None, Form.TE),
    (Formality.PLAIN, Form.NON_PAST),
    (Formality.PLAIN, Form.NON_PAST_NEG),
    (Formality.PLAIN, Form.PAST),
    (Formality.PLAIN, Form.PAST_NEG)
]

ADJECTIVE_COMBOS = [
    (Formality.POLITE, Form.NON_PAST),
    (Formality.POLITE, Form.NON_PAST_NEG),
    (Formality.POLITE, Form.PAST),
    (Formality.POLITE, Form.PAST_NEG),
    (None, Form.TE),
    (Formality.PLAIN, Form.NON_PAST),
    (Formality.PLAIN, Form.NON_PAST_NEG),
    (Formality.PLAIN, Form.PAST),
    (Formality.PLAIN, Form.PAST_NEG)
]
