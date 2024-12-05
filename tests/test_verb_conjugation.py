import pytest

from anki_jpn.verbs import conjugate_ichidan, conjugate_godan, Conjugation

ichidan_test_data = [
    ("開ける", Conjugation.NON_PAST, "開けます"),
    ("開ける", Conjugation.NON_PAST_NEGATIVE, "開けません")
]
@pytest.mark.parametrize("dict_form, tense, reference", ichidan_test_data)
def test_ichidan_conjugation(dict_form, tense, reference):
    result = conjugate_ichidan(dict_form, tense)
    assert result == reference


godan_test_data = [
    ("あそぶ", Conjugation.NON_PAST, "あそびます"),
    ("あそぶ", Conjugation.NON_PAST_NEGATIVE, "あそびません"),
    ("遊ぶ", Conjugation.NON_PAST, "遊びます"),
    ("遊ぶ", Conjugation.NON_PAST_NEGATIVE, "遊びません")
]
@pytest.mark.parametrize("dict_form, tense, reference", godan_test_data)
def test_godan_conjugation(dict_form, tense, reference):
    result = conjugate_godan(dict_form, tense)
    assert result == reference