import pytest
from src.Ej_1_2 import control, simbolo


@pytest.mark.parametrize(
    "inClave, inDiccionario, outFallo",
    [
        ("Libra", {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}, 1),
        ("Euro", {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}, 0),
        ("Rupia", {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}, 1),
        ("Yen", {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}, 0)
    ]
)
def test_control(inClave, inDiccionario, outFallo):
    assert control(inClave, inDiccionario) == outFallo


@pytest.mark.parametrize(
    "inClave, inDiccionario, outDivisa",
    [
        ("Libra", {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}, None),
        ("Euro", {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}, '€'),
        ("Yen", {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}, '¥'),
    ]
)
def test_simbolo(inClave, inDiccionario, outDivisa):
    assert simbolo(inClave, inDiccionario) == outDivisa
