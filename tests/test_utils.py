"""Unit tests for utility methods"""
import importlib.resources
import pytest
import js2py
import japanese_conjugation.resources
from japanese_conjugation.util import (
    remove_furigana,
    promote_furigana,
    escape_query
)

insert_ending_spans_text = importlib.resources.read_text(japanese_conjugation.resources, # pylint: disable=W4902
                                                         'insert_ending_spans.js')
insert_ending_spans = js2py.eval_js(insert_ending_spans_text)
insert_ending_spans_data = [
    ('foo', 'foobar', 'foo<span class=ending>bar</span>'),
    ('foo', 'bar', '<span class=ending>bar</span>'),
    ('foo', 'foo', 'foo'),
    ('foot', 'foobar', 'foo<span class=ending>bar</span>'),
    ('食べる', '食べます', '食べ<span class=ending>ます</span>'),
    ('<ruby><rb>食</rb><rt>た</rt></ruby>べる', '<ruby><rb>食</rb><rt>た</rt></ruby>べます',
        '<ruby><rb>食</rb><rt>た</rt></ruby>べ<span class=ending>ます</span>'),
    ('来る', '来ない', '来<span class=ending>ない</span>'),
    ('<ruby><rb>来</rb><rt>く</rt></ruby>る', '<ruby><rb>来</rb><rt>こ</rt></ruby>ない',
        '<ruby><rb>来</rb><rt><span class=ending>こ</span></rt></ruby><span class=ending>ない</span>'),
    ('<ruby><rb>歩</rb><rt>ある</rt></ruby>く', '<ruby><rb>歩</rb><rt>ある</rt></ruby>きます',
     '<ruby><rb>歩</rb><rt>ある</rt></ruby><span class=ending>きます</span>'),
    ('ある', 'ない', '<span class=ending>ない</span>'),
    ('<ruby><rb>食</rb><rt>た</rt></ruby>べる', '<ruby><rb>食</rb><rt>た</rt></ruby>べる',
     '<ruby><rb>食</rb><rt>た</rt></ruby>べる'),
    ('<ruby><rb>連</rb><rt>つ</rt/></ruby>れて <ruby><rb>来</rb><rt>く</rt></ruby>る',
      '<ruby><rb>連</rb><rt>つ</rt/></ruby>れて <ruby><rb>来</rb><rt>き</rt></ruby>ます',
      '<ruby><rb>連</rb><rt>つ</rt/></ruby>れて <ruby><rb>来</rb><rt><span '\
        'class=ending>き</span></rt></ruby><span class=ending>ます</span>')
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

escape_query_data = [
    ("", ""),
    ("cat", "cat"),
    ('"cat"', r'\"cat\"'),
    ("'cat'", "'cat'"),
    ('cat" and dog', r'cat\" and dog'),
    (r'cat\" and dog', r'cat\\\" and dog'),
    (r'cat\\" and dog', r'cat\\\\\" and dog'),
    (r'cat\\" and \"dog', r'cat\\\\\" and \\\"dog')
]
@pytest.mark.parametrize("raw_input, ref_output", escape_query_data)
def test_escape_query(raw_input, ref_output):
    """Test the escaping of query text"""
    output = escape_query(raw_input)
    assert output == ref_output
