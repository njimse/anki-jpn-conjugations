"""Unit tests for the verb conjugation functions"""
import pytest
from japanese_conjugation.enums import (
    VerbClass,
    Formality,
    Form,
)
from japanese_conjugation.verbs import (
    generate_verb_forms,
    polite_nonpast_positive,
    polite_nonpast_negative,
    polite_past_positive,
    polite_past_negative,
    polite_nonpast_positive_potential,
    polite_nonpast_negative_potential,
    polite_past_positive_potential,
    polite_past_negative_potential,
    polite_volitional,
    te,
    te_potential,
    plain_nonpast_positive,
    plain_nonpast_negative,
    plain_past_positive,
    plain_past_negative,
    plain_volitional,
    plain_nonpast_positive_potential,
    plain_nonpast_negative_potential,
    plain_past_positive_potential,
    plain_past_negative_potential
)

polite_nonpast_positive_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[き]ます'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[き]ます'),
    ('する', VerbClass.IRREGULAR, 'します'),
    ('行[い]く', VerbClass.GODAN, '行[い]きます'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをします'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]みます'),
    ('買[か]う', VerbClass.GODAN, '買[か]います'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]します'),
    # No kanji
    ('くる', VerbClass.IRREGULAR, 'きます'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてきます'),
    ('いく', VerbClass.GODAN, 'いきます'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをします'),
    ('よむ', VerbClass.GODAN, 'よみます'),
    ('かう', VerbClass.GODAN, 'かいます'),
    ('はなす', VerbClass.GODAN, 'はなします'),
    # no furigana
    ('来る', VerbClass.IRREGULAR, '来[き]ます'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[き]ます'),
    ('行く', VerbClass.GODAN, '行きます'),
    ('読む', VerbClass.GODAN, '読みます'),
    ('買う', VerbClass.GODAN, '買います'),
    ('話す', VerbClass.GODAN, '話します'),
]
@pytest.mark.parametrize("dict_form, verb_class, reference", polite_nonpast_positive_data)
def test_polite_nonpast_positive(dict_form, verb_class, reference):
    """test the Polite Non-Past conjugation"""
    result = polite_nonpast_positive(dict_form, verb_class)
    assert result == reference

polite_nonpast_negative_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[き]ません'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[き]ません'),
    ('する', VerbClass.IRREGULAR, 'しません'),
    ('行[い]く', VerbClass.GODAN, '行[い]きません'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをしません'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]みません'),
    ('買[か]う', VerbClass.GODAN, '買[か]いません'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]しません'),
    # no kanji
    ('くる', VerbClass.IRREGULAR, 'きません'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてきません'),
    ('する', VerbClass.IRREGULAR, 'しません'),
    ('いく', VerbClass.GODAN, 'いきません'),
    ('よむ', VerbClass.GODAN, 'よみません'),
    ('かう', VerbClass.GODAN, 'かいません'),
    ('はなす', VerbClass.GODAN, 'はなしません'),
    # no furigana
    ('来る', VerbClass.IRREGULAR, '来[き]ません'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[き]ません'),
    ('行く', VerbClass.GODAN, '行きません'),
    ('読む', VerbClass.GODAN, '読みません'),
    ('買う', VerbClass.GODAN, '買いません'),
    ('話す', VerbClass.GODAN, '話しません'),
]
@pytest.mark.parametrize("dict_form, verb_class, reference", polite_nonpast_negative_data)
def test_polite_nonpast_negative(dict_form, verb_class, reference):
    """test the Polite Non-Past Negative conjugation"""
    result = polite_nonpast_negative(dict_form, verb_class)
    assert result == reference

polite_past_positive_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[き]ました'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[き]ました'),
    ('する', VerbClass.IRREGULAR, 'しました'),
    ('行[い]く', VerbClass.GODAN, '行[い]きました'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをしました'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]みました'),
    ('買[か]う', VerbClass.GODAN, '買[か]いました'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]しました'),
    # no kanji
    ('くる', VerbClass.IRREGULAR, 'きました'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてきました'),
    ('いく', VerbClass.GODAN, 'いきました'),
    ('よむ', VerbClass.GODAN, 'よみました'),
    ('かう', VerbClass.GODAN, 'かいました'),
    ('はなす', VerbClass.GODAN, 'はなしました'),
    # no furigana
    ('来る', VerbClass.IRREGULAR, '来[き]ました'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[き]ました'),
    ('行く', VerbClass.GODAN, '行きました'),
    ('読む', VerbClass.GODAN, '読みました'),
    ('買う', VerbClass.GODAN, '買いました'),
    ('話す', VerbClass.GODAN, '話しました'),
]
@pytest.mark.parametrize("dict_form, verb_class, reference", polite_past_positive_data)
def test_polite_past_positive(dict_form, verb_class, reference):
    """test the Polite Past conjugation"""
    result = polite_past_positive(dict_form, verb_class)
    assert result == reference

polite_past_negative_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[き]ませんでした'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[き]ませんでした'),
    ('する', VerbClass.IRREGULAR, 'しませんでした'),
    ('行[い]く', VerbClass.GODAN, '行[い]きませんでした'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをしませんでした'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]みませんでした'),
    ('買[か]う', VerbClass.GODAN, '買[か]いませんでした'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]しませんでした'),
    # no kanji
    ('くる', VerbClass.IRREGULAR, 'きませんでした'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてきませんでした'),
    ('いく', VerbClass.GODAN, 'いきませんでした'),
    ('よむ', VerbClass.GODAN, 'よみませんでした'),
    ('かう', VerbClass.GODAN, 'かいませんでした'),
    ('はなす', VerbClass.GODAN, 'はなしませんでした'),
    # no furigana
    ('来る', VerbClass.IRREGULAR, '来[き]ませんでした'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[き]ませんでした'),
    ('行く', VerbClass.GODAN, '行きませんでした'),
    ('読む', VerbClass.GODAN, '読みませんでした'),
    ('買う', VerbClass.GODAN, '買いませんでした'),
    ('話す', VerbClass.GODAN, '話しませんでした')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", polite_past_negative_data)
def test_polite_past_negative(dict_form, verb_class, reference):
    """test the Polite Past Negative conjugation"""
    result = polite_past_negative(dict_form, verb_class)
    assert result == reference

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

polite_volitional_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[き]ましょう'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[き]ましょう'),
    ('する', VerbClass.IRREGULAR, 'しましょう'),
    ('行[い]く', VerbClass.GODAN, '行[い]きましょう'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをしましょう'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]みましょう'),
    ('買[か]う', VerbClass.GODAN, '買[か]いましょう'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]しましょう'),
    # no kanji
    ('くる', VerbClass.IRREGULAR, 'きましょう'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてきましょう'),
    ('いく', VerbClass.GODAN, 'いきましょう'),
    ('よむ', VerbClass.GODAN, 'よみましょう'),
    ('かう', VerbClass.GODAN, 'かいましょう'),
    ('はなす', VerbClass.GODAN, 'はなしましょう'),
    # no furigana
    ('来る', VerbClass.IRREGULAR, '来[き]ましょう'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[き]ましょう'),
    ('行く', VerbClass.GODAN, '行きましょう'),
    ('読む', VerbClass.GODAN, '読みましょう'),
    ('買う', VerbClass.GODAN, '買いましょう'),
    ('話す', VerbClass.GODAN, '話しましょう')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", polite_volitional_data)
def test_polite_volitional(dict_form, verb_class, reference):
    """test the Polite Volitional conjugation"""
    result = polite_volitional(dict_form, verb_class)
    assert result == reference

te_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[き]て'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[き]て'),
    ('する', VerbClass.IRREGULAR, 'して'),
    ('行[い]く', VerbClass.GODAN, '行[い]って'),
    ('書[か]く', VerbClass.GODAN, '書[か]いて'),
    ('遊[あそ]ぶ', VerbClass.GODAN, '遊[あそ]んで'),
    ('立[た]つ', VerbClass.GODAN, '立[た]って'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをして'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]んで'),
    ('買[か]う', VerbClass.GODAN, '買[か]って'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]して'),
    ('泳[およ]ぐ', VerbClass.GODAN, '泳[およ]いで'),
    ('食[た]べる', VerbClass.ICHIDAN, '食[た]べて'),
    ('起[お]きる', VerbClass.ICHIDAN, '起[お]きて'),
    ('開[あ]ける', VerbClass.ICHIDAN, '開[あ]けて'),
    ('借[か]りる', VerbClass.ICHIDAN, '借[か]りて'),
    # no kanji
    ('くる', VerbClass.IRREGULAR, 'きて'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてきて'),
    ('いく', VerbClass.GODAN, 'いって'),
    ('かく', VerbClass.GODAN, 'かいて'),
    ('あそぶ', VerbClass.GODAN, 'あそんで'),
    ('たつ', VerbClass.GODAN, 'たって'),
    ('よむ', VerbClass.GODAN, 'よんで'),
    ('かう', VerbClass.GODAN, 'かって'),
    ('はなす', VerbClass.GODAN, 'はなして'),
    ('およぐ', VerbClass.GODAN, 'およいで'),
    ('たべる', VerbClass.ICHIDAN, 'たべて'),
    ('おきる', VerbClass.ICHIDAN, 'おきて'),
    ('あける', VerbClass.ICHIDAN, 'あけて'),
    ('かりる', VerbClass.ICHIDAN, 'かりて'),
    # no furigana
    ('来る', VerbClass.IRREGULAR, '来[き]て'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[き]て'),
    ('行く', VerbClass.GODAN, '行って'),
    ('書く', VerbClass.GODAN, '書いて'),
    ('遊ぶ', VerbClass.GODAN, '遊んで'),
    ('立つ', VerbClass.GODAN, '立って'),
    ('読む', VerbClass.GODAN, '読んで'),
    ('買う', VerbClass.GODAN, '買って'),
    ('話す', VerbClass.GODAN, '話して'),
    ('泳ぐ', VerbClass.GODAN, '泳いで'),
    ('食べる', VerbClass.ICHIDAN, '食べて'),
    ('起きる', VerbClass.ICHIDAN, '起きて'),
    ('開ける', VerbClass.ICHIDAN, '開けて'),
    ('借りる', VerbClass.ICHIDAN, '借りて')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", te_data)
def test_te(dict_form, verb_class, reference):
    """test the Te conjugation"""
    result = te(dict_form, verb_class)
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

# Plain forms
plain_nonpast_positive_data = [
    ('来[く]る', '来[く]る'),
    ('連[つ]れて 来[く]る', '連[つ]れて 来[く]る'),
    ('する', 'する'),
    ('行[い]く', '行[い]く'),
    ('スポーツをする', 'スポーツをする'),
    ('読[よ]む', '読[よ]む'),
    ('買[か]う', '買[か]う'),
    ('話[はな]す', '話[はな]す'),
    ('切[き]る', '切[き]る'),
    # no kanji
    ('くる', 'くる'),
    ('つれてくる', 'つれてくる'),
    ('いく', 'いく'),
    ('よむ', 'よむ'),
    ('かう', 'かう'),
    ('はなす', 'はなす'),
    ('きる', 'きる'),
    # no furigana
    ('来る', '来[く]る'),
    ('連れて来る', '連れて 来[く]る'),
    ('行く', '行く'),
    ('読む', '読む'),
    ('買う', '買う'),
    ('話す', '話す'),
    ('切る', '切る')
]
@pytest.mark.parametrize("dict_form, reference", plain_nonpast_positive_data)
def test_plain_nonpast_positive(dict_form, reference):
    """test the Plain Non-Past conjugation"""
    # Note the VerbClass isn't actually used for this function, but we have the
    # parameter to keep consistency with the other conjugation functions
    result = plain_nonpast_positive(dict_form, VerbClass)
    assert result == reference

plain_nonpast_negative_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]ない'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]ない'),
    ('する', VerbClass.IRREGULAR, 'しない'),
    ('ある', VerbClass.GODAN, 'ない'),
    ('人気[にんき]がある', VerbClass.GODAN, '人気[にんき]がない'),
    ('行[い]く', VerbClass.GODAN, '行[い]かない'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをしない'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]まない'),
    ('買[か]う', VerbClass.GODAN, '買[か]わない'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]さない'),
    # no kanji
    ('くる', VerbClass.IRREGULAR, 'こない'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこない'),
    ('にんきがある', VerbClass.GODAN, 'にんきがない'),
    ('いく', VerbClass.GODAN, 'いかない'),
    ('よむ', VerbClass.GODAN, 'よまない'),
    ('かう', VerbClass.GODAN, 'かわない'),
    ('はなす', VerbClass.GODAN, 'はなさない'),
    # no furigana
    ('来る', VerbClass.IRREGULAR, '来[こ]ない'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]ない'),
    ('人気がある', VerbClass.GODAN, '人気がない'),
    ('行く', VerbClass.GODAN, '行かない'),
    ('読む', VerbClass.GODAN, '読まない'),
    ('買う', VerbClass.GODAN, '買わない'),
    ('話す', VerbClass.GODAN, '話さない')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", plain_nonpast_negative_data)
def test_plain_nonpast_negative(dict_form, verb_class, reference):
    """test the Plain Non-Past Negative conjugation"""
    result = plain_nonpast_negative(dict_form, verb_class)
    assert result == reference

plain_past_positive_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[き]た'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[き]た'),
    ('する', VerbClass.IRREGULAR, 'した'),
    ('行[い]く', VerbClass.GODAN, '行[い]った'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをした'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]んだ'),
    ('買[か]う', VerbClass.GODAN, '買[か]った'),
    ('泳[およ]ぐ', VerbClass.GODAN, '泳[およ]いだ'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]した'),
    ('切[き]る', VerbClass.GODAN, '切[き]った'),
    # no kanji
    ('くる', VerbClass.IRREGULAR, 'きた'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてきた'),
    ('いく', VerbClass.GODAN, 'いった'),
    ('よむ', VerbClass.GODAN, 'よんだ'),
    ('かう', VerbClass.GODAN, 'かった'),
    ('およぐ', VerbClass.GODAN, 'およいだ'),
    ('はなす', VerbClass.GODAN, 'はなした'),
    ('きる', VerbClass.GODAN, 'きった'),
    # no furigana
    ('来る', VerbClass.IRREGULAR, '来[き]た'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[き]た'),
    ('行く', VerbClass.GODAN, '行った'),
    ('読む', VerbClass.GODAN, '読んだ'),
    ('買う', VerbClass.GODAN, '買った'),
    ('泳ぐ', VerbClass.GODAN, '泳いだ'),
    ('話す', VerbClass.GODAN, '話した'),
    ('切る', VerbClass.GODAN, '切った')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", plain_past_positive_data)
def test_plain_past_positive(dict_form, verb_class, reference):
    """test the Plain Past conjugation"""
    result = plain_past_positive(dict_form, verb_class)
    assert result == reference

plain_past_negative_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]なかった'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]なかった'),
    ('する', VerbClass.IRREGULAR, 'しなかった'),
    ('行[い]く', VerbClass.GODAN, '行[い]かなかった'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをしなかった'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]まなかった'),
    ('買[か]う', VerbClass.GODAN, '買[か]わなかった'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]さなかった'),
    # no kanji
    ('くる', VerbClass.IRREGULAR, 'こなかった'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこなかった'),
    ('いく', VerbClass.GODAN, 'いかなかった'),
    ('よむ', VerbClass.GODAN, 'よまなかった'),
    ('かう', VerbClass.GODAN, 'かわなかった'),
    ('はなす', VerbClass.GODAN, 'はなさなかった'),
    # no furigana
    ('来る', VerbClass.IRREGULAR, '来[こ]なかった'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]なかった'),
    ('行く', VerbClass.GODAN, '行かなかった'),
    ('読む', VerbClass.GODAN, '読まなかった'),
    ('買う', VerbClass.GODAN, '買わなかった'),
    ('話す', VerbClass.GODAN, '話さなかった')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", plain_past_negative_data)
def test_plain_past_negative(dict_form, verb_class, reference):
    """test the Plain Past Negative conjugation"""
    result = plain_past_negative(dict_form, verb_class)
    assert result == reference

plain_volitional_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]よう'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]よう'),
    ('する', VerbClass.IRREGULAR, 'しよう'),
    ('行[い]く', VerbClass.GODAN, '行[い]こう'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをしよう'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]もう'),
    ('買[か]う', VerbClass.GODAN, '買[か]おう'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]そう'),
    # no kanji
    ('くる', VerbClass.IRREGULAR, 'こよう'),
    ('つれてくる', VerbClass.IRREGULAR, 'つれてこよう'),
    ('いく', VerbClass.GODAN, 'いこう'),
    ('よむ', VerbClass.GODAN, 'よもう'),
    ('かう', VerbClass.GODAN, 'かおう'),
    ('はなす', VerbClass.GODAN, 'はなそう'),
    # no furigana
    ('来る', VerbClass.IRREGULAR, '来[こ]よう'),
    ('連れて来る', VerbClass.IRREGULAR, '連れて 来[こ]よう'),
    ('行く', VerbClass.GODAN, '行こう'),
    ('読む', VerbClass.GODAN, '読もう'),
    ('買う', VerbClass.GODAN, '買おう'),
    ('話す', VerbClass.GODAN, '話そう')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", plain_volitional_data)
def test_plain_volitional(dict_form, verb_class, reference):
    """test the Plain Past Negative conjugation"""
    result = plain_volitional(dict_form, verb_class)
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

generate_verb_forms_data = [
    ('来[く]る', VerbClass.IRREGULAR, [
        # Polite forms
        ['来[き]ます', Form.NON_PAST, Formality.POLITE],
        ['来[き]ません', Form.NON_PAST_NEG, Formality.POLITE],
        ['来[き]ました', Form.PAST, Formality.POLITE],
        ['来[き]ませんでした', Form.PAST_NEG, Formality.POLITE],
        ['来[き]ましょう', Form.VOLITIONAL, Formality.POLITE],
        # Plain forms
        ['来[く]る', Form.NON_PAST, Formality.PLAIN],
        ['来[こ]ない', Form.NON_PAST_NEG, Formality.PLAIN],
        ['来[き]た', Form.PAST, Formality.PLAIN],
        ['来[こ]なかった', Form.PAST_NEG, Formality.PLAIN],
        # formality-constant
        ['来[き]て', Form.TE, None],
        # Polite Potential forms
        ['来[こ]られます', Form.POTENTIAL_NON_PAST, Formality.POLITE],
        ['来[こ]られません', Form.POTENTIAL_NON_PAST_NEG, Formality.POLITE],
        ['来[こ]られました', Form.POTENTIAL_PAST, Formality.POLITE],
        ['来[こ]られませんでした', Form.POTENTIAL_PAST_NEG, Formality.POLITE],
        # Plain Potential forms
        ['来[こ]られる', Form.POTENTIAL_NON_PAST, Formality.PLAIN],
        ['来[こ]られない', Form.POTENTIAL_NON_PAST_NEG, Formality.PLAIN],
        ['来[こ]られた', Form.POTENTIAL_PAST, Formality.PLAIN],
        ['来[こ]られなかった', Form.POTENTIAL_PAST_NEG, Formality.PLAIN],
        # formality-constant Potential
        ['来[こ]られて', Form.POTENTIAL_TE, None],
        # tai forms
        # Polite forms
        ['来[き]たいです', Form.TAI_NON_PAST, Formality.POLITE],
        ['来[き]たくないです', Form.TAI_NON_PAST_NEG, Formality.POLITE],
        ['来[き]たかったです', Form.TAI_PAST, Formality.POLITE],
        ['来[き]たくなかったです', Form.TAI_PAST_NEG, Formality.POLITE],
        # Plain forms
        ['来[き]たい', Form.TAI_NON_PAST, Formality.PLAIN],
        ['来[き]たくない', Form.TAI_NON_PAST_NEG, Formality.PLAIN],
        ['来[き]たかった', Form.TAI_PAST, Formality.PLAIN],
        ['来[き]たくなかった', Form.TAI_PAST_NEG, Formality.PLAIN],
        # formality-constant
        ['来[き]たくて', Form.TAI_TE, None],
    ]),
    ('食[た]べる', VerbClass.ICHIDAN, [
        # Polite forms
        ['食[た]べます', Form.NON_PAST, Formality.POLITE],
        ['食[た]べません', Form.NON_PAST_NEG, Formality.POLITE],
        ['食[た]べました', Form.PAST, Formality.POLITE],
        ['食[た]べませんでした', Form.PAST_NEG, Formality.POLITE],
        ['食[た]べましょう', Form.VOLITIONAL, Formality.POLITE],
        # Plain forms
        ['食[た]べる', Form.NON_PAST, Formality.PLAIN],
        ['食[た]べない', Form.NON_PAST_NEG, Formality.PLAIN],
        ['食[た]べた', Form.PAST, Formality.PLAIN],
        ['食[た]べなかった', Form.PAST_NEG, Formality.PLAIN],
        # formality-constant
        ['食[た]べて', Form.TE, None],

        # Potential forms
        # Polite forms
        ['食[た]べられます', Form.POTENTIAL_NON_PAST, Formality.POLITE],
        ['食[た]べられません', Form.POTENTIAL_NON_PAST_NEG, Formality.POLITE],
        ['食[た]べられました', Form.POTENTIAL_PAST, Formality.POLITE],
        ['食[た]べられませんでした', Form.POTENTIAL_PAST_NEG, Formality.POLITE],
        # Plain forms
        ['食[た]べられる', Form.POTENTIAL_NON_PAST, Formality.PLAIN],
        ['食[た]べられない', Form.POTENTIAL_NON_PAST_NEG, Formality.PLAIN],
        ['食[た]べられた', Form.POTENTIAL_PAST, Formality.PLAIN],
        ['食[た]べられなかった', Form.POTENTIAL_PAST_NEG, Formality.PLAIN],
        # formality-constant
        ['食[た]べられて', Form.POTENTIAL_TE, None],

        # tai forms
        # Polite forms
        ['食[た]べたいです', Form.TAI_NON_PAST, Formality.POLITE],
        ['食[た]べたくないです', Form.TAI_NON_PAST_NEG, Formality.POLITE],
        ['食[た]べたかったです', Form.TAI_PAST, Formality.POLITE],
        ['食[た]べたくなかったです', Form.TAI_PAST_NEG, Formality.POLITE],
        # Plain forms
        ['食[た]べたい', Form.TAI_NON_PAST, Formality.PLAIN],
        ['食[た]べたくない', Form.TAI_NON_PAST_NEG, Formality.PLAIN],
        ['食[た]べたかった', Form.TAI_PAST, Formality.PLAIN],
        ['食[た]べたくなかった', Form.TAI_PAST_NEG, Formality.PLAIN],
        # formality-constant
        ['食[た]べたくて', Form.TAI_TE, None],
    ]),
    ('切[き]る', VerbClass.GODAN, [
        # Polite forms
        ['切[き]ります', Form.NON_PAST, Formality.POLITE],
        ['切[き]りません', Form.NON_PAST_NEG, Formality.POLITE],
        ['切[き]りました', Form.PAST, Formality.POLITE],
        ['切[き]りませんでした', Form.PAST_NEG, Formality.POLITE],
        ['切[き]りましょう', Form.VOLITIONAL, Formality.POLITE],
        # Plain forms
        ['切[き]る', Form.NON_PAST, Formality.PLAIN],
        ['切[き]らない', Form.NON_PAST_NEG, Formality.PLAIN],
        ['切[き]った', Form.PAST, Formality.PLAIN],
        ['切[き]らなかった', Form.PAST_NEG, Formality.PLAIN],
        # formality-constant
        ['切[き]って', Form.TE, None],

        # Potential forms
        # Polite forms
        ['切[き]れます', Form.POTENTIAL_NON_PAST, Formality.POLITE],
        ['切[き]れません', Form.POTENTIAL_NON_PAST_NEG, Formality.POLITE],
        ['切[き]れました', Form.POTENTIAL_PAST, Formality.POLITE],
        ['切[き]れませんでした', Form.POTENTIAL_PAST_NEG, Formality.POLITE],
        # Plain forms
        ['切[き]れる', Form.POTENTIAL_NON_PAST, Formality.PLAIN],
        ['切[き]れない', Form.POTENTIAL_NON_PAST_NEG, Formality.PLAIN],
        ['切[き]れた', Form.POTENTIAL_PAST, Formality.PLAIN],
        ['切[き]れなかった', Form.POTENTIAL_PAST_NEG, Formality.PLAIN],
        # formality-constant
        ['切[き]れて', Form.POTENTIAL_TE, None],

        # tai forms
        # Polite forms
        ['切[き]りたいです', Form.TAI_NON_PAST, Formality.POLITE],
        ['切[き]りたくないです', Form.TAI_NON_PAST_NEG, Formality.POLITE],
        ['切[き]りたかったです', Form.TAI_PAST, Formality.POLITE],
        ['切[き]りたくなかったです', Form.TAI_PAST_NEG, Formality.POLITE],
        # Plain forms
        ['切[き]りたい', Form.TAI_NON_PAST, Formality.PLAIN],
        ['切[き]りたくない', Form.TAI_NON_PAST_NEG, Formality.PLAIN],
        ['切[き]りたかった', Form.TAI_PAST, Formality.PLAIN],
        ['切[き]りたくなかった', Form.TAI_PAST_NEG, Formality.PLAIN],
        # formality-constant
        ['切[き]りたくて', Form.TAI_TE, None],
    ]),
    ('汚[きたな]い', VerbClass.GENERAL, []),
    ('です', VerbClass.GODAN, [
        # Polite forms pylint: disable=R0801
        ['です', Form.NON_PAST, Formality.POLITE],
        ['じゃないです', Form.NON_PAST_NEG, Formality.POLITE],
        ['でした', Form.PAST, Formality.POLITE],
        ['ませんでした', Form.PAST_NEG, Formality.POLITE],
        ['でしょう', Form.VOLITIONAL, Formality.POLITE],
        # Plain forms
        ['だ', Form.NON_PAST, Formality.PLAIN],
        ['じゃない', Form.NON_PAST_NEG, Formality.PLAIN],
        ['だった', Form.PAST, Formality.PLAIN],
        ['なかった', Form.PAST_NEG, Formality.PLAIN],
        # formality-constant
        ['で', Form.TE, None],
    ])
]
@pytest.mark.parametrize("dict_form, verb_class, reference", generate_verb_forms_data)
def test_generate_verb_forms(dict_form, verb_class, reference):
    """test the generate_verb_forms() method"""
    forms = generate_verb_forms(dict_form, verb_class)
    assert forms == reference
    general_forms = generate_verb_forms(dict_form, VerbClass.GENERAL)
    assert general_forms == reference
