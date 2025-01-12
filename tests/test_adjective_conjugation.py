"""Unit tests for the adjective conjugation methods"""
import pytest

from anki_jpn.enums import (
    AdjectiveClass,
    Form,
    Formality
)
from anki_jpn.adjectives import (
    generate_adjective_forms,
    polite_nonpast_positive,
    polite_nonpast_negative,
    polite_past_positive,
    polite_past_negative,
    te,
    plain_nonpast_positive,
    plain_nonpast_negative,
    plain_past_positive,
    plain_past_negative,
)

polite_nonpast_positive_data = [
    ('元気な', AdjectiveClass.NA, '元気です'),
    ('元気[げんき]な', AdjectiveClass.NA, '元気[げんき]です'),
    ('暇[ひま]な', AdjectiveClass.NA, '暇[ひま]です'),
    ('暇な', AdjectiveClass.NA, '暇です'),
    ('美味[おい]しい', AdjectiveClass.I, '美味[おい]しいです'),
    ('美味しい', AdjectiveClass.I, '美味しいです'),
    ('早[はや]い', AdjectiveClass.I, '早[はや]いです'),
    ('格好[かっこ]いい', AdjectiveClass.I, '格好[かっこ]いいです')
]
@pytest.mark.parametrize("dict_form, adj_class, reference", polite_nonpast_positive_data)
def test_polite_nonpast_positive(dict_form, adj_class, reference):
    """test the Polite Non-Past conjugation"""
    result = polite_nonpast_positive(dict_form, adj_class)
    assert result == reference

polite_nonpast_negative_data = [
    ('元気な', AdjectiveClass.NA, '元気じゃないです'),
    ('元気[げんき]な', AdjectiveClass.NA, '元気[げんき]じゃないです'),
    ('暇[ひま]な', AdjectiveClass.NA, '暇[ひま]じゃないです'),
    ('暇な', AdjectiveClass.NA, '暇じゃないです'),
    ('美味[おい]しい', AdjectiveClass.I, '美味[おい]しくないです'),
    ('美味しい', AdjectiveClass.I, '美味しくないです'),
    ('早[はや]い', AdjectiveClass.I, '早[はや]くないです'),
    ('格好[かっこ]いい', AdjectiveClass.I, '格好[かっこ]よくないです')
]
@pytest.mark.parametrize("dict_form, adj_class, reference", polite_nonpast_negative_data)
def test_polite_nonpast_negative(dict_form, adj_class, reference):
    """test the Polite Non-Past Negative conjugation"""
    result = polite_nonpast_negative(dict_form, adj_class)
    assert result == reference

polite_past_positive_data = [
    ('元気な', AdjectiveClass.NA, '元気でした'),
    ('元気[げんき]な', AdjectiveClass.NA, '元気[げんき]でした'),
    ('暇[ひま]な', AdjectiveClass.NA, '暇[ひま]でした'),
    ('暇な', AdjectiveClass.NA, '暇でした'),
    ('美味[おい]しい', AdjectiveClass.I, '美味[おい]しかったです'),
    ('美味しい', AdjectiveClass.I, '美味しかったです'),
    ('早[はや]い', AdjectiveClass.I, '早[はや]かったです'),
    ('格好[かっこ]いい', AdjectiveClass.I, '格好[かっこ]よかったです')
]
@pytest.mark.parametrize("dict_form, adj_class, reference", polite_past_positive_data)
def test_polite_past_positive(dict_form, adj_class, reference):
    """test the Polite Past conjugation"""
    result = polite_past_positive(dict_form, adj_class)
    assert result == reference

polite_past_negative_data = [
    ('元気な', AdjectiveClass.NA, '元気じゃなかったです'),
    ('元気[げんき]な', AdjectiveClass.NA, '元気[げんき]じゃなかったです'),
    ('暇[ひま]な', AdjectiveClass.NA, '暇[ひま]じゃなかったです'),
    ('暇な', AdjectiveClass.NA, '暇じゃなかったです'),
    ('美味[おい]しい', AdjectiveClass.I, '美味[おい]しくなかったです'),
    ('美味しい', AdjectiveClass.I, '美味しくなかったです'),
    ('早[はや]い', AdjectiveClass.I, '早[はや]くなかったです'),
    ('格好[かっこ]いい', AdjectiveClass.I, '格好[かっこ]よくなかったです')
]
@pytest.mark.parametrize("dict_form, adj_class, reference", polite_past_negative_data)
def test_polite_past_negative(dict_form, adj_class, reference):
    """test the Polite Past Negative conjugation"""
    result = polite_past_negative(dict_form, adj_class)
    assert result == reference

te_data = [
    ('元気な', AdjectiveClass.NA, '元気で'),
    ('元気[げんき]な', AdjectiveClass.NA, '元気[げんき]で'),
    ('暇[ひま]な', AdjectiveClass.NA, '暇[ひま]で'),
    ('暇な', AdjectiveClass.NA, '暇で'),
    ('美味[おい]しい', AdjectiveClass.I, '美味[おい]しくて'),
    ('美味しい', AdjectiveClass.I, '美味しくて'),
    ('早[はや]い', AdjectiveClass.I, '早[はや]くて'),
    ('格好[かっこ]いい', AdjectiveClass.I, '格好[かっこ]よくて')
]
@pytest.mark.parametrize("dict_form, adj_class, reference", te_data)
def test_te(dict_form, adj_class, reference):
    """test the Te conjugation"""
    result = te(dict_form, adj_class)
    assert result == reference

# Plain forms
plain_nonpast_positive_data = [
    ('元気な', AdjectiveClass.NA, '元気だ'),
    ('元気[げんき]な', AdjectiveClass.NA, '元気[げんき]だ'),
    ('暇[ひま]な', AdjectiveClass.NA, '暇[ひま]だ'),
    ('暇な', AdjectiveClass.NA, '暇だ'),
    ('美味[おい]しい', AdjectiveClass.I, '美味[おい]しい'),
    ('美味しい', AdjectiveClass.I, '美味しい'),
    ('早[はや]い', AdjectiveClass.I, '早[はや]い'),
    ('格好[かっこ]いい', AdjectiveClass.I, '格好[かっこ]いい')
]
@pytest.mark.parametrize("dict_form, adj_class, reference", plain_nonpast_positive_data)
def test_plain_nonpast_positive(dict_form, adj_class, reference):
    """test the Plain Non-Past conjugation"""
    result = plain_nonpast_positive(dict_form, adj_class)
    assert result == reference

plain_nonpast_negative_data = [
    ('元気な', AdjectiveClass.NA, '元気じゃない'),
    ('元気[げんき]な', AdjectiveClass.NA, '元気[げんき]じゃない'),
    ('暇[ひま]な', AdjectiveClass.NA, '暇[ひま]じゃない'),
    ('暇な', AdjectiveClass.NA, '暇じゃない'),
    ('美味[おい]しい', AdjectiveClass.I, '美味[おい]しくない'),
    ('美味しい', AdjectiveClass.I, '美味しくない'),
    ('早[はや]い', AdjectiveClass.I, '早[はや]くない'),
    ('格好[かっこ]いい', AdjectiveClass.I, '格好[かっこ]よくない')
]
@pytest.mark.parametrize("dict_form, adj_class, reference", plain_nonpast_negative_data)
def test_plain_nonpast_negative(dict_form, adj_class, reference):
    """test the Plain Non-Past Negative conjugation"""
    result = plain_nonpast_negative(dict_form, adj_class)
    assert result == reference

plain_past_positive_data = [
    ('元気な', AdjectiveClass.NA, '元気だった'),
    ('元気[げんき]な', AdjectiveClass.NA, '元気[げんき]だった'),
    ('暇[ひま]な', AdjectiveClass.NA, '暇[ひま]だった'),
    ('暇な', AdjectiveClass.NA, '暇だった'),
    ('美味[おい]しい', AdjectiveClass.I, '美味[おい]しかった'),
    ('美味しい', AdjectiveClass.I, '美味しかった'),
    ('早[はや]い', AdjectiveClass.I, '早[はや]かった'),
    ('格好[かっこ]いい', AdjectiveClass.I, '格好[かっこ]よかった')
]
@pytest.mark.parametrize("dict_form, adj_class, reference", plain_past_positive_data)
def test_plain_past_positive(dict_form, adj_class, reference):
    """test the Plain Past conjugation"""
    result = plain_past_positive(dict_form, adj_class)
    assert result == reference

plain_past_negative_data = [
    ('元気な', AdjectiveClass.NA, '元気じゃなかった'),
    ('元気[げんき]な', AdjectiveClass.NA, '元気[げんき]じゃなかった'),
    ('暇[ひま]な', AdjectiveClass.NA, '暇[ひま]じゃなかった'),
    ('暇な', AdjectiveClass.NA, '暇じゃなかった'),
    ('美味[おい]しい', AdjectiveClass.I, '美味[おい]しくなかった'),
    ('美味しい', AdjectiveClass.I, '美味しくなかった'),
    ('早[はや]い', AdjectiveClass.I, '早[はや]くなかった'),
    ('格好[かっこ]いい', AdjectiveClass.I, '格好[かっこ]よくなかった')
]
@pytest.mark.parametrize("dict_form, adj_class, reference", plain_past_negative_data)
def test_plain_past_negative(dict_form, adj_class, reference):
    """test the Plain Past Negative conjugation"""
    result = plain_past_negative(dict_form, adj_class)
    assert result == reference

generate_adjective_forms_data = [
    ('嫌[きら]いな', AdjectiveClass.NA, [
        # Polite forms
        ['嫌[きら]いです', Form.NON_PAST, Formality.POLITE],
        ['嫌[きら]いじゃないです', Form.NON_PAST_NEG, Formality.POLITE],
        ['嫌[きら]いでした', Form.PAST, Formality.POLITE],
        ['嫌[きら]いじゃなかったです', Form.PAST_NEG, Formality.POLITE],
        # Plain forms
        ['嫌[きら]いだ', Form.NON_PAST, Formality.PLAIN],
        ['嫌[きら]いじゃない', Form.NON_PAST_NEG, Formality.PLAIN],
        ['嫌[きら]いだった', Form.PAST, Formality.PLAIN],
        ['嫌[きら]いじゃなかった', Form.PAST_NEG, Formality.PLAIN],
        # formality-constant
        ['嫌[きら]いで', Form.TE, None],
    ]),
    ('嫌[きら]い', AdjectiveClass.NA, [
        # Polite forms
        ['嫌[きら]いです', Form.NON_PAST, Formality.POLITE],
        ['嫌[きら]いじゃないです', Form.NON_PAST_NEG, Formality.POLITE],
        ['嫌[きら]いでした', Form.PAST, Formality.POLITE],
        ['嫌[きら]いじゃなかったです', Form.PAST_NEG, Formality.POLITE],
        # Plain forms
        ['嫌[きら]いだ', Form.NON_PAST, Formality.PLAIN],
        ['嫌[きら]いじゃない', Form.NON_PAST_NEG, Formality.PLAIN],
        ['嫌[きら]いだった', Form.PAST, Formality.PLAIN],
        ['嫌[きら]いじゃなかった', Form.PAST_NEG, Formality.PLAIN],
        # formality-constant
        ['嫌[きら]いで', Form.TE, None],
    ]),
    ('暖[あたた]かい', AdjectiveClass.I, [
        # Polite forms
        ['暖[あたた]かいです', Form.NON_PAST, Formality.POLITE],
        ['暖[あたた]かくないです', Form.NON_PAST_NEG, Formality.POLITE],
        ['暖[あたた]かかったです', Form.PAST, Formality.POLITE],
        ['暖[あたた]かくなかったです', Form.PAST_NEG, Formality.POLITE],
        # Plain forms
        ['暖[あたた]かい', Form.NON_PAST, Formality.PLAIN],
        ['暖[あたた]かくない', Form.NON_PAST_NEG, Formality.PLAIN],
        ['暖[あたた]かかった', Form.PAST, Formality.PLAIN],
        ['暖[あたた]かくなかった', Form.PAST_NEG, Formality.PLAIN],
        # formality-constant
        ['暖[あたた]かくて', Form.TE, None],
    ])
]
@pytest.mark.parametrize("dict_form, adj_class, reference", generate_adjective_forms_data)
def test_generate_adjective_forms(dict_form, adj_class, reference):
    """test the generate_adjective_forms() method"""
    forms = generate_adjective_forms(dict_form, adj_class)
    assert forms == reference
    general_forms = generate_adjective_forms(dict_form, AdjectiveClass.GENERAL)
    assert general_forms == reference
