import pytest
from src.Ej_6_2 import control, datacion


@pytest.mark.parametrize(
    "inClave, inDato, outError",
    [
        ("Nombre", "Ángel Arrieta", 0),
        ("Nombre", "J0$e._.M4nue/", 1),
        ("Edad", "025", 0),
        ("Edad", "1047", 2),
        ("Edad", "4E", 2),
        ("Edad", "00", 3),
        ("Edad", "131", 3),
        ("Sexo", "Hombre", 0),
        ("Sexo", "hombREs", 4),
        ("Sexo", "mUJer", 0),
        ("Sexo", "mUJereS", 4),
        ("Sexo", "amigable", 4),
        ("Teléfono", "123456789", 0),
        ("Teléfono", "12345678", 5),
        ("Teléfono", "0123456789", 5),
        ("Teléfono", "I2·456/8", 5),
        ("Correo electrónico", "a@a.a", 0),
        ("Correo electrónico", "a.arrieta03_soto@gmail.com", 0),
        ("Correo electrónico", "a.arrieta@03_soto@gmail.com", 6),
        ("Correo electrónico", "a.arrieta03_sotogmail.com", 6),
        ("Correo electrónico", "a.arrieta03_soto@gmailcom", 6),
        ("Correo electrónico", "a.arrieta03_soto@gm.ail.com", 6),
        ("Correo electrónico", "^ar¿[ri e]/a)03*soto@gmail.com", 6),
        ("Correo electrónico", "a.arrieta03_soto@GM a1l.com", 6),
        ("Correo electrónico", "a.arrieta03_soto@gmail.C 0m", 6)
    ]
)
def test_control(inClave, inDato, outError):
    assert control(inClave, inDato) == outError


@pytest.mark.parametrize(
    "inDatos, outMensaje",
    [
        ({"Nombre": "Ángel"}, "Nombre: Ángel"),
        ({"Nombre": "Ángel", "Edad": "25", "Sexo": "hombre"}, "Nombre: Ángel\nEdad: 25\nSexo: hombre"),
        ({"Nombre": "Ángel", "Edad": "25"}, "Nombre: Ángel\nEdad: 25")
    ]
)
def test_datacion(inDatos, outMensaje):
    assert datacion(inDatos) == outMensaje
