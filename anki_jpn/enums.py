from enum import Enum

class Form(Enum):
    NON_PAST = 'non-past'
    NON_PAST_NEG = 'negative'
    PAST = 'past'
    PAST_NEG = 'past negative'
    TE = 'te'
    VOLITIONAL = 'volitional'

class Formality(Enum):
    POLITE = 'polite'
    PLAIN = 'plain'

class VerbClass(Enum):
    GODAN = 'godan'
    ICHIDAN = 'ichidan'
    IRREGULAR = 'irregular'

class AdjectiveClass(Enum):
    NA = 'na-adjective'
    I = 'i-adjective'

class ModelType(Enum):
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