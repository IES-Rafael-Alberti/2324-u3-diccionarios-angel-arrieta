import pytest
from src.Ej_4_2 import control_formato_fecha, adecuar_fecha, control_fecha, dividir_fecha, mes_escrito


@pytest.mark.parametrize(
    "inFecha, outError",
    [
        ("24/12/2003", 0),
        ("5/3/2015", 1),
        ("05/03/2015", 0),
        ("15 07 1897", 1),
        ("08/ago/1931", 1)
    ]
)
def test_control_formato_fecha(inFecha, outError):
    assert control_formato_fecha(inFecha) == outError


@pytest.mark.parametrize(
    "inCadena, outLista",
    [
        ("05/03/2015", [5, 3, 2015]),
        ("22/02/1998", [22, 2, 1998]),
        ("01/01/1975", [1, 1, 1975])
    ]
)
def test_adecuar_fecha(inCadena, outLista):
    assert adecuar_fecha(inCadena) == outLista


@pytest.mark.parametrize(
    "inFecha, outError",
    [
        ([24, 12, 2003], 0),
        ([27, 0, 1998], 2),
        ([44, 11, 1783], 3),
        ([29, 2, 2017], 4),
        ([31, 4, 2023], 5)
    ]
)
def test_control_fecha(inFecha, outError):
    assert control_fecha(inFecha) == outError


@pytest.mark.parametrize(
    "inFecha, outTupla",
    [
        ([24, 12, 2003], (24, 12, 2003)),
        ([22, 2, 1998], (22, 2, 1998)),
        ([17, 5, 1833], (17, 5, 1833)),
        ([8, 10, 2011], (8, 10, 2011))
    ]
)
def test_dividir_fecha(inFecha, outTupla):
    assert dividir_fecha(inFecha) == outTupla


@pytest.mark.parametrize(
    "inMeses, inNumero, outMes",
    [
        ({1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
            9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"}, 1, "enero"),
        ({1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
            9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"}, 5, "mayo"),
        ({1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
            9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"}, 9, "septiembre"),
        ({1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
            9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"}, 4, "abril"),
        ({1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
            9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"}, 12, "diciembre")
    ]
)
def test_mes_escrito(inMeses, inNumero, outMes):
    assert mes_escrito(inMeses, inNumero) == outMes
