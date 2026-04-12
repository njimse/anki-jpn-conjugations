import pytest
from typing import List

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

@pytest.mark.parametrize("input, ref", [
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
def test_gyo_identification(input: str, ref: Gyo):
    identified_gyo = Gyo.identify(input)
    assert identified_gyo == ref

@pytest.mark.parametrize("input, refs", [
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
def test_gyo_dan(input: Gyo, refs: List[str]):
    assert input.dan(Dan.a) == refs[0]
    assert input.dan(Dan.i) == refs[1]
    assert input.dan(Dan.u) == refs[2]
    assert input.dan(Dan.e) == refs[3]
    assert input.dan(Dan.o) == refs[4]