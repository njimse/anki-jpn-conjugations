from ..enums import VerbClass


godan_te_mapping = {
    "う": "って",
    "つ": "って",
    "る": "って",
    "ぬ": "んで",
    "む": "んで",
    "ぶ": "んで",
    "く": "いて",
    "ぐ": "いで",
    "す": "して",
}

def te(dictionary_form: str, verb_class: VerbClass) -> str:
    """Get the Te form conjugation

    Parameters
    ----------
    dictionary_form : str
        Dictionary form of the verb to be conjugated
    verb_class : VerbClass
        Class of the verb being conjugated

    Returns
    -------
    str
        Conjugated verb
    """
    completion = None
    if verb_class == VerbClass.ICHIDAN:
        completion = dictionary_form[:-1] + "て"
    elif verb_class == VerbClass.GODAN:
        if dictionary_form.endswith('行[い]く') or dictionary_form.endswith('いく') \
            or dictionary_form.endswith('行く'):

            completion = dictionary_form[:-1] + "って"
        else:
            completion = dictionary_form[:-1] + godan_te_mapping[dictionary_form[-1]]
    elif verb_class == VerbClass.IRREGULAR:
        if dictionary_form.endswith("する"):
            completion = dictionary_form[:-2] + "して"
        elif dictionary_form.endswith("来[く]る"):
            completion = dictionary_form[:-5] + "来[き]て"
        elif dictionary_form.endswith("くる"):
            completion = dictionary_form[:-2] + "きて"
        elif dictionary_form.endswith("来る"):
            if len(dictionary_form) == 2:
                completion = "来[き]て"
            else:
                completion = dictionary_form[:-2] + " 来[き]て"
        elif dictionary_form.endswith('しゃる') \
            or dictionary_form.endswith('なさる') \
            or dictionary_form.endswith('くださる') \
            or dictionary_form.endswith('下[くだ]さる') \
            or dictionary_form.endswith('下さる'):

            completion = dictionary_form[:-1] + "って"

    assert completion is not None
    return completion