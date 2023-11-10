import pytest
from src.Ej_9_2 import control_factura, control_identificador, recoger_identificadores, deuda_clientes


@pytest.mark.parametrize(
    "inFactura, outError",
    [
        ("10142: 73.52", 0),
        ("10142 - 73.52", 1),
        ("10142: :73.52", 1),
        (".10I42: 73.52", 2),
        ("10142: ~7E.5$", 2),
        ("0010142: 73.52", 3),
        ("10142: 73.5.2", 4)
    ]
)
def test_control_factura(inFactura, outError):
    assert control_factura(inFactura) == outError


@pytest.mark.parametrize(
    "inIdentidad, outError",
    [
        ("0990476", 0),
        ("", 5),
        ("0þ9.0A76", 6)
    ]
)
def test_control_identificador(inIdentidad, outError):
    assert control_identificador(inIdentidad) == outError


@pytest.mark.parametrize(
    "inFacturas, outIdentidades",
    [
        ({56071: 50.21, 81022: 173.80}, [56071, 81022]),
        ({56071: 50.21, 81022: 173.80, 42033369: 96.24}, [56071, 81022, 42033369])

    ]
)
def test_recoger_identificadores(inFacturas, outIdentidades):
    assert recoger_identificadores(inFacturas) == outIdentidades


@pytest.mark.parametrize(
    "inFacturas, outTotal_pagos",
    [
        ({56071: 50.21, 81022: 173.80}, 224.01),
        ({71092: 46.55, 93041: 262.61, 42033369: 96.24}, 405.40)
    ]
)
def test_deuda_clientes(inFacturas, outTotal_pagos):
    assert deuda_clientes(inFacturas) == outTotal_pagos
