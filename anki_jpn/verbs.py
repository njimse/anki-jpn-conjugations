from enum import Enum

class Conjugation(Enum):
    NON_PAST = 1
    NON_PAST_NEGATIVE = 2

endings = {
    Conjugation.NON_PAST: "ます",
    Conjugation.NON_PAST_NEGATIVE: "ません"
}

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

def get_godan_stem(input):
    stem = input[:-1] + godan_stem_mapping[input[-1]]
    return stem

def conjugate_ichidan(dictionary_form: str, target: Conjugation = Conjugation.NON_PAST) -> str:
    assert dictionary_form.endswith('る')
    stem = dictionary_form[:-1]
    completion = stem + endings[target]
    return completion

def conjugate_godan(dictionary_form: str, target: Conjugation = Conjugation.NON_PAST) -> str:
    stem = get_godan_stem(dictionary_form)
    completion = stem + endings[target]
    return completion