import pytest

from anki_jpn.verbs import (
    VerbClass,
    Formality,
    Polarity,
    Form,
    generate_forms,
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
    ('話[はな]す', VerbClass.GODAN, '話[はな]します')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", polite_nonpast_positive_data)
def test_polite_nonpast_positive(dict_form, verb_class, reference):
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
    ('話[はな]す', VerbClass.GODAN, '話[はな]しません')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", polite_nonpast_negative_data)
def test_polite_nonpast_negative(dict_form, verb_class, reference):
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
    ('話[はな]す', VerbClass.GODAN, '話[はな]しました')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", polite_past_positive_data)
def test_polite_past_positive(dict_form, verb_class, reference):
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
    ('話[はな]す', VerbClass.GODAN, '話[はな]しませんでした')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", polite_past_negative_data)
def test_polite_past_negative(dict_form, verb_class, reference):
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
    ('話[はな]す', VerbClass.GODAN, '話[はな]しましょう')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", polite_volitional_data)
def test_polite_volitional(dict_form, verb_class, reference):
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
    ('借[か]りる', VerbClass.ICHIDAN, '借[か]りて')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", te_data)
def test_te(dict_form, verb_class, reference):
    result = te(dict_form, verb_class)
    assert result == reference

# Plain forms
plain_nonpast_positive_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[く]る'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[く]る'),
    ('する', VerbClass.IRREGULAR, 'する'),
    ('行[い]く', VerbClass.GODAN, '行[い]く'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをする'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]む'),
    ('買[か]う', VerbClass.GODAN, '買[か]う'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]す')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", plain_nonpast_positive_data)
def test_plain_nonpast_positive(dict_form, verb_class, reference):
    result = plain_nonpast_positive(dict_form, verb_class)
    assert result == reference

plain_nonpast_negative_data = [
    ('来[く]る', VerbClass.IRREGULAR, '来[こ]ない'),
    ('連[つ]れて 来[く]る', VerbClass.IRREGULAR, '連[つ]れて 来[こ]ない'),
    ('する', VerbClass.IRREGULAR, 'しない'),
    ('ある', VerbClass.IRREGULAR, 'ない'),
    ('行[い]く', VerbClass.GODAN, '行[い]かない'),
    ('スポーツをする', VerbClass.IRREGULAR, 'スポーツをしない'),
    ('読[よ]む', VerbClass.GODAN, '読[よ]まない'),
    ('買[か]う', VerbClass.GODAN, '買[か]わない'),
    ('話[はな]す', VerbClass.GODAN, '話[はな]さない')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", plain_nonpast_negative_data)
def test_plain_nonpast_negative(dict_form, verb_class, reference):
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
    ('話[はな]す', VerbClass.GODAN, '話[はな]した')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", plain_past_positive_data)
def test_plain_past_positive(dict_form, verb_class, reference):
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
    ('話[はな]す', VerbClass.GODAN, '話[はな]さなかった')
]
@pytest.mark.parametrize("dict_form, verb_class, reference", plain_past_negative_data)
def test_plain_past_negative(dict_form, verb_class, reference):
    result = plain_past_negative(dict_form, verb_class)
    assert result == reference

generate_forms_data = [
    ('来[く]る', VerbClass.IRREGULAR, [
        # Polite forms
        ['来[き]ます', Form.NON_PAST, Formality.POLITE, Polarity.POS],
        ['来[き]ません', Form.NON_PAST, Formality.POLITE, Polarity.NEG],
        ['来[き]ました', Form.PAST, Formality.POLITE, Polarity.POS],
        ['来[き]ませんでした', Form.PAST, Formality.POLITE, Polarity.NEG],
        ['来[き]ましょう', Form.VOLITIONAL, Formality.POLITE, None],
        # Plain forms
        ['来[く]る', Form.NON_PAST, Formality.POLITE, Polarity.POS],
        ['来[こ]ない', Form.NON_PAST, Formality.POLITE, Polarity.NEG],
        ['来[き]た', Form.PAST, Formality.POLITE, Polarity.POS],
        ['来[こ]なかった', Form.PAST, Formality.POLITE, Polarity.NEG],
        # formality-constant
        ['来[き]て', Form.TE, None, None],
    ]),
    ('食[た]べる', VerbClass.ICHIDAN, [
        # Polite forms
        ['食[た]べます', Form.NON_PAST, Formality.POLITE, Polarity.POS],
        ['食[た]べません', Form.NON_PAST, Formality.POLITE, Polarity.NEG],
        ['食[た]べました', Form.PAST, Formality.POLITE, Polarity.POS],
        ['食[た]べませんでした', Form.PAST, Formality.POLITE, Polarity.NEG],
        ['食[た]べましょう', Form.VOLITIONAL, Formality.POLITE, None],
        # Plain forms
        ['食[た]べる', Form.NON_PAST, Formality.POLITE, Polarity.POS],
        ['食[た]べない', Form.NON_PAST, Formality.POLITE, Polarity.NEG],
        ['食[た]べた', Form.PAST, Formality.POLITE, Polarity.POS],
        ['食[た]べなかった', Form.PAST, Formality.POLITE, Polarity.NEG],
        # formality-constant
        ['食[た]べて', Form.TE, None, None],
    ]),
    ('切[き]る', VerbClass.GODAN, [
        # Polite forms
        ['切[き]ります', Form.NON_PAST, Formality.POLITE, Polarity.POS],
        ['切[き]りません', Form.NON_PAST, Formality.POLITE, Polarity.NEG],
        ['切[き]りました', Form.PAST, Formality.POLITE, Polarity.POS],
        ['切[き]りませんでした', Form.PAST, Formality.POLITE, Polarity.NEG],
        ['切[き]りましょう', Form.VOLITIONAL, Formality.POLITE, None],
        # Plain forms
        ['切[き]る', Form.NON_PAST, Formality.POLITE, Polarity.POS],
        ['切[き]らない', Form.NON_PAST, Formality.POLITE, Polarity.NEG],
        ['切[き]った', Form.PAST, Formality.POLITE, Polarity.POS],
        ['切[き]らなかった', Form.PAST, Formality.POLITE, Polarity.NEG],
        # formality-constant
        ['切[き]って', Form.TE, None, None],
    ])
]
@pytest.mark.parametrize("dict_form, verb_class, reference", generate_forms_data)
def test_generate_forms(dict_form, verb_class, reference):
    forms = generate_forms(dict_form, verb_class)
    assert forms == reference