"""Unit tests for the verb conjugation functions"""
import pytest
from anki_jpn.enums import (
    VerbClass,
    Formality,
    Form,
)
from anki_jpn.verbs import (
    generate_verb_forms,
    polite_nonpast_positive,
    polite_nonpast_negative,
    polite_past_positive,
    polite_past_negative,
    polite_volitional,
    te,
    plain_nonpast_positive,
    plain_nonpast_negative,
    plain_past_positive,
    plain_past_negative
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
    ('はなす', VerbClass.GODAN, 'はなします')
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
    ('はなす', VerbClass.GODAN, 'はなしません')
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
    ('はなす', VerbClass.GODAN, 'はなしました')
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
    ('はなす', VerbClass.GODAN, 'はなしませんでした')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", polite_past_negative_data)
def test_polite_past_negative(dict_form, verb_class, reference):
    """test the Polite Past Negative conjugation"""
    result = polite_past_negative(dict_form, verb_class)
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
    ('はなす', VerbClass.GODAN, 'はなしましょう')
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
    ('かりる', VerbClass.ICHIDAN, 'かりて')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", te_data)
def test_te(dict_form, verb_class, reference):
    """test the Te conjugation"""
    result = te(dict_form, verb_class)
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
    ('きる', 'きる')
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
    ('はなす', VerbClass.GODAN, 'はなさない')
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
    ('きる', VerbClass.GODAN, 'きった')
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
    ('はなす', VerbClass.GODAN, 'はなさなかった')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", plain_past_negative_data)
def test_plain_past_negative(dict_form, verb_class, reference):
    """test the Plain Past Negative conjugation"""
    result = plain_past_negative(dict_form, verb_class)
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
    ('汚[きたな]い', VerbClass.GENERAL, [])
]
@pytest.mark.parametrize("dict_form, verb_class, reference", generate_verb_forms_data)
def test_generate_verb_forms(dict_form, verb_class, reference):
    """test the generate_verb_forms() method"""
    forms = generate_verb_forms(dict_form, verb_class)
    assert forms == reference
    general_forms = generate_verb_forms(dict_form, VerbClass.GENERAL)
    assert general_forms == reference
