"""Unit tests for utility methods"""
import importlib.resources
import pytest
import js2py
import anki_jpn.resources
from anki_jpn.util import (
    remove_furigana,
    promote_furigana
)

insert_ending_spans_text = importlib.resources.read_text(anki_jpn.resources, # pylint: disable=W4902
                                                         'insert_ending_spans.js')
insert_ending_spans = js2py.eval_js(insert_ending_spans_text)
insert_ending_spans_data = [
    ('foo', 'foobar', 'foo<span id=ending>bar</span>'),
    ('foo', 'bar', '<span id=ending>bar</span>'),
    ('foo', 'foo', 'foo'),
    ('foot', 'foobar', 'foo<span id=ending>bar</span>'),
    ('食べる', '食べます', '食べ<span id=ending>ます</span>'),
    ('<ruby><rb>食</rb><rt>た</rt></ruby>べる', '<ruby><rb>食</rb><rt>た</rt></ruby>べます',
        '<ruby><rb>食</rb><rt>た</rt></ruby>べ<span id=ending>ます</span>'),
    ('来る', '来ない', '来<span id=ending>ない</span>'),
    ('<ruby><rb>来</rb><rt>く</rt></ruby>る', '<ruby><rb>来</rb><rt>こ</rt></ruby>ない',
        '<ruby><rb>来</rb><rt><span id=ending>こ</span></rt></ruby><span id=ending>ない</span>'),
    ('<ruby><rb>歩</rb><rt>ある</rt></ruby>く', '<ruby><rb>歩</rb><rt>ある</rt></ruby>きます',
     '<ruby><rb>歩</rb><rt>ある</rt></ruby><span id=ending>きます</span>'),
    ('ある', 'ない', '<span id=ending>ない</span>'),
    ('<ruby><rb>食</rb><rt>た</rt></ruby>べる', '<ruby><rb>食</rb><rt>た</rt></ruby>べる',
     '<ruby><rb>食</rb><rt>た</rt></ruby>べる')
]
@pytest.mark.parametrize('dict_form, conj, ref_conjugation', insert_ending_spans_data)
def test_insert_ending_spans(dict_form, conj, ref_conjugation):
    """test the correctness of the Javascript function used to identify the difference
    between the dictionary and conjugated forms, inserting <span> tags to label the
    identified differences"""
    modified_conjugation = insert_ending_spans(dict_form, conj)
    assert modified_conjugation == ref_conjugation


furigana_removal_data = [
    ("いる", "いる"),
    ("くる", "くる"),
    ("来る", "来る"),
    ("来[く]る", "来る"),
    ("持[も]って 来[く]る", "持って来る"),
    ("発音[はつおん]する", "発音する"),
    ("発[はつ] 音[おん]する", "発音する"),
    ("お 久[ひさ]し 振[ぶ]りです", "お久し振りです")
]
@pytest.mark.parametrize("reading, ref", furigana_removal_data)
def test_remove_furigana(reading, ref):
    """Test the removal of furigana"""

    hyp = remove_furigana(reading)
    assert hyp == ref

furigana_promotion_data = [
    ("いる", "いる"),
    ("くる", "くる"),
    ("来る", "来る"),
    ("来[く]る", "くる"),
    ("持[も]って 来[く]る", "もってくる"),
    ("発音[はつおん]する", "はつおんする"),
    ("発[はつ] 音[おん]する", "はつおんする"),
    ("お 久[ひさ]し 振[ぶ]りです", "おひさしぶりです")
]
@pytest.mark.parametrize("reading, ref", furigana_promotion_data)
def test_promote_furigana(reading, ref):
    """Test the promotion of furigana"""

    hyp = promote_furigana(reading)
    assert hyp == ref
