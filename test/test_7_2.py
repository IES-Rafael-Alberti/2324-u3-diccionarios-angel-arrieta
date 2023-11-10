import pytest
from src.Ej_7_2 import control_articulo, control_valor, cesta


@pytest.mark.parametrize(
    "inObjeto, outError",
    [
        ("Sartén", 0),
        ("Super-glue_101", 1)
    ]
)
def test_control_articulo(inObjeto, outError):
    assert control_articulo(inObjeto) == outError


@pytest.mark.parametrize(
    "inPrecio, outError",
    [
        ("13", 0),
        ("4.75", 0),
        ("34.26.7", 2),
        ("I5.4A", 2)
    ]
)
def test_control_valor(inPrecio, outError):
    assert control_valor(inPrecio) == outError


@pytest.mark.parametrize(
    "inMensaje, outMensaje",
    [
        ({"Mesa madera": 49.99, "Banqueta": 12.99}, "Mesa madera: 49.99\nBanqueta: 12.99\nTotal: 62.98"),
        ({"Mesa madera": 49.99, "Banqueta": 12.99, "Centro de mesa": 4.99},
            "Mesa madera: 49.99\nBanqueta: 12.99\nCentro de mesa: 4.99\nTotal: 67.97"),
    ]
)
def test_cesta(inMensaje, outMensaje):
    assert cesta(inMensaje) == outMensaje

