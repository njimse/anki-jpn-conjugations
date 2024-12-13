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
