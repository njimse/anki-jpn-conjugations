"""Unit tests for the classification of adjectives"""
import pytest

from japanese_conjugation.enums import AdjectiveClass
from japanese_conjugation.adjectives import classify_adjective

adjective_classification_data = [
    # These are the (main) exceptions
    ("綺麗", AdjectiveClass.NA),
    ("綺麗[きれい]", AdjectiveClass.NA),
    ("きれい", AdjectiveClass.NA),
    ("綺麗[きれい]な", AdjectiveClass.NA),
    ("きれいな", AdjectiveClass.NA),
    ("嫌[きら]い", AdjectiveClass.NA),
    ("きらい", AdjectiveClass.NA),
    ("嫌[きら]いな", AdjectiveClass.NA),
    ("きらいな", AdjectiveClass.NA),
    ("幸[さいわ]い", AdjectiveClass.NA),
    ("さいわい", AdjectiveClass.NA),
    ("幸[さいわ]いな", AdjectiveClass.NA),
    ("さいわいな", AdjectiveClass.NA),
    # End main exceptions
    ("美味しい", AdjectiveClass.I),
    ("美味[おおい]しい", AdjectiveClass.I),
    ("おおいしい", AdjectiveClass.I),
    ("簡単", AdjectiveClass.NA),
    ("簡単な", AdjectiveClass.NA),
    ("簡単[かんたん]", AdjectiveClass.NA),
    ("簡単[かんたん]な", AdjectiveClass.NA),
    ("かんたん", AdjectiveClass.NA),
    ("かんたんな", AdjectiveClass.NA),
    ("良い", AdjectiveClass.I),
    ("良[よ]い", AdjectiveClass.I),
    ("よい", AdjectiveClass.I),
    ("可愛い", AdjectiveClass.I),
    ("可愛[かわい]い", AdjectiveClass.I),
    ("かわいい", AdjectiveClass.I),
    ("かっこいい", AdjectiveClass.I),
    ("格好[かっこ] 良[よ]い", AdjectiveClass.I),
    ("格好良[かっこよ]い", AdjectiveClass.I),
]
@pytest.mark.parametrize("reading, ref_class", adjective_classification_data)
def test_adjective_classification(reading, ref_class):
    """Test that we correctly classify adjectives"""
    hyp_class = classify_adjective(reading)
    assert hyp_class == ref_class
