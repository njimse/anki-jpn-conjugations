"""Tests covering the correctness of the causative conjugations"""
import pytest
from japanese_conjugation.enums import (
    VerbClass
)
from japanese_conjugation.verbs import (
    polite_nonpast_positive_causative,
    polite_nonpast_negative_causative,
    polite_past_positive_causative,
    polite_past_negative_causative,
    te_causative,
    plain_nonpast_positive_causative,
    plain_nonpast_negative_causative,
    plain_past_positive_causative,
    plain_past_negative_causative
)

polite_nonpast_positive_causative_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]させます'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]させます'),
    ('する', VerbClass.IRREGULAR, 'させます'),
    ('行[い]く', VerbClass.GODAN, '行[い]かせます'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをさせます'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]ませます'),
    ('買[か]う', VerbClass.GODAN, '買[か]わせます'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]させます'),
    ('くる', VerbClass.IRREGULAR, 'こさせます'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこさせます'),
    ('いく', VerbClass.GODAN, 'いかせます'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをさせます'),
    ('よむ', VerbClass.GODAN, 'よませます'),
    ('かう', VerbClass.GODAN, 'かわせます'),
    ('はなす', VerbClass.GODAN, 'はなさせます'),
    ('来る', VerbClass.IRREGULAR, '来[こ]させます'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]させます'),
    ('行く', VerbClass.GODAN, '行かせます'),
    ('読む', VerbClass.GODAN, '読ませます'),
    ('買う', VerbClass.GODAN, '買わせます'),
    ('話す', VerbClass.GODAN, '話させます'),
]
@pytest.mark.parametrize("dict_form, verb_class, reference", polite_nonpast_positive_causative_data)
def test_polite_nonpast_positive_causative(dict_form, verb_class, reference):
    """test the Polite Non-Past Causative conjugation"""
    result = polite_nonpast_positive_causative(dict_form, verb_class)
    assert result == reference

polite_nonpast_negative_causative_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]させません'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]させません'),
    ('する', VerbClass.IRREGULAR, 'させません'),
    ('行[い]く', VerbClass.GODAN, '行[い]かせません'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをさせません'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]ませません'),
    ('買[か]う', VerbClass.GODAN, '買[か]わせません'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]させません'),
    ('くる', VerbClass.IRREGULAR, 'こさせません'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこさせません'),
    ('する', VerbClass.IRREGULAR, 'させません'),
    ('いく', VerbClass.GODAN, 'いかせません'),
    ('よむ', VerbClass.GODAN, 'よませません'),
    ('かう', VerbClass.GODAN, 'かわせません'),
    ('はなす', VerbClass.GODAN, 'はなさせません'),
    ('来る', VerbClass.IRREGULAR, '来[こ]させません'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]させません'),
    ('行く', VerbClass.GODAN, '行かせません'),
    ('読む', VerbClass.GODAN, '読ませません'),
    ('買う', VerbClass.GODAN, '買わせません'),
    ('話す', VerbClass.GODAN, '話させません'),
]
@pytest.mark.parametrize("dict_form, verb_class, reference", polite_nonpast_negative_causative_data)
def test_polite_nonpast_negative_causative(dict_form, verb_class, reference):
    """test the Polite Non-Past Negative Causative conjugation"""
    result = polite_nonpast_negative_causative(dict_form, verb_class)
    assert result == reference

polite_past_positive_causative_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]させました'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]させました'),
    ('する', VerbClass.IRREGULAR, 'させました'),
    ('行[い]く', VerbClass.GODAN, '行[い]かせました'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをさせました'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]ませました'),
    ('買[か]う', VerbClass.GODAN, '買[か]わせました'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]させました'),
    ('くる', VerbClass.IRREGULAR, 'こさせました'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこさせました'),
    ('いく', VerbClass.GODAN, 'いかせました'),
    ('よむ', VerbClass.GODAN, 'よませました'),
    ('かう', VerbClass.GODAN, 'かわせました'),
    ('はなす', VerbClass.GODAN, 'はなさせました'),
    ('来る', VerbClass.IRREGULAR, '来[こ]させました'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]させました'),
    ('行く', VerbClass.GODAN, '行かせました'),
    ('読む', VerbClass.GODAN, '読ませました'),
    ('買う', VerbClass.GODAN, '買わせました'),
    ('話す', VerbClass.GODAN, '話させました'),
]
@pytest.mark.parametrize("dict_form, verb_class, reference", polite_past_positive_causative_data)
def test_polite_past_positive_causative(dict_form, verb_class, reference):
    """test the Polite Past Causative conjugation"""
    result = polite_past_positive_causative(dict_form, verb_class)
    assert result == reference

polite_past_negative_causative_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]させませんでした'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]させませんでした'),
    ('する', VerbClass.IRREGULAR, 'させませんでした'),
    ('行[い]く', VerbClass.GODAN, '行[い]かせませんでした'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをさせませんでした'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]ませませんでした'),
    ('買[か]う', VerbClass.GODAN, '買[か]わせませんでした'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]させませんでした'),
    ('くる', VerbClass.IRREGULAR, 'こさせませんでした'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこさせませんでした'),
    ('いく', VerbClass.GODAN, 'いかせませんでした'),
    ('よむ', VerbClass.GODAN, 'よませませんでした'),
    ('かう', VerbClass.GODAN, 'かわせませんでした'),
    ('はなす', VerbClass.GODAN, 'はなさせませんでした'),
    ('来る', VerbClass.IRREGULAR, '来[こ]させませんでした'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]させませんでした'),
    ('行く', VerbClass.GODAN, '行かせませんでした'),
    ('読む', VerbClass.GODAN, '読ませませんでした'),
    ('買う', VerbClass.GODAN, '買わせませんでした'),
    ('話す', VerbClass.GODAN, '話させませんでした'),
]
@pytest.mark.parametrize("dict_form, verb_class, reference", polite_past_negative_causative_data)
def test_polite_past_negative_causative(dict_form, verb_class, reference):
    """test the Polite Past Negative Causative conjugation"""
    result = polite_past_negative_causative(dict_form, verb_class)
    assert result == reference

te_causative_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]させて'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]させて'),
    ('する', VerbClass.IRREGULAR, 'させて'),
    ('行[い]く', VerbClass.GODAN, '行[い]かせて'),
    ('書[か]く', VerbClass.GODAN, '書[か]かせて'),
    ('遊[あそ]ぶ', VerbClass.GODAN, '遊[あそ]ばせて'),
    ('立[た]つ', VerbClass.GODAN, '立[た]たせて'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをさせて'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]ませて'),
    ('買[か]う', VerbClass.GODAN, '買[か]わせて'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]させて'),
    ('泳[およ]ぐ', VerbClass.GODAN, '泳[およ]がせて'),
    ('食[た]べる', VerbClass.ICHIDAN, '食[た]べさせて'),
    ('起[お]きる', VerbClass.ICHIDAN, '起[お]きさせて'),
    ('開[あ]ける', VerbClass.ICHIDAN, '開[あ]けさせて'),
    ('借[か]りる', VerbClass.ICHIDAN, '借[か]りさせて'),
    ('くる', VerbClass.IRREGULAR, 'こさせて'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこさせて'),
    ('いく', VerbClass.GODAN, 'いかせて'),
    ('かく', VerbClass.GODAN, 'かかせて'),
    ('あそぶ', VerbClass.GODAN, 'あそばせて'),
    ('たつ', VerbClass.GODAN, 'たたせて'),
    ('よむ', VerbClass.GODAN, 'よませて'),
    ('かう', VerbClass.GODAN, 'かわせて'),
    ('はなす', VerbClass.GODAN, 'はなさせて'),
    ('およぐ', VerbClass.GODAN, 'およがせて'),
    ('たべる', VerbClass.ICHIDAN, 'たべさせて'),
    ('おきる', VerbClass.ICHIDAN, 'おきさせて'),
    ('あける', VerbClass.ICHIDAN, 'あけさせて'),
    ('かりる', VerbClass.ICHIDAN, 'かりさせて'),
    ('来る', VerbClass.IRREGULAR, '来[こ]させて'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]させて'),
    ('行く', VerbClass.GODAN, '行かせて'),
    ('書く', VerbClass.GODAN, '書かせて'),
    ('遊ぶ', VerbClass.GODAN, '遊ばせて'),
    ('立つ', VerbClass.GODAN, '立たせて'),
    ('読む', VerbClass.GODAN, '読ませて'),
    ('買う', VerbClass.GODAN, '買わせて'),
    ('話す', VerbClass.GODAN, '話させて'),
    ('泳ぐ', VerbClass.GODAN, '泳がせて'),
    ('食べる', VerbClass.ICHIDAN, '食べさせて'),
    ('起きる', VerbClass.ICHIDAN, '起きさせて'),
    ('開ける', VerbClass.ICHIDAN, '開けさせて'),
    ('借りる', VerbClass.ICHIDAN, '借りさせて'),
]
@pytest.mark.parametrize("dict_form, verb_class, reference", te_causative_data)
def test_te_causative(dict_form, verb_class, reference):
    """test the Te Causative conjugation"""
    result = te_causative(dict_form, verb_class)
    assert result == reference

plain_nonpast_positive_causative_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]させる'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]させる'),
    ('する', VerbClass.IRREGULAR, 'させる'),
    ('行[い]く', VerbClass.GODAN, '行[い]かせる'),
    ('書[か]く', VerbClass.GODAN, '書[か]かせる'),
    ('遊[あそ]ぶ', VerbClass.GODAN, '遊[あそ]ばせる'),
    ('立[た]つ', VerbClass.GODAN, '立[た]たせる'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをさせる'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]ませる'),
    ('買[か]う', VerbClass.GODAN, '買[か]わせる'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]させる'),
    ('泳[およ]ぐ', VerbClass.GODAN, '泳[およ]がせる'),
    ('電話[でんわ]を 掛[か]ける', VerbClass.ICHIDAN, '電話[でんわ]を 掛[か]けさせる'),
    ('食[た]べる', VerbClass.ICHIDAN, '食[た]べさせる'),
    ('起[お]きる', VerbClass.ICHIDAN, '起[お]きさせる'),
    ('開[あ]ける', VerbClass.ICHIDAN, '開[あ]けさせる'),
    ('借[か]りる', VerbClass.ICHIDAN, '借[か]りさせる'),
    ('くる', VerbClass.IRREGULAR, 'こさせる'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこさせる'),
    ('いく', VerbClass.GODAN, 'いかせる'),
    ('かく', VerbClass.GODAN, 'かかせる'),
    ('あそぶ', VerbClass.GODAN, 'あそばせる'),
    ('たつ', VerbClass.GODAN, 'たたせる'),
    ('よむ', VerbClass.GODAN, 'よませる'),
    ('かう', VerbClass.GODAN, 'かわせる'),
    ('はなす', VerbClass.GODAN, 'はなさせる'),
    ('およぐ', VerbClass.GODAN, 'およがせる'),
    ('たべる', VerbClass.ICHIDAN, 'たべさせる'),
    ('おきる', VerbClass.ICHIDAN, 'おきさせる'),
    ('あける', VerbClass.ICHIDAN, 'あけさせる'),
    ('かりる', VerbClass.ICHIDAN, 'かりさせる'),
    ('来る', VerbClass.IRREGULAR, '来[こ]させる'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]させる'),
    ('行く', VerbClass.GODAN, '行かせる'),
    ('書く', VerbClass.GODAN, '書かせる'),
    ('遊ぶ', VerbClass.GODAN, '遊ばせる'),
    ('立つ', VerbClass.GODAN, '立たせる'),
    ('読む', VerbClass.GODAN, '読ませる'),
    ('買う', VerbClass.GODAN, '買わせる'),
    ('話す', VerbClass.GODAN, '話させる'),
    ('泳ぐ', VerbClass.GODAN, '泳がせる'),
    ('食べる', VerbClass.ICHIDAN, '食べさせる'),
    ('起きる', VerbClass.ICHIDAN, '起きさせる'),
    ('開ける', VerbClass.ICHIDAN, '開けさせる'),
    ('借りる', VerbClass.ICHIDAN, '借りさせる'),
]
@pytest.mark.parametrize("dict_form, verb_class, reference", plain_nonpast_positive_causative_data)
def test_plain_nonpast_positive_causative(dict_form, verb_class, reference):
    """test the Plain Non-Past Causative conjugation"""
    result = plain_nonpast_positive_causative(dict_form, verb_class)
    assert result == reference

plain_nonpast_negative_causative_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]させない'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]させない'),
    ('する', VerbClass.IRREGULAR, 'させない'),
    ('ある', VerbClass.GODAN, 'あらせない'),
    ('行[い]く', VerbClass.GODAN, '行[い]かせない'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをさせない'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]ませない'),
    ('買[か]う', VerbClass.GODAN, '買[か]わせない'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]させない'),
    ('くる', VerbClass.IRREGULAR, 'こさせない'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこさせない'),
    ('いく', VerbClass.GODAN, 'いかせない'),
    ('よむ', VerbClass.GODAN, 'よませない'),
    ('かう', VerbClass.GODAN, 'かわせない'),
    ('はなす', VerbClass.GODAN, 'はなさせない'),
    ('来る', VerbClass.IRREGULAR, '来[こ]させない'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]させない'),
    ('行く', VerbClass.GODAN, '行かせない'),
    ('読む', VerbClass.GODAN, '読ませない'),
    ('買う', VerbClass.GODAN, '買わせない'),
    ('話す', VerbClass.GODAN, '話させない'),
]
@pytest.mark.parametrize("dict_form, verb_class, reference", plain_nonpast_negative_causative_data)
def test_plain_nonpast_negative_causative(dict_form, verb_class, reference):
    """test the Plain Non-Past Negative Causative conjugation"""
    result = plain_nonpast_negative_causative(dict_form, verb_class)
    assert result == reference

plain_past_positive_causative_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]させた'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]させた'),
    ('する', VerbClass.IRREGULAR, 'させた'),
    ('行[い]く', VerbClass.GODAN, '行[い]かせた'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをさせた'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]ませた'),
    ('買[か]う', VerbClass.GODAN, '買[か]わせた'),
    ('泳[およ]ぐ', VerbClass.GODAN, '泳[およ]がせた'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]させた'),
    ('切[き]る', VerbClass.GODAN, '切[き]らせた'),
    ('くる', VerbClass.IRREGULAR, 'こさせた'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこさせた'),
    ('いく', VerbClass.GODAN, 'いかせた'),
    ('よむ', VerbClass.GODAN, 'よませた'),
    ('かう', VerbClass.GODAN, 'かわせた'),
    ('およぐ', VerbClass.GODAN, 'およがせた'),
    ('はなす', VerbClass.GODAN, 'はなさせた'),
    ('きる', VerbClass.GODAN, 'きらせた'),
    ('来る', VerbClass.IRREGULAR, '来[こ]させた'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]させた'),
    ('行く', VerbClass.GODAN, '行かせた'),
    ('読む', VerbClass.GODAN, '読ませた'),
    ('買う', VerbClass.GODAN, '買わせた'),
    ('泳ぐ', VerbClass.GODAN, '泳がせた'),
    ('話す', VerbClass.GODAN, '話させた'),
    ('切る', VerbClass.GODAN, '切らせた'),
]
@pytest.mark.parametrize("dict_form, verb_class, reference", plain_past_positive_causative_data)
def test_plain_past_positive_causative(dict_form, verb_class, reference):
    """test the Plain Past Causative conjugation"""
    result = plain_past_positive_causative(dict_form, verb_class)
    assert result == reference

plain_past_negative_causative_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]させなかった'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]させなかった'),
    ('する', VerbClass.IRREGULAR, 'させなかった'),
    ('行[い]く', VerbClass.GODAN, '行[い]かせなかった'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをさせなかった'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]ませなかった'),
    ('買[か]う', VerbClass.GODAN, '買[か]わせなかった'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]させなかった'),
    ('くる', VerbClass.IRREGULAR, 'こさせなかった'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこさせなかった'),
    ('いく', VerbClass.GODAN, 'いかせなかった'),
    ('よむ', VerbClass.GODAN, 'よませなかった'),
    ('かう', VerbClass.GODAN, 'かわせなかった'),
    ('はなす', VerbClass.GODAN, 'はなさせなかった'),
    ('来る', VerbClass.IRREGULAR, '来[こ]させなかった'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]させなかった'),
    ('行く', VerbClass.GODAN, '行かせなかった'),
    ('読む', VerbClass.GODAN, '読ませなかった'),
    ('買う', VerbClass.GODAN, '買わせなかった'),
    ('話す', VerbClass.GODAN, '話させなかった'),
]
@pytest.mark.parametrize("dict_form, verb_class, reference", plain_past_negative_causative_data)
def test_plain_past_negative_causative(dict_form, verb_class, reference):
    """test the Plain Past Negative Causative conjugation"""
    result = plain_past_negative_causative(dict_form, verb_class)
    assert result == reference
