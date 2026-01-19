"""Unit tests for the classification of verbs"""
import pytest

from japanese_conjugation.enums import VerbClass
from japanese_conjugation.verbs import classify_verb

verb_classification_data = [
    ("たべる", VerbClass.ICHIDAN),
    ("食べる", VerbClass.ICHIDAN),
    ("食[た]べる", VerbClass.ICHIDAN),
    ("くる", VerbClass.IRREGULAR),
    ("来る", VerbClass.IRREGULAR),
    ("来[く]る", VerbClass.IRREGULAR),
    ("いく", VerbClass.GODAN),
    ("行く", VerbClass.GODAN),
    ("行[い]く", VerbClass.GODAN),
    ("しらべる", VerbClass.ICHIDAN),
    ("調べる", VerbClass.ICHIDAN),
    ("調[しら]べる", VerbClass.ICHIDAN),
    ("挵る", VerbClass.GODAN),
    ("挵[せせ]る", VerbClass.GODAN),
    ("せせる", VerbClass.GODAN),
    ("要る", VerbClass.GODAN),
    ("要[い]る", VerbClass.GODAN),
    ("いる", VerbClass.ICHIDAN),
    ("かりる", VerbClass.ICHIDAN),
    ("借りる", VerbClass.ICHIDAN),
    ("借[か]りる", VerbClass.ICHIDAN),
    ("持[も]って 来[く]る", VerbClass.IRREGULAR),
    ("持[も]って 行[い]く", VerbClass.GODAN),
    ("返る", VerbClass.GODAN),
    ("返[かえ]る", VerbClass.GODAN),
    ("かえる", VerbClass.ICHIDAN),
    ("減る", VerbClass.GODAN),
    ("減[へ]る", VerbClass.GODAN),
    ("へる", VerbClass.ICHIDAN)
]
@pytest.mark.parametrize("reading, ref_class", verb_classification_data)
def test_verb_classification(reading, ref_class):
    """Test that we correctly classify verbs"""
    hyp_class = classify_verb(reading)
    assert hyp_class == ref_class
