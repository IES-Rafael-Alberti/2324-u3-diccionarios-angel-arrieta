import pytest
from src.Ej_2_2 import adecuacion, control, agenda


@pytest.mark.parametrize(
    "inCadena, outLista",
    [
        ("Angel,20, calle lisa numero 13 , 666123487",
         ["Ángel", "20", "calle lisa numero 13", "666123487"]),
        ("Luis Miguel ,dieciocho , C/Carvajal Nº8, 612 53 47 77 ",
         ["Luis Miguel", "dieciocho", "C/Carvajal Nº8", "612 53 47 77"])
    ]
)
def test_adecuacion(inCadena, outLista):
    assert adecuacion(inCadena) == outLista


@pytest.mark.parametrize(
    "inDatos, outFallo",
    [
        (["María Jose", "0", "C/Carvajal Nº8", "612532777"], 4),
        (["José", "33", "Avda. Libertadores Nº41 A", "612 532 47 77"], 5),
        (["Ángel", "20", "calle lisa numero 13", "666123487"], 0),
        (["Luís Miguel", "dieciocho", "Calle Lorca_3", "611532444"], 3),
        (["Jaíme", "20", "Camino_antiguo", "Villa_carmen", "2", "666123487"], 1),
        (["4ndr3a", "25", "pluton 31", "77564"], 2),
        (["Mario", "25", "C/Carvajal Nº8", "666777"], 6)
    ]
)
def test_control(inDatos, outFallo):
    assert control(inDatos) == outFallo


@pytest.mark.parametrize(
    "inDatos, outContacto",
    [
        (["José", "33", "Avda. Libertadores Nº41 A", "612532477"],
    {"nombre": "José", "edad": "33", "dirección": "Avda. Libertadores Nº41 A", "teléfono": "612532477"}),
        (["Ángel", "20", "calle lisa numero 13", "666123487"],
    {"nombre": "Ángel", "edad": "20", "dirección": "calle lisa numero 13", "teléfono": "666123487"}),
        (["Andrea", "25", "pluton 31", "775641383"],
    {"nombre": "Andrea", "edad": "25", "dirección": "pluton 31", "teléfono": "775641383"})
    ]
)
def test_agenda(inDatos, outContacto):
    assert agenda(inDatos) == outContacto
