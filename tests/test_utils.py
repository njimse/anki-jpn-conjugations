import pytest

from anki_jpn.util import delta_split

delta_split_data = [
    ('foo', 'foobar', 'foo', 'bar'),
    ('foo', 'bar', '', 'bar'),
    ('foot', 'foobar', 'foo', 'bar'),
    ('食べる', '食べます', '食べ', 'ます'),
    ('食[た]べる', '食[た]べます', '食[た]べ', 'ます'),
    ('来る', '来ない', '来', 'ない'),
    ('来[く]る', '来[こ]ない', '', '来[こ]ない'),
    ('歩[ある]く', '歩[ある]きます', '歩[ある]', 'きます'),
    ('ある', 'ない', '', 'ない'),
    ('食[た]べる', '食[た]べる', '食[た]べる', '')
]
@pytest.mark.parametrize('dict_form, conj, ref_stem, ref_ending', delta_split_data)
def test_delta_split(dict_form, conj, ref_stem, ref_ending):
    stem, ending = delta_split(dict_form, conj)
    assert stem == ref_stem
    assert ending == ref_ending