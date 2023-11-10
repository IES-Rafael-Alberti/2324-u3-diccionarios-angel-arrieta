import pytest
from src.Ej_3_2 import control_stock, control_kg, pedido


@pytest.mark.parametrize(
    "inFruta, inStock, outFallo",
    [
        ("manzana", {"plátano": 1.35, "manzana": 0.80, "pera": 0.85, "naranja": 0.70}, 0),
        ("p3_r@", {"plátano": 1.35, "manzana": 0.80, "pera": 0.85, "naranja": 0.70}, 1),
        ("melocotón", {"plátano": 1.35, "manzana": 0.80, "pera": 0.85, "naranja": 0.70}, 2)
    ]
)
def test_control_stock(inFruta, inStock, outFallo):
    assert control_stock(inFruta, inStock) == outFallo


@pytest.mark.parametrize(
    "inPeso, outFallo",
    [
        ("1.3", 0),
        ("2.A5", 3),
        ("2.55.76", 4),
        ("0.06", 5)
    ]
)
def test_control_kg(inPeso, outFallo):
    assert control_kg(inPeso) == outFallo


@pytest.mark.parametrize(
    "inFruta, inPeso, inTienda, outPrecio",
    [
        ("manzana", 0.76, {"plátano": 1.35, "manzana": 0.80, "pera": 0.85, "naranja": 0.70}, 0.61),
        ("plátano", 0.28, {"plátano": 1.35, "manzana": 0.80, "pera": 0.85, "naranja": 0.70}, 0.38),
        ("naranja", 1.35, {"plátano": 1.35, "manzana": 0.80, "pera": 0.85, "naranja": 0.70}, 0.94),
        ("pera", 2.74, {"plátano": 1.35, "manzana": 0.80, "pera": 0.85, "naranja": 0.70}, 2.33)
    ]
)
def test_pedido(inFruta, inPeso, inTienda, outPrecio):
    assert pedido(inFruta, inPeso, inTienda) == outPrecio
