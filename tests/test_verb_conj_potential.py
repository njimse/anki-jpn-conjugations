import pytest
from japanese_conjugation.enums import VerbClass
from japanese_conjugation.verbs import (
    polite_nonpast_positive_potential,
    polite_nonpast_negative_potential,
    polite_past_positive_potential,
    polite_past_negative_potential,
    te_potential,
    plain_nonpast_positive_potential,
    plain_nonpast_negative_potential,
    plain_past_positive_potential,
    plain_past_negative_potential
)

polite_nonpast_positive_potential_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]られます'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]られます'),
    ('する', VerbClass.IRREGULAR, 'できます'),
    ('行[い]く', VerbClass.GODAN, '行[い]けます'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツができます'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]めます'),
    ('買[か]う', VerbClass.GODAN, '買[か]えます'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]せます'),
    # No kanji
    ('くる', VerbClass.IRREGULAR, 'こられます'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこられます'),
    ('いく', VerbClass.GODAN, 'いけます'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツができます'),
    ('よむ', VerbClass.GODAN, 'よめます'),
    ('かう', VerbClass.GODAN, 'かえます'),
    ('はなす', VerbClass.GODAN, 'はなせます'),
    # no furigana
    ('来る', VerbClass.IRREGULAR, '来[こ]られます'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]られます'),
    ('行く', VerbClass.GODAN, '行けます'),
    ('読む', VerbClass.GODAN, '読めます'),
    ('買う', VerbClass.GODAN, '買えます'),
    ('話す', VerbClass.GODAN, '話せます'),
]
@pytest.mark.parametrize("dict_form, verb_class, reference", polite_nonpast_positive_potential_data)
def test_polite_nonpast_positive_potential(dict_form, verb_class, reference):
    """test the Polite Non-Past Potential conjugation"""
    result = polite_nonpast_positive_potential(dict_form, verb_class)
    assert result == reference

polite_nonpast_negative_potential_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]られません'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]られません'),
    ('する', VerbClass.IRREGULAR, 'できません'),
    ('行[い]く', VerbClass.GODAN, '行[い]けません'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツができません'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]めません'),
    ('買[か]う', VerbClass.GODAN, '買[か]えません'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]せません'),
    # no kanji
    ('くる', VerbClass.IRREGULAR, 'こられません'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこられません'),
    ('する', VerbClass.IRREGULAR, 'できません'),
    ('いく', VerbClass.GODAN, 'いけません'),
    ('よむ', VerbClass.GODAN, 'よめません'),
    ('かう', VerbClass.GODAN, 'かえません'),
    ('はなす', VerbClass.GODAN, 'はなせません'),
    # no furigana
    ('来る', VerbClass.IRREGULAR, '来[こ]られません'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]られません'),
    ('行く', VerbClass.GODAN, '行けません'),
    ('読む', VerbClass.GODAN, '読めません'),
    ('買う', VerbClass.GODAN, '買えません'),
    ('話す', VerbClass.GODAN, '話せません'),
]
@pytest.mark.parametrize("dict_form, verb_class, reference", polite_nonpast_negative_potential_data)
def test_polite_nonpast_negative_potential(dict_form, verb_class, reference):
    """test the Polite Non-Past Negative Potential conjugation"""
    result = polite_nonpast_negative_potential(dict_form, verb_class)
    assert result == reference

polite_past_positive_potential_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]られました'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]られました'),
    ('する', VerbClass.IRREGULAR, 'できました'),
    ('行[い]く', VerbClass.GODAN, '行[い]けました'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツができました'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]めました'),
    ('買[か]う', VerbClass.GODAN, '買[か]えました'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]せました'),
    # no kanji
    ('くる', VerbClass.IRREGULAR, 'こられました'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこられました'),
    ('いく', VerbClass.GODAN, 'いけました'),
    ('よむ', VerbClass.GODAN, 'よめました'),
    ('かう', VerbClass.GODAN, 'かえました'),
    ('はなす', VerbClass.GODAN, 'はなせました'),
    # no furigana
    ('来る', VerbClass.IRREGULAR, '来[こ]られました'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]られました'),
    ('行く', VerbClass.GODAN, '行けました'),
    ('読む', VerbClass.GODAN, '読めました'),
    ('買う', VerbClass.GODAN, '買えました'),
    ('話す', VerbClass.GODAN, '話せました'),
]
@pytest.mark.parametrize("dict_form, verb_class, reference", polite_past_positive_potential_data)
def test_polite_past_positive_potential(dict_form, verb_class, reference):
    """test the Polite Past Potential conjugation"""
    result = polite_past_positive_potential(dict_form, verb_class)
    assert result == reference

polite_past_negative_potential_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]られませんでした'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]られませんでした'),
    ('する', VerbClass.IRREGULAR, 'できませんでした'),
    ('行[い]く', VerbClass.GODAN, '行[い]けませんでした'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツができませんでした'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]めませんでした'),
    ('買[か]う', VerbClass.GODAN, '買[か]えませんでした'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]せませんでした'),
    # no kanji
    ('くる', VerbClass.IRREGULAR, 'こられませんでした'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこられませんでした'),
    ('いく', VerbClass.GODAN, 'いけませんでした'),
    ('よむ', VerbClass.GODAN, 'よめませんでした'),
    ('かう', VerbClass.GODAN, 'かえませんでした'),
    ('はなす', VerbClass.GODAN, 'はなせませんでした'),
    # no furigana
    ('来る', VerbClass.IRREGULAR, '来[こ]られませんでした'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]られませんでした'),
    ('行く', VerbClass.GODAN, '行けませんでした'),
    ('読む', VerbClass.GODAN, '読めませんでした'),
    ('買う', VerbClass.GODAN, '買えませんでした'),
    ('話す', VerbClass.GODAN, '話せませんでした')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", polite_past_negative_potential_data)
def test_polite_past_negative_potential(dict_form, verb_class, reference):
    """test the Polite Past Negative Potential conjugation"""
    result = polite_past_negative_potential(dict_form, verb_class)
    assert result == reference


te_potential_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]られて'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]られて'),
    ('する', VerbClass.IRREGULAR, 'できて'),
    ('行[い]く', VerbClass.GODAN, '行[い]けて'),
    ('書[か]く', VerbClass.GODAN, '書[か]けて'),
    ('遊[あそ]ぶ', VerbClass.GODAN, '遊[あそ]べて'),
    ('立[た]つ', VerbClass.GODAN, '立[た]てて'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツができて'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]めて'),
    ('買[か]う', VerbClass.GODAN, '買[か]えて'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]せて'),
    ('泳[およ]ぐ', VerbClass.GODAN, '泳[およ]げて'),
    ('食[た]べる', VerbClass.ICHIDAN, '食[た]べられて'),
    ('起[お]きる', VerbClass.ICHIDAN, '起[お]きられて'),
    ('開[あ]ける', VerbClass.ICHIDAN, '開[あ]けられて'),
    ('借[か]りる', VerbClass.ICHIDAN, '借[か]りられて'),
    # no kanji
    ('くる', VerbClass.IRREGULAR, 'こられて'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこられて'),
    ('いく', VerbClass.GODAN, 'いけて'),
    ('かく', VerbClass.GODAN, 'かけて'),
    ('あそぶ', VerbClass.GODAN, 'あそべて'),
    ('たつ', VerbClass.GODAN, 'たてて'),
    ('よむ', VerbClass.GODAN, 'よめて'),
    ('かう', VerbClass.GODAN, 'かえて'),
    ('はなす', VerbClass.GODAN, 'はなせて'),
    ('およぐ', VerbClass.GODAN, 'およげて'),
    ('たべる', VerbClass.ICHIDAN, 'たべられて'),
    ('おきる', VerbClass.ICHIDAN, 'おきられて'),
    ('あける', VerbClass.ICHIDAN, 'あけられて'),
    ('かりる', VerbClass.ICHIDAN, 'かりられて'),
    # no furigana
    ('来る', VerbClass.IRREGULAR, '来[こ]られて'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]られて'),
    ('行く', VerbClass.GODAN, '行けて'),
    ('書く', VerbClass.GODAN, '書けて'),
    ('遊ぶ', VerbClass.GODAN, '遊べて'),
    ('立つ', VerbClass.GODAN, '立てて'),
    ('読む', VerbClass.GODAN, '読めて'),
    ('買う', VerbClass.GODAN, '買えて'),
    ('話す', VerbClass.GODAN, '話せて'),
    ('泳ぐ', VerbClass.GODAN, '泳げて'),
    ('食べる', VerbClass.ICHIDAN, '食べられて'),
    ('起きる', VerbClass.ICHIDAN, '起きられて'),
    ('開ける', VerbClass.ICHIDAN, '開けられて'),
    ('借りる', VerbClass.ICHIDAN, '借りられて')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", te_potential_data)
def test_te_potential(dict_form, verb_class, reference):
    """test the Te Potential conjugation"""
    result = te_potential(dict_form, verb_class)
    assert result == reference

plain_nonpast_positive_potential_data = [

    ('来[く]る', VerbClass.IRREGULAR, '来[こ]られる'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]られる'),
    ('する', VerbClass.IRREGULAR, 'できる'),
    ('行[い]く', VerbClass.GODAN, '行[い]ける'),
    ('書[か]く', VerbClass.GODAN, '書[か]ける'),
    ('遊[あそ]ぶ', VerbClass.GODAN, '遊[あそ]べる'),
    ('立[た]つ', VerbClass.GODAN, '立[た]てる'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツができる'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]める'),
    ('買[か]う', VerbClass.GODAN, '買[か]える'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]せる'),
    ('泳[およ]ぐ', VerbClass.GODAN, '泳[およ]げる'),
    ('電話[でんわ]を 掛[か]ける', VerbClass.ICHIDAN, '電話[でんわ]が 掛[か]けられる'),
    ('食[た]べる', VerbClass.ICHIDAN, '食[た]べられる'),
    ('起[お]きる', VerbClass.ICHIDAN, '起[お]きられる'),
    ('開[あ]ける', VerbClass.ICHIDAN, '開[あ]けられる'),
    ('借[か]りる', VerbClass.ICHIDAN, '借[か]りられる'),
    # no kanji
    ('くる', VerbClass.IRREGULAR, 'こられる'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこられる'),
    ('いく', VerbClass.GODAN, 'いける'),
    ('かく', VerbClass.GODAN, 'かける'),
    ('あそぶ', VerbClass.GODAN, 'あそべる'),
    ('たつ', VerbClass.GODAN, 'たてる'),
    ('よむ', VerbClass.GODAN, 'よめる'),
    ('かう', VerbClass.GODAN, 'かえる'),
    ('はなす', VerbClass.GODAN, 'はなせる'),
    ('およぐ', VerbClass.GODAN, 'およげる'),
    ('たべる', VerbClass.ICHIDAN, 'たべられる'),
    ('おきる', VerbClass.ICHIDAN, 'おきられる'),
    ('あける', VerbClass.ICHIDAN, 'あけられる'),
    ('かりる', VerbClass.ICHIDAN, 'かりられる'),
    # no furigana
    ('来る', VerbClass.IRREGULAR, '来[こ]られる'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]られる'),
    ('行く', VerbClass.GODAN, '行ける'),
    ('書く', VerbClass.GODAN, '書ける'),
    ('遊ぶ', VerbClass.GODAN, '遊べる'),
    ('立つ', VerbClass.GODAN, '立てる'),
    ('読む', VerbClass.GODAN, '読める'),
    ('買う', VerbClass.GODAN, '買える'),
    ('話す', VerbClass.GODAN, '話せる'),
    ('泳ぐ', VerbClass.GODAN, '泳げる'),
    ('食べる', VerbClass.ICHIDAN, '食べられる'),
    ('起きる', VerbClass.ICHIDAN, '起きられる'),
    ('開ける', VerbClass.ICHIDAN, '開けられる'),
    ('借りる', VerbClass.ICHIDAN, '借りられる')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", plain_nonpast_positive_potential_data)
def test_plain_nonpast_positive_potential(dict_form, verb_class, reference):
    """test the Plain Non-Past Potential conjugation"""
    # Note the VerbClass isn't actually used for this function, but we have the
    # parameter to keep consistency with the other conjugation functions
    result = plain_nonpast_positive_potential(dict_form, verb_class)
    assert result == reference

plain_nonpast_negative_potential_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]られない'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]られない'),
    ('する', VerbClass.IRREGULAR, 'できない'),
    ('ある', VerbClass.GODAN, 'あれない'),
    ('人気[にんき]がある', VerbClass.GODAN, '人気[にんき]があれない'),
    ('行[い]く', VerbClass.GODAN, '行[い]けない'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツができない'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]めない'),
    ('買[か]う', VerbClass.GODAN, '買[か]えない'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]せない'),
    # no kanji
    ('くる', VerbClass.IRREGULAR, 'こられない'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこられない'),
    ('にんきがある', VerbClass.GODAN, 'にんきがあれない'),
    ('いく', VerbClass.GODAN, 'いけない'),
    ('よむ', VerbClass.GODAN, 'よめない'),
    ('かう', VerbClass.GODAN, 'かえない'),
    ('はなす', VerbClass.GODAN, 'はなせない'),
    # no furigana
    ('来る', VerbClass.IRREGULAR, '来[こ]られない'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]られない'),
    ('人気がある', VerbClass.GODAN, '人気があれない'),
    ('行く', VerbClass.GODAN, '行けない'),
    ('読む', VerbClass.GODAN, '読めない'),
    ('買う', VerbClass.GODAN, '買えない'),
    ('話す', VerbClass.GODAN, '話せない')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", plain_nonpast_negative_potential_data)
def test_plain_nonpast_negative_potential(dict_form, verb_class, reference):
    """test the Plain Non-Past Negative Potential conjugation"""
    result = plain_nonpast_negative_potential(dict_form, verb_class)
    assert result == reference

plain_past_positive_potential_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]られた'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]られた'),
    ('する', VerbClass.IRREGULAR, 'できた'),
    ('行[い]く', VerbClass.GODAN, '行[い]けた'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツができた'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]めた'),
    ('買[か]う', VerbClass.GODAN, '買[か]えた'),
    ('泳[およ]ぐ', VerbClass.GODAN, '泳[およ]げた'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]せた'),
    ('切[き]る', VerbClass.GODAN, '切[き]れた'),
    # no kanji
    ('くる', VerbClass.IRREGULAR, 'こられた'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこられた'),
    ('いく', VerbClass.GODAN, 'いけた'),
    ('よむ', VerbClass.GODAN, 'よめた'),
    ('かう', VerbClass.GODAN, 'かえた'),
    ('およぐ', VerbClass.GODAN, 'およげた'),
    ('はなす', VerbClass.GODAN, 'はなせた'),
    ('きる', VerbClass.GODAN, 'きれた'),
    # no furigana
    ('来る', VerbClass.IRREGULAR, '来[こ]られた'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]られた'),
    ('行く', VerbClass.GODAN, '行けた'),
    ('読む', VerbClass.GODAN, '読めた'),
    ('買う', VerbClass.GODAN, '買えた'),
    ('泳ぐ', VerbClass.GODAN, '泳げた'),
    ('話す', VerbClass.GODAN, '話せた'),
    ('切る', VerbClass.GODAN, '切れた')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", plain_past_positive_potential_data)
def test_plain_past_positive_potential(dict_form, verb_class, reference):
    """test the Plain Past Potenial conjugation"""
    result = plain_past_positive_potential(dict_form, verb_class)
    assert result == reference

plain_past_negative_potential_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]られなかった'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]られなかった'),
    ('する', VerbClass.IRREGULAR, 'できなかった'),
    ('行[い]く', VerbClass.GODAN, '行[い]けなかった'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツができなかった'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]めなかった'),
    ('買[か]う', VerbClass.GODAN, '買[か]えなかった'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]せなかった'),
    # no kanji
    ('くる', VerbClass.IRREGULAR, 'こられなかった'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこられなかった'),
    ('いく', VerbClass.GODAN, 'いけなかった'),
    ('よむ', VerbClass.GODAN, 'よめなかった'),
    ('かう', VerbClass.GODAN, 'かえなかった'),
    ('はなす', VerbClass.GODAN, 'はなせなかった'),
    # no furigana
    ('来る', VerbClass.IRREGULAR, '来[こ]られなかった'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]られなかった'),
    ('行く', VerbClass.GODAN, '行けなかった'),
    ('読む', VerbClass.GODAN, '読めなかった'),
    ('買う', VerbClass.GODAN, '買えなかった'),
    ('話す', VerbClass.GODAN, '話せなかった')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", plain_past_negative_potential_data)
def test_plain_past_negative_potential(dict_form, verb_class, reference):
    """test the Plain Past Negative Potential conjugation"""
    result = plain_past_negative_potential(dict_form, verb_class)
    assert result == reference