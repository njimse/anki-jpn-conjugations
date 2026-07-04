"""Tests covering the correctness of the causative-passive conjugations"""
import pytest
from japanese_conjugation.enums import (
    VerbClass
)
from japanese_conjugation.verbs import (
    polite_nonpast_positive_causative_passive,
    polite_nonpast_negative_causative_passive,
    polite_past_positive_causative_passive,
    polite_past_negative_causative_passive,
    te_causative_passive,
    plain_nonpast_positive_causative_passive,
    plain_nonpast_negative_causative_passive,
    plain_past_positive_causative_passive,
    plain_past_negative_causative_passive
)

polite_nonpast_positive_causative_passive_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]させられます'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]させられます'),
    ('する', VerbClass.IRREGULAR, 'させられます'),
    ('行[い]く', VerbClass.GODAN, '行[い]かされます'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをさせられます'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]まされます'),
    ('買[か]う', VerbClass.GODAN, '買[か]わされます'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]させられます'),
    ('くる', VerbClass.IRREGULAR, 'こさせられます'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこさせられます'),
    ('いく', VerbClass.GODAN, 'いかされます'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをさせられます'),
    ('よむ', VerbClass.GODAN, 'よまされます'),
    ('かう', VerbClass.GODAN, 'かわされます'),
    ('はなす', VerbClass.GODAN, 'はなさせられます'),
    ('来る', VerbClass.IRREGULAR, '来[こ]させられます'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]させられます'),
    ('行く', VerbClass.GODAN, '行かされます'),
    ('読む', VerbClass.GODAN, '読まされます'),
    ('買う', VerbClass.GODAN, '買わされます'),
    ('話す', VerbClass.GODAN, '話させられます'),
]
@pytest.mark.parametrize(
    "dict_form, verb_class, reference", polite_nonpast_positive_causative_passive_data)
def test_polite_nonpast_positive_causative_passive(dict_form, verb_class, reference):
    """test the Polite Non-Past Causative-Passive conjugation"""
    result = polite_nonpast_positive_causative_passive(dict_form, verb_class)
    assert result == reference

polite_nonpast_negative_causative_passive_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]させられません'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]させられません'),
    ('する', VerbClass.IRREGULAR, 'させられません'),
    ('行[い]く', VerbClass.GODAN, '行[い]かされません'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをさせられません'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]まされません'),
    ('買[か]う', VerbClass.GODAN, '買[か]わされません'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]させられません'),
    ('くる', VerbClass.IRREGULAR, 'こさせられません'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこさせられません'),
    ('する', VerbClass.IRREGULAR, 'させられません'),
    ('いく', VerbClass.GODAN, 'いかされません'),
    ('よむ', VerbClass.GODAN, 'よまされません'),
    ('かう', VerbClass.GODAN, 'かわされません'),
    ('はなす', VerbClass.GODAN, 'はなさせられません'),
    ('来る', VerbClass.IRREGULAR, '来[こ]させられません'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]させられません'),
    ('行く', VerbClass.GODAN, '行かされません'),
    ('読む', VerbClass.GODAN, '読まされません'),
    ('買う', VerbClass.GODAN, '買わされません'),
    ('話す', VerbClass.GODAN, '話させられません'),
]
@pytest.mark.parametrize(
    "dict_form, verb_class, reference", polite_nonpast_negative_causative_passive_data)
def test_polite_nonpast_negative_causative_passive(dict_form, verb_class, reference):
    """test the Polite Non-Past Negative Causative-Passive conjugation"""
    result = polite_nonpast_negative_causative_passive(dict_form, verb_class)
    assert result == reference

polite_past_positive_causative_passive_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]させられました'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]させられました'),
    ('する', VerbClass.IRREGULAR, 'させられました'),
    ('行[い]く', VerbClass.GODAN, '行[い]かされました'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをさせられました'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]まされました'),
    ('買[か]う', VerbClass.GODAN, '買[か]わされました'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]させられました'),
    ('くる', VerbClass.IRREGULAR, 'こさせられました'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこさせられました'),
    ('いく', VerbClass.GODAN, 'いかされました'),
    ('よむ', VerbClass.GODAN, 'よまされました'),
    ('かう', VerbClass.GODAN, 'かわされました'),
    ('はなす', VerbClass.GODAN, 'はなさせられました'),
    ('来る', VerbClass.IRREGULAR, '来[こ]させられました'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]させられました'),
    ('行く', VerbClass.GODAN, '行かされました'),
    ('読む', VerbClass.GODAN, '読まされました'),
    ('買う', VerbClass.GODAN, '買わされました'),
    ('話す', VerbClass.GODAN, '話させられました'),
]
@pytest.mark.parametrize(
    "dict_form, verb_class, reference", polite_past_positive_causative_passive_data)
def test_polite_past_positive_causative_passive(dict_form, verb_class, reference):
    """test the Polite Past Causative-Passive conjugation"""
    result = polite_past_positive_causative_passive(dict_form, verb_class)
    assert result == reference

polite_past_negative_causative_passive_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]させられませんでした'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]させられませんでした'),
    ('する', VerbClass.IRREGULAR, 'させられませんでした'),
    ('行[い]く', VerbClass.GODAN, '行[い]かされませんでした'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをさせられませんでした'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]まされませんでした'),
    ('買[か]う', VerbClass.GODAN, '買[か]わされませんでした'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]させられませんでした'),
    ('くる', VerbClass.IRREGULAR, 'こさせられませんでした'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこさせられませんでした'),
    ('いく', VerbClass.GODAN, 'いかされませんでした'),
    ('よむ', VerbClass.GODAN, 'よまされませんでした'),
    ('かう', VerbClass.GODAN, 'かわされませんでした'),
    ('はなす', VerbClass.GODAN, 'はなさせられませんでした'),
    ('来る', VerbClass.IRREGULAR, '来[こ]させられませんでした'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]させられませんでした'),
    ('行く', VerbClass.GODAN, '行かされませんでした'),
    ('読む', VerbClass.GODAN, '読まされませんでした'),
    ('買う', VerbClass.GODAN, '買わされませんでした'),
    ('話す', VerbClass.GODAN, '話させられませんでした'),
]
@pytest.mark.parametrize(
    "dict_form, verb_class, reference", polite_past_negative_causative_passive_data)
def test_polite_past_negative_causative_passive(dict_form, verb_class, reference):
    """test the Polite Past Negative Causative-Passive conjugation"""
    result = polite_past_negative_causative_passive(dict_form, verb_class)
    assert result == reference

te_causative_passive_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]させられて'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]させられて'),
    ('する', VerbClass.IRREGULAR, 'させられて'),
    ('行[い]く', VerbClass.GODAN, '行[い]かされて'),
    ('書[か]く', VerbClass.GODAN, '書[か]かされて'),
    ('遊[あそ]ぶ', VerbClass.GODAN, '遊[あそ]ばされて'),
    ('立[た]つ', VerbClass.GODAN, '立[た]たされて'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをさせられて'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]まされて'),
    ('買[か]う', VerbClass.GODAN, '買[か]わされて'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]させられて'),
    ('泳[およ]ぐ', VerbClass.GODAN, '泳[およ]がされて'),
    ('食[た]べる', VerbClass.ICHIDAN, '食[た]べさせられて'),
    ('起[お]きる', VerbClass.ICHIDAN, '起[お]きさせられて'),
    ('開[あ]ける', VerbClass.ICHIDAN, '開[あ]けさせられて'),
    ('借[か]りる', VerbClass.ICHIDAN, '借[か]りさせられて'),
    ('くる', VerbClass.IRREGULAR, 'こさせられて'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこさせられて'),
    ('いく', VerbClass.GODAN, 'いかされて'),
    ('かく', VerbClass.GODAN, 'かかされて'),
    ('あそぶ', VerbClass.GODAN, 'あそばされて'),
    ('たつ', VerbClass.GODAN, 'たたされて'),
    ('よむ', VerbClass.GODAN, 'よまされて'),
    ('かう', VerbClass.GODAN, 'かわされて'),
    ('はなす', VerbClass.GODAN, 'はなさせられて'),
    ('およぐ', VerbClass.GODAN, 'およがされて'),
    ('たべる', VerbClass.ICHIDAN, 'たべさせられて'),
    ('おきる', VerbClass.ICHIDAN, 'おきさせられて'),
    ('あける', VerbClass.ICHIDAN, 'あけさせられて'),
    ('かりる', VerbClass.ICHIDAN, 'かりさせられて'),
    ('来る', VerbClass.IRREGULAR, '来[こ]させられて'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]させられて'),
    ('行く', VerbClass.GODAN, '行かされて'),
    ('書く', VerbClass.GODAN, '書かされて'),
    ('遊ぶ', VerbClass.GODAN, '遊ばされて'),
    ('立つ', VerbClass.GODAN, '立たされて'),
    ('読む', VerbClass.GODAN, '読まされて'),
    ('買う', VerbClass.GODAN, '買わされて'),
    ('話す', VerbClass.GODAN, '話させられて'),
    ('泳ぐ', VerbClass.GODAN, '泳がされて'),
    ('食べる', VerbClass.ICHIDAN, '食べさせられて'),
    ('起きる', VerbClass.ICHIDAN, '起きさせられて'),
    ('開ける', VerbClass.ICHIDAN, '開けさせられて'),
    ('借りる', VerbClass.ICHIDAN, '借りさせられて'),
]
@pytest.mark.parametrize(
    "dict_form, verb_class, reference", te_causative_passive_data)
def test_te_causative_passive(dict_form, verb_class, reference):
    """test the Te Causative-Passive conjugation"""
    result = te_causative_passive(dict_form, verb_class)
    assert result == reference

plain_nonpast_positive_causative_passive_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]させられる'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]させられる'),
    ('する', VerbClass.IRREGULAR, 'させられる'),
    ('行[い]く', VerbClass.GODAN, '行[い]かされる'),
    ('書[か]く', VerbClass.GODAN, '書[か]かされる'),
    ('遊[あそ]ぶ', VerbClass.GODAN, '遊[あそ]ばされる'),
    ('立[た]つ', VerbClass.GODAN, '立[た]たされる'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをさせられる'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]まされる'),
    ('買[か]う', VerbClass.GODAN, '買[か]わされる'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]させられる'),
    ('泳[およ]ぐ', VerbClass.GODAN, '泳[およ]がされる'),
    ('電話[でんわ]を 掛[か]ける', VerbClass.ICHIDAN, '電話[でんわ]を 掛[か]けさせられる'),
    ('食[た]べる', VerbClass.ICHIDAN, '食[た]べさせられる'),
    ('起[お]きる', VerbClass.ICHIDAN, '起[お]きさせられる'),
    ('開[あ]ける', VerbClass.ICHIDAN, '開[あ]けさせられる'),
    ('借[か]りる', VerbClass.ICHIDAN, '借[か]りさせられる'),
    ('くる', VerbClass.IRREGULAR, 'こさせられる'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこさせられる'),
    ('いく', VerbClass.GODAN, 'いかされる'),
    ('かく', VerbClass.GODAN, 'かかされる'),
    ('あそぶ', VerbClass.GODAN, 'あそばされる'),
    ('たつ', VerbClass.GODAN, 'たたされる'),
    ('よむ', VerbClass.GODAN, 'よまされる'),
    ('かう', VerbClass.GODAN, 'かわされる'),
    ('はなす', VerbClass.GODAN, 'はなさせられる'),
    ('およぐ', VerbClass.GODAN, 'およがされる'),
    ('たべる', VerbClass.ICHIDAN, 'たべさせられる'),
    ('おきる', VerbClass.ICHIDAN, 'おきさせられる'),
    ('あける', VerbClass.ICHIDAN, 'あけさせられる'),
    ('かりる', VerbClass.ICHIDAN, 'かりさせられる'),
    ('来る', VerbClass.IRREGULAR, '来[こ]させられる'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]させられる'),
    ('行く', VerbClass.GODAN, '行かされる'),
    ('書く', VerbClass.GODAN, '書かされる'),
    ('遊ぶ', VerbClass.GODAN, '遊ばされる'),
    ('立つ', VerbClass.GODAN, '立たされる'),
    ('読む', VerbClass.GODAN, '読まされる'),
    ('買う', VerbClass.GODAN, '買わされる'),
    ('話す', VerbClass.GODAN, '話させられる'),
    ('泳ぐ', VerbClass.GODAN, '泳がされる'),
    ('食べる', VerbClass.ICHIDAN, '食べさせられる'),
    ('起きる', VerbClass.ICHIDAN, '起きさせられる'),
    ('開ける', VerbClass.ICHIDAN, '開けさせられる'),
    ('借りる', VerbClass.ICHIDAN, '借りさせられる'),
]
@pytest.mark.parametrize(
    "dict_form, verb_class, reference", plain_nonpast_positive_causative_passive_data)
def test_plain_nonpast_positive_causative_passive(dict_form, verb_class, reference):
    """test the Plain Non-Past Causative-Passive conjugation"""
    result = plain_nonpast_positive_causative_passive(dict_form, verb_class)
    assert result == reference

plain_nonpast_negative_causative_passive_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]させられない'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]させられない'),
    ('する', VerbClass.IRREGULAR, 'させられない'),
    ('ある', VerbClass.GODAN, 'あらされない'),
    ('行[い]く', VerbClass.GODAN, '行[い]かされない'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをさせられない'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]まされない'),
    ('買[か]う', VerbClass.GODAN, '買[か]わされない'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]させられない'),
    ('くる', VerbClass.IRREGULAR, 'こさせられない'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこさせられない'),
    ('いく', VerbClass.GODAN, 'いかされない'),
    ('よむ', VerbClass.GODAN, 'よまされない'),
    ('かう', VerbClass.GODAN, 'かわされない'),
    ('はなす', VerbClass.GODAN, 'はなさせられない'),
    ('来る', VerbClass.IRREGULAR, '来[こ]させられない'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]させられない'),
    ('行く', VerbClass.GODAN, '行かされない'),
    ('読む', VerbClass.GODAN, '読まされない'),
    ('買う', VerbClass.GODAN, '買わされない'),
    ('話す', VerbClass.GODAN, '話させられない'),
]
@pytest.mark.parametrize(
    "dict_form, verb_class, reference", plain_nonpast_negative_causative_passive_data)
def test_plain_nonpast_negative_causative_passive(dict_form, verb_class, reference):
    """test the Plain Non-Past Negative Causative-Passive conjugation"""
    result = plain_nonpast_negative_causative_passive(dict_form, verb_class)
    assert result == reference

plain_past_positive_causative_passive_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]させられた'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]させられた'),
    ('する', VerbClass.IRREGULAR, 'させられた'),
    ('行[い]く', VerbClass.GODAN, '行[い]かされた'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをさせられた'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]まされた'),
    ('買[か]う', VerbClass.GODAN, '買[か]わされた'),
    ('泳[およ]ぐ', VerbClass.GODAN, '泳[およ]がされた'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]させられた'),
    ('切[き]る', VerbClass.GODAN, '切[き]らされた'),
    ('くる', VerbClass.IRREGULAR, 'こさせられた'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこさせられた'),
    ('いく', VerbClass.GODAN, 'いかされた'),
    ('よむ', VerbClass.GODAN, 'よまされた'),
    ('かう', VerbClass.GODAN, 'かわされた'),
    ('およぐ', VerbClass.GODAN, 'およがされた'),
    ('はなす', VerbClass.GODAN, 'はなさせられた'),
    ('きる', VerbClass.GODAN, 'きらされた'),
    ('来る', VerbClass.IRREGULAR, '来[こ]させられた'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]させられた'),
    ('行く', VerbClass.GODAN, '行かされた'),
    ('読む', VerbClass.GODAN, '読まされた'),
    ('買う', VerbClass.GODAN, '買わされた'),
    ('泳ぐ', VerbClass.GODAN, '泳がされた'),
    ('話す', VerbClass.GODAN, '話させられた'),
    ('切る', VerbClass.GODAN, '切らされた'),
]
@pytest.mark.parametrize(
    "dict_form, verb_class, reference", plain_past_positive_causative_passive_data)
def test_plain_past_positive_causative_passive(dict_form, verb_class, reference):
    """test the Plain Past Causative-Passive conjugation"""
    result = plain_past_positive_causative_passive(dict_form, verb_class)
    assert result == reference

plain_past_negative_causative_passive_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]させられなかった'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]させられなかった'),
    ('する', VerbClass.IRREGULAR, 'させられなかった'),
    ('行[い]く', VerbClass.GODAN, '行[い]かされなかった'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをさせられなかった'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]まされなかった'),
    ('買[か]う', VerbClass.GODAN, '買[か]わされなかった'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]させられなかった'),
    ('くる', VerbClass.IRREGULAR, 'こさせられなかった'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこさせられなかった'),
    ('いく', VerbClass.GODAN, 'いかされなかった'),
    ('よむ', VerbClass.GODAN, 'よまされなかった'),
    ('かう', VerbClass.GODAN, 'かわされなかった'),
    ('はなす', VerbClass.GODAN, 'はなさせられなかった'),
    ('来る', VerbClass.IRREGULAR, '来[こ]させられなかった'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]させられなかった'),
    ('行く', VerbClass.GODAN, '行かされなかった'),
    ('読む', VerbClass.GODAN, '読まされなかった'),
    ('買う', VerbClass.GODAN, '買わされなかった'),
    ('話す', VerbClass.GODAN, '話させられなかった'),
]
@pytest.mark.parametrize(
    "dict_form, verb_class, reference", plain_past_negative_causative_passive_data)
def test_plain_past_negative_causative_passive(dict_form, verb_class, reference):
    """test the Plain Past Negative Causative-Passive conjugation"""
    result = plain_past_negative_causative_passive(dict_form, verb_class)
    assert result == reference
