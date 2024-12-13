import pytest

from anki_jpn.enums import (
    AdjectiveClass
)
from anki_jpn.adjectives import (
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
    ('早[はや]い', AdjectiveClass.I, '早[はや]いです')
]
@pytest.mark.parametrize("dict_form, adj_class, reference", polite_nonpast_positive_data)
def test_polite_nonpast_positive(dict_form, adj_class, reference):
    result = polite_nonpast_positive(dict_form, adj_class)
    assert result == reference

polite_nonpast_negative_data = [
    ('元気な', AdjectiveClass.NA, '元気じゃないです'),
    ('元気[げんき]な', AdjectiveClass.NA, '元気[げんき]じゃないです'),
    ('暇[ひま]な', AdjectiveClass.NA, '暇[ひま]じゃないです'),
    ('暇な', AdjectiveClass.NA, '暇じゃないです'),
    ('美味[おい]しい', AdjectiveClass.I, '美味[おい]しくないです'),
    ('美味しい', AdjectiveClass.I, '美味しくないです'),
    ('早[はや]い', AdjectiveClass.I, '早[はや]くないです')
]
@pytest.mark.parametrize("dict_form, adj_class, reference", polite_nonpast_negative_data)
def test_polite_nonpast_negative(dict_form, adj_class, reference):
    result = polite_nonpast_negative(dict_form, adj_class)
    assert result == reference

polite_past_positive_data = [
    ('元気な', AdjectiveClass.NA, '元気でした'),
    ('元気[げんき]な', AdjectiveClass.NA, '元気[げんき]でした'),
    ('暇[ひま]な', AdjectiveClass.NA, '暇[ひま]でした'),
    ('暇な', AdjectiveClass.NA, '暇でした'),
    ('美味[おい]しい', AdjectiveClass.I, '美味[おい]しかったです'),
    ('美味しい', AdjectiveClass.I, '美味しかったです'),
    ('早[はや]い', AdjectiveClass.I, '早[はや]かったです')
]
@pytest.mark.parametrize("dict_form, adj_class, reference", polite_past_positive_data)
def test_polite_past_positive(dict_form, adj_class, reference):
    result = polite_past_positive(dict_form, adj_class)
    assert result == reference

polite_past_negative_data = [
    ('元気な', AdjectiveClass.NA, '元気じゃなかったです'),
    ('元気[げんき]な', AdjectiveClass.NA, '元気[げんき]じゃなかったです'),
    ('暇[ひま]な', AdjectiveClass.NA, '暇[ひま]じゃなかったです'),
    ('暇な', AdjectiveClass.NA, '暇じゃなかったです'),
    ('美味[おい]しい', AdjectiveClass.I, '美味[おい]しくなかったです'),
    ('美味しい', AdjectiveClass.I, '美味しくなかったです'),
    ('早[はや]い', AdjectiveClass.I, '早[はや]くなかったです')
]
@pytest.mark.parametrize("dict_form, adj_class, reference", polite_past_negative_data)
def test_polite_past_negative(dict_form, adj_class, reference):
    result = polite_past_negative(dict_form, adj_class)
    assert result == reference

te_data = [
    ('元気な', AdjectiveClass.NA, '元気で'),
    ('元気[げんき]な', AdjectiveClass.NA, '元気[げんき]で'),
    ('暇[ひま]な', AdjectiveClass.NA, '暇[ひま]で'),
    ('暇な', AdjectiveClass.NA, '暇で'),
    ('美味[おい]しい', AdjectiveClass.I, '美味[おい]しくて'),
    ('美味しい', AdjectiveClass.I, '美味しくて'),
    ('早[はや]い', AdjectiveClass.I, '早[はや]くて')
]
@pytest.mark.parametrize("dict_form, adj_class, reference", te_data)
def test_te(dict_form, adj_class, reference):
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
    ('早[はや]い', AdjectiveClass.I, '早[はや]い')
]
@pytest.mark.parametrize("dict_form, adj_class, reference", plain_nonpast_positive_data)
def test_plain_nonpast_positive(dict_form, adj_class, reference):
    result = plain_nonpast_positive(dict_form, adj_class)
    assert result == reference

plain_nonpast_negative_data = [
    ('元気な', AdjectiveClass.NA, '元気じゃない'),
    ('元気[げんき]な', AdjectiveClass.NA, '元気[げんき]じゃない'),
    ('暇[ひま]な', AdjectiveClass.NA, '暇[ひま]じゃない'),
    ('暇な', AdjectiveClass.NA, '暇じゃない'),
    ('美味[おい]しい', AdjectiveClass.I, '美味[おい]しくない'),
    ('美味しい', AdjectiveClass.I, '美味しくない'),
    ('早[はや]い', AdjectiveClass.I, '早[はや]くない')
]
@pytest.mark.parametrize("dict_form, adj_class, reference", plain_nonpast_negative_data)
def test_plain_nonpast_negative(dict_form, adj_class, reference):
    result = plain_nonpast_negative(dict_form, adj_class)
    assert result == reference

plain_past_positive_data = [
    ('元気な', AdjectiveClass.NA, '元気だった'),
    ('元気[げんき]な', AdjectiveClass.NA, '元気[げんき]だった'),
    ('暇[ひま]な', AdjectiveClass.NA, '暇[ひま]だった'),
    ('暇な', AdjectiveClass.NA, '暇だった'),
    ('美味[おい]しい', AdjectiveClass.I, '美味[おい]しかった'),
    ('美味しい', AdjectiveClass.I, '美味しかった'),
    ('早[はや]い', AdjectiveClass.I, '早[はや]かった')
]
@pytest.mark.parametrize("dict_form, adj_class, reference", plain_past_positive_data)
def test_plain_past_positive(dict_form, adj_class, reference):
    result = plain_past_positive(dict_form, adj_class)
    assert result == reference

plain_past_negative_data = [
    ('元気な', AdjectiveClass.NA, '元気じゃなかった'),
    ('元気[げんき]な', AdjectiveClass.NA, '元気[げんき]じゃなかった'),
    ('暇[ひま]な', AdjectiveClass.NA, '暇[ひま]じゃなかった'),
    ('暇な', AdjectiveClass.NA, '暇じゃなかった'),
    ('美味[おい]しい', AdjectiveClass.I, '美味[おい]しくなかった'),
    ('美味しい', AdjectiveClass.I, '美味しくなかった'),
    ('早[はや]い', AdjectiveClass.I, '早[はや]くなかった')
]
@pytest.mark.parametrize("dict_form, adj_class, reference", plain_past_negative_data)
def test_plain_past_negative(dict_form, adj_class, reference):
    result = plain_past_negative(dict_form, adj_class)
    assert result == reference