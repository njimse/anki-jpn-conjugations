"""Tests for the enums submodule"""
from typing import List
import pytest

from japanese_conjugation.enums import (
    Dan,
    Gyo,
    AGyo,
    KaGyo,
    GaGyo,
    SaGyo,
    ZaGyo,
    TaGyo,
    DaGyo,
    NaGyo,
    HaGyo,
    BaGyo,
    PaGyo,
    MaGyo,
    RaGyo
)

@pytest.mark.parametrize("input_str, ref", [
    ("あ", AGyo), ("い", AGyo), ("う", AGyo), ("え", AGyo), ("お", AGyo),
    ("か", KaGyo), ("き", KaGyo), ("く", KaGyo), ("け", KaGyo), ("こ", KaGyo),
    ("が", GaGyo), ("ぎ", GaGyo), ("ぐ", GaGyo), ("げ", GaGyo), ("ご", GaGyo),
    ("さ", SaGyo), ("し", SaGyo), ("す", SaGyo), ("せ", SaGyo), ("そ", SaGyo),
    ("ざ", ZaGyo), ("じ", ZaGyo), ("ず", ZaGyo), ("ぜ", ZaGyo), ("ぞ", ZaGyo),
    ("た", TaGyo), ("ち", TaGyo), ("つ", TaGyo), ("て", TaGyo), ("と", TaGyo),
    ("だ", DaGyo), ("ぢ", DaGyo), ("づ", DaGyo), ("で", DaGyo), ("ど", DaGyo),
    ("な", NaGyo), ("に", NaGyo), ("ぬ", NaGyo), ("ね", NaGyo), ("の", NaGyo),
    ("は", HaGyo), ("ひ", HaGyo), ("ふ", HaGyo), ("へ", HaGyo), ("ほ", HaGyo),
    ("ば", BaGyo), ("び", BaGyo), ("ぶ", BaGyo), ("べ", BaGyo), ("ぼ", BaGyo),
    ("ぱ", PaGyo), ("ぴ", PaGyo), ("ぷ", PaGyo), ("ぺ", PaGyo), ("ぽ", PaGyo),
    ("ま", MaGyo), ("み", MaGyo), ("む", MaGyo), ("め", MaGyo), ("も", MaGyo),
    ("ら", RaGyo), ("り", RaGyo), ("る", RaGyo), ("れ", RaGyo), ("ろ", RaGyo),
])
def test_gyo_identification(input_str: str, ref: Gyo):
    """Test the correctness of the Gyo identification method"""
    identified_gyo = Gyo.identify(input_str)
    assert identified_gyo == ref

@pytest.mark.parametrize("input_gyo, refs", [
    (AGyo, ["あ", "い", "う", "え", "お"]),
    (KaGyo, ["か", "き", "く", "け", "こ"]),
    (GaGyo, ["が", "ぎ", "ぐ", "げ", "ご"]),
    (SaGyo, ["さ", "し", "す", "せ", "そ"]),
    (ZaGyo, ["ざ", "じ", "ず", "ぜ", "ぞ"]),
    (TaGyo, ["た", "ち", "つ", "て", "と"]),
    (DaGyo, ["だ", "ぢ", "づ", "で", "ど"]),
    (NaGyo, ["な", "に", "ぬ", "ね", "の"]),
    (HaGyo, ["は", "ひ", "ふ", "へ", "ほ"]),
    (BaGyo, ["ば", "び", "ぶ", "べ", "ぼ"]),
    (PaGyo, ["ぱ", "ぴ", "ぷ", "ぺ", "ぽ"]),
    (MaGyo, ["ま", "み", "む", "め", "も"]),
    (RaGyo, ["ら", "り", "る", "れ", "ろ"])
])
def test_gyo_dan(input_gyo: Gyo, refs: List[str]):
    """Test the correctness of the dan() function for each Gyo"""
    assert input_gyo.dan(Dan.A) == refs[0]
    assert input_gyo.dan(Dan.I) == refs[1]
    assert input_gyo.dan(Dan.U) == refs[2]
    assert input_gyo.dan(Dan.E) == refs[3]
    assert input_gyo.dan(Dan.O) == refs[4]
