import pytest
from src.Ej_5_2 import mensaje, total_creditos


@pytest.mark.parametrize(
    "inAsignaturas, outMensaje",
    [
        ({'Matemáticas': 6, 'Física': 4, 'Química': 5},
            "Matemáticas tiene 6 créditos\nFísica tiene 4 créditos\nQuímica tiene 5 créditos"),
        ({'Física teórica': 3, 'Bio-Química': 8, 'Física aplicada': 10},
         "Física teórica tiene 3 créditos\nBio-Química tiene 8 créditos\nFísica aplicada tiene 10 créditos")
    ]
)
def test_mensaje(inAsignaturas, outMensaje):
    assert mensaje(inAsignaturas) == outMensaje


@pytest.mark.parametrize(
    "inAsignaturas, outMensaje",
    [
        ({'Matemáticas': 6, 'Física': 4, 'Química': 5}, "Créditos totales del curso: 15"),
        ({'Física teórica': 3, 'Bio-Química': 8, 'Física aplicada': 10}, "Créditos totales del curso: 21")
    ]
)
def test_total_creditos(inAsignaturas, outMensaje):
    assert total_creditos(inAsignaturas) == outMensaje
