"""Unit tests for the util module"""
import pytest

from anki_jpn.util import (
    remove_furigana,
    promote_furigana
)

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
    hyp = promote_furigana(reading)
    assert hyp == ref
