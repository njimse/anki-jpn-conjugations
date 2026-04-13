"""Tests covering the correctness of the passive conjugations"""
import pytest
from japanese_conjugation.enums import (
    VerbClass
)
from japanese_conjugation.verbs import (
    polite_nonpast_positive_passive,
    polite_nonpast_negative_passive,
    polite_past_positive_passive,
    polite_past_negative_passive,
    te_passive,
    plain_nonpast_positive_passive,
    plain_nonpast_negative_passive,
    plain_past_positive_passive,
    plain_past_negative_passive
)

polite_nonpast_positive_passive_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]られます'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]られます'),
    ('する', VerbClass.IRREGULAR, 'されます'),
    ('行[い]く', VerbClass.GODAN, '行[い]かれます'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをされます'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]まれます'),
    ('買[か]う', VerbClass.GODAN, '買[か]われます'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]されます'),
    # No kanji
    ('くる', VerbClass.IRREGULAR, 'こられます'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこられます'),
    ('いく', VerbClass.GODAN, 'いかれます'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをされます'),
    ('よむ', VerbClass.GODAN, 'よまれます'),
    ('かう', VerbClass.GODAN, 'かわれます'),
    ('はなす', VerbClass.GODAN, 'はなされます'),
    # no furigana
    ('来る', VerbClass.IRREGULAR, '来[こ]られます'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]られます'),
    ('行く', VerbClass.GODAN, '行かれます'),
    ('読む', VerbClass.GODAN, '読まれます'),
    ('買う', VerbClass.GODAN, '買われます'),
    ('話す', VerbClass.GODAN, '話されます'),
]
@pytest.mark.parametrize("dict_form, verb_class, reference", polite_nonpast_positive_passive_data)
def test_polite_nonpast_positive_passive(dict_form, verb_class, reference):
    """test the Polite Non-Past Passive conjugation"""
    result = polite_nonpast_positive_passive(dict_form, verb_class)
    assert result == reference

polite_nonpast_negative_passive_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]られません'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]られません'),
    ('する', VerbClass.IRREGULAR, 'されません'),
    ('行[い]く', VerbClass.GODAN, '行[い]かれません'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをされません'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]まれません'),
    ('買[か]う', VerbClass.GODAN, '買[か]われません'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]されません'),
    # no kanji
    ('くる', VerbClass.IRREGULAR, 'こられません'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこられません'),
    ('する', VerbClass.IRREGULAR, 'されません'),
    ('いく', VerbClass.GODAN, 'いかれません'),
    ('よむ', VerbClass.GODAN, 'よまれません'),
    ('かう', VerbClass.GODAN, 'かわれません'),
    ('はなす', VerbClass.GODAN, 'はなされません'),
    # no furigana
    ('来る', VerbClass.IRREGULAR, '来[こ]られません'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]られません'),
    ('行く', VerbClass.GODAN, '行かれません'),
    ('読む', VerbClass.GODAN, '読まれません'),
    ('買う', VerbClass.GODAN, '買われません'),
    ('話す', VerbClass.GODAN, '話されません'),
]
@pytest.mark.parametrize("dict_form, verb_class, reference", polite_nonpast_negative_passive_data)
def test_polite_nonpast_negative_passive(dict_form, verb_class, reference):
    """test the Polite Non-Past Negative Passive conjugation"""
    result = polite_nonpast_negative_passive(dict_form, verb_class)
    assert result == reference

polite_past_positive_passive_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]られました'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]られました'),
    ('する', VerbClass.IRREGULAR, 'されました'),
    ('行[い]く', VerbClass.GODAN, '行[い]かれました'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをされました'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]まれました'),
    ('買[か]う', VerbClass.GODAN, '買[か]われました'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]されました'),
    # no kanji
    ('くる', VerbClass.IRREGULAR, 'こられました'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこられました'),
    ('いく', VerbClass.GODAN, 'いかれました'),
    ('よむ', VerbClass.GODAN, 'よまれました'),
    ('かう', VerbClass.GODAN, 'かわれました'),
    ('はなす', VerbClass.GODAN, 'はなされました'),
    # no furigana
    ('来る', VerbClass.IRREGULAR, '来[こ]られました'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]られました'),
    ('行く', VerbClass.GODAN, '行かれました'),
    ('読む', VerbClass.GODAN, '読まれました'),
    ('買う', VerbClass.GODAN, '買われました'),
    ('話す', VerbClass.GODAN, '話されました'),
]
@pytest.mark.parametrize("dict_form, verb_class, reference", polite_past_positive_passive_data)
def test_polite_past_positive_passive(dict_form, verb_class, reference):
    """test the Polite Past Passive conjugation"""
    result = polite_past_positive_passive(dict_form, verb_class)
    assert result == reference

polite_past_negative_passive_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]られませんでした'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]られませんでした'),
    ('する', VerbClass.IRREGULAR, 'されませんでした'),
    ('行[い]く', VerbClass.GODAN, '行[い]かれませんでした'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをされませんでした'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]まれませんでした'),
    ('買[か]う', VerbClass.GODAN, '買[か]われませんでした'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]されませんでした'),
    # no kanji
    ('くる', VerbClass.IRREGULAR, 'こられませんでした'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこられませんでした'),
    ('いく', VerbClass.GODAN, 'いかれませんでした'),
    ('よむ', VerbClass.GODAN, 'よまれませんでした'),
    ('かう', VerbClass.GODAN, 'かわれませんでした'),
    ('はなす', VerbClass.GODAN, 'はなされませんでした'),
    # no furigana
    ('来る', VerbClass.IRREGULAR, '来[こ]られませんでした'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]られませんでした'),
    ('行く', VerbClass.GODAN, '行かれませんでした'),
    ('読む', VerbClass.GODAN, '読まれませんでした'),
    ('買う', VerbClass.GODAN, '買われませんでした'),
    ('話す', VerbClass.GODAN, '話されませんでした')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", polite_past_negative_passive_data)
def test_polite_past_negative_passive(dict_form, verb_class, reference):
    """test the Polite Past Negative Passive conjugation"""
    result = polite_past_negative_passive(dict_form, verb_class)
    assert result == reference


te_passive_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]られて'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]られて'),
    ('する', VerbClass.IRREGULAR, 'されて'),
    ('行[い]く', VerbClass.GODAN, '行[い]かれて'),
    ('書[か]く', VerbClass.GODAN, '書[か]かれて'),
    ('遊[あそ]ぶ', VerbClass.GODAN, '遊[あそ]ばれて'),
    ('立[た]つ', VerbClass.GODAN, '立[た]たれて'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをされて'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]まれて'),
    ('買[か]う', VerbClass.GODAN, '買[か]われて'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]されて'),
    ('泳[およ]ぐ', VerbClass.GODAN, '泳[およ]がれて'),
    ('食[た]べる', VerbClass.ICHIDAN, '食[た]べられて'),
    ('起[お]きる', VerbClass.ICHIDAN, '起[お]きられて'),
    ('開[あ]ける', VerbClass.ICHIDAN, '開[あ]けられて'),
    ('借[か]りる', VerbClass.ICHIDAN, '借[か]りられて'),
    # no kanji
    ('くる', VerbClass.IRREGULAR, 'こられて'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこられて'),
    ('いく', VerbClass.GODAN, 'いかれて'),
    ('かく', VerbClass.GODAN, 'かかれて'),
    ('あそぶ', VerbClass.GODAN, 'あそばれて'),
    ('たつ', VerbClass.GODAN, 'たたれて'),
    ('よむ', VerbClass.GODAN, 'よまれて'),
    ('かう', VerbClass.GODAN, 'かわれて'),
    ('はなす', VerbClass.GODAN, 'はなされて'),
    ('およぐ', VerbClass.GODAN, 'およがれて'),
    ('たべる', VerbClass.ICHIDAN, 'たべられて'),
    ('おきる', VerbClass.ICHIDAN, 'おきられて'),
    ('あける', VerbClass.ICHIDAN, 'あけられて'),
    ('かりる', VerbClass.ICHIDAN, 'かりられて'),
    # no furigana
    ('来る', VerbClass.IRREGULAR, '来[こ]られて'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]られて'),
    ('行く', VerbClass.GODAN, '行かれて'),
    ('書く', VerbClass.GODAN, '書かれて'),
    ('遊ぶ', VerbClass.GODAN, '遊ばれて'),
    ('立つ', VerbClass.GODAN, '立たれて'),
    ('読む', VerbClass.GODAN, '読まれて'),
    ('買う', VerbClass.GODAN, '買われて'),
    ('話す', VerbClass.GODAN, '話されて'),
    ('泳ぐ', VerbClass.GODAN, '泳がれて'),
    ('食べる', VerbClass.ICHIDAN, '食べられて'),
    ('起きる', VerbClass.ICHIDAN, '起きられて'),
    ('開ける', VerbClass.ICHIDAN, '開けられて'),
    ('借りる', VerbClass.ICHIDAN, '借りられて')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", te_passive_data)
def test_te_passive(dict_form, verb_class, reference):
    """test the Te Passive conjugation"""
    result = te_passive(dict_form, verb_class)
    assert result == reference


plain_nonpast_positive_passive_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]られる'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]られる'),
    ('する', VerbClass.IRREGULAR, 'される'),
    ('行[い]く', VerbClass.GODAN, '行[い]かれる'),
    ('書[か]く', VerbClass.GODAN, '書[か]かれる'),
    ('遊[あそ]ぶ', VerbClass.GODAN, '遊[あそ]ばれる'),
    ('立[た]つ', VerbClass.GODAN, '立[た]たれる'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをされる'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]まれる'),
    ('買[か]う', VerbClass.GODAN, '買[か]われる'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]される'),
    ('泳[およ]ぐ', VerbClass.GODAN, '泳[およ]がれる'),
    ('電話[でんわ]を 掛[か]ける', VerbClass.ICHIDAN, '電話[でんわ]を 掛[か]けられる'),
    ('食[た]べる', VerbClass.ICHIDAN, '食[た]べられる'),
    ('起[お]きる', VerbClass.ICHIDAN, '起[お]きられる'),
    ('開[あ]ける', VerbClass.ICHIDAN, '開[あ]けられる'),
    ('借[か]りる', VerbClass.ICHIDAN, '借[か]りられる'),
    # no kanji
    ('くる', VerbClass.IRREGULAR, 'こられる'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこられる'),
    ('いく', VerbClass.GODAN, 'いかれる'),
    ('かく', VerbClass.GODAN, 'かかれる'),
    ('あそぶ', VerbClass.GODAN, 'あそばれる'),
    ('たつ', VerbClass.GODAN, 'たたれる'),
    ('よむ', VerbClass.GODAN, 'よまれる'),
    ('かう', VerbClass.GODAN, 'かわれる'),
    ('はなす', VerbClass.GODAN, 'はなされる'),
    ('およぐ', VerbClass.GODAN, 'およがれる'),
    ('たべる', VerbClass.ICHIDAN, 'たべられる'),
    ('おきる', VerbClass.ICHIDAN, 'おきられる'),
    ('あける', VerbClass.ICHIDAN, 'あけられる'),
    ('かりる', VerbClass.ICHIDAN, 'かりられる'),
    # no furigana
    ('来る', VerbClass.IRREGULAR, '来[こ]られる'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]られる'),
    ('行く', VerbClass.GODAN, '行かれる'),
    ('書く', VerbClass.GODAN, '書かれる'),
    ('遊ぶ', VerbClass.GODAN, '遊ばれる'),
    ('立つ', VerbClass.GODAN, '立たれる'),
    ('読む', VerbClass.GODAN, '読まれる'),
    ('買う', VerbClass.GODAN, '買われる'),
    ('話す', VerbClass.GODAN, '話される'),
    ('泳ぐ', VerbClass.GODAN, '泳がれる'),
    ('食べる', VerbClass.ICHIDAN, '食べられる'),
    ('起きる', VerbClass.ICHIDAN, '起きられる'),
    ('開ける', VerbClass.ICHIDAN, '開けられる'),
    ('借りる', VerbClass.ICHIDAN, '借りられる')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", plain_nonpast_positive_passive_data)
def test_plain_nonpast_positive_passive(dict_form, verb_class, reference):
    """test the Plain Non-Past Passive conjugation"""
    # Note the VerbClass isn't actually used for this function, but we have the
    # parameter to keep consistency with the other conjugation functions
    result = plain_nonpast_positive_passive(dict_form, verb_class)
    assert result == reference

plain_nonpast_negative_passive_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]られない'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]られない'),
    ('する', VerbClass.IRREGULAR, 'されない'),
    ('ある', VerbClass.GODAN, 'あられない'),
    ('行[い]く', VerbClass.GODAN, '行[い]かれない'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをされない'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]まれない'),
    ('買[か]う', VerbClass.GODAN, '買[か]われない'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]されない'),
    # no kanji
    ('くる', VerbClass.IRREGULAR, 'こられない'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこられない'),
    ('いく', VerbClass.GODAN, 'いかれない'),
    ('よむ', VerbClass.GODAN, 'よまれない'),
    ('かう', VerbClass.GODAN, 'かわれない'),
    ('はなす', VerbClass.GODAN, 'はなされない'),
    # no furigana
    ('来る', VerbClass.IRREGULAR, '来[こ]られない'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]られない'),
    ('行く', VerbClass.GODAN, '行かれない'),
    ('読む', VerbClass.GODAN, '読まれない'),
    ('買う', VerbClass.GODAN, '買われない'),
    ('話す', VerbClass.GODAN, '話されない')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", plain_nonpast_negative_passive_data)
def test_plain_nonpast_negative_passive(dict_form, verb_class, reference):
    """test the Plain Non-Past Negative Passive conjugation"""
    result = plain_nonpast_negative_passive(dict_form, verb_class)
    assert result == reference

plain_past_positive_passive_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]られた'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]られた'),
    ('する', VerbClass.IRREGULAR, 'された'),
    ('行[い]く', VerbClass.GODAN, '行[い]かれた'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをされた'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]まれた'),
    ('買[か]う', VerbClass.GODAN, '買[か]われた'),
    ('泳[およ]ぐ', VerbClass.GODAN, '泳[およ]がれた'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]された'),
    ('切[き]る', VerbClass.GODAN, '切[き]られた'),
    # no kanji
    ('くる', VerbClass.IRREGULAR, 'こられた'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこられた'),
    ('いく', VerbClass.GODAN, 'いかれた'),
    ('よむ', VerbClass.GODAN, 'よまれた'),
    ('かう', VerbClass.GODAN, 'かわれた'),
    ('およぐ', VerbClass.GODAN, 'およがれた'),
    ('はなす', VerbClass.GODAN, 'はなされた'),
    ('きる', VerbClass.GODAN, 'きられた'),
    # no furigana
    ('来る', VerbClass.IRREGULAR, '来[こ]られた'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]られた'),
    ('行く', VerbClass.GODAN, '行かれた'),
    ('読む', VerbClass.GODAN, '読まれた'),
    ('買う', VerbClass.GODAN, '買われた'),
    ('泳ぐ', VerbClass.GODAN, '泳がれた'),
    ('話す', VerbClass.GODAN, '話された'),
    ('切る', VerbClass.GODAN, '切られた')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", plain_past_positive_passive_data)
def test_plain_past_positive_passive(dict_form, verb_class, reference):
    """test the Plain Past Potenial conjugation"""
    result = plain_past_positive_passive(dict_form, verb_class)
    assert result == reference

plain_past_negative_passive_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]られなかった'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]られなかった'),
    ('する', VerbClass.IRREGULAR, 'されなかった'),
    ('行[い]く', VerbClass.GODAN, '行[い]かれなかった'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをされなかった'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]まれなかった'),
    ('買[か]う', VerbClass.GODAN, '買[か]われなかった'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]されなかった'),
    # no kanji
    ('くる', VerbClass.IRREGULAR, 'こられなかった'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこられなかった'),
    ('いく', VerbClass.GODAN, 'いかれなかった'),
    ('よむ', VerbClass.GODAN, 'よまれなかった'),
    ('かう', VerbClass.GODAN, 'かわれなかった'),
    ('はなす', VerbClass.GODAN, 'はなされなかった'),
    # no furigana
    ('来る', VerbClass.IRREGULAR, '来[こ]られなかった'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]られなかった'),
    ('行く', VerbClass.GODAN, '行かれなかった'),
    ('読む', VerbClass.GODAN, '読まれなかった'),
    ('買う', VerbClass.GODAN, '買われなかった'),
    ('話す', VerbClass.GODAN, '話されなかった')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", plain_past_negative_passive_data)
def test_plain_past_negative_passive(dict_form, verb_class, reference):
    """test the Plain Past Negative Passive conjugation"""
    result = plain_past_negative_passive(dict_form, verb_class)
    assert result == reference
