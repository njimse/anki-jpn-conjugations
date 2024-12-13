from anki_jpn.enums import AdjectiveClass

def polite_nonpast_positive(dictionary_form: str, adj_class: AdjectiveClass):
    stem = dictionary_form[:-1]
    if adj_class == AdjectiveClass.NA:
        ending = 'です'
    else:
        ending = 'いです'
    completion = stem + ending
    return completion

def polite_nonpast_negative(dictionary_form: str, adj_class: AdjectiveClass):
    stem = dictionary_form[:-1]
    if adj_class == AdjectiveClass.NA:
        ending = 'じゃないです'
    else:
        ending = 'くないです'
    completion = stem + ending
    return completion

def polite_past_positive(dictionary_form: str, adj_class: AdjectiveClass):
    stem = dictionary_form[:-1]
    if adj_class == AdjectiveClass.NA:
        ending = 'でした'
    else:
        ending = 'かったです'
    completion = stem + ending
    return completion

def polite_past_negative(dictionary_form: str, adj_class: AdjectiveClass):
    stem = dictionary_form[:-1]
    if adj_class == AdjectiveClass.NA:
        ending = 'じゃなかったです'
    else:
        ending = 'くなかったです'
    completion = stem + ending
    return completion

def te(dictionary_form: str, adj_class: AdjectiveClass):
    stem = dictionary_form[:-1]
    if adj_class == AdjectiveClass.NA:
        ending = 'で'
    else:
        ending = 'くて'
    completion = stem + ending
    return completion