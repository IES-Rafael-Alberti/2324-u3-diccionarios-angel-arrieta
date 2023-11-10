import pytest
from src.Ej_10_2 import comprobar_adecuacion, nombres_clientes


@pytest.mark.parametrize(
    "inCampo, inValor, outFallo",
    [
        ("NIF", "123456789A", 0),
        ("NIF", "1234567A", 1),
        ("NIF", "1234567890A", 1),
        ("NIF", "1234567", 1),
        ("NIF", "123456789", 1),
        ("nombre", "Ángel Arrieta", 0),
        ("nombre", "Ángel_Arrieta", 2),
        ("nombre", "4nge1.Arri€/a", 2),
        ("dirección", "C./ Alameda 8", 0),
        ("dirección", "C. Alameda 8", 3),
        ("dirección", "C.// Alameda 8", 3),
        ("dirección", "C/ Alameda 8", 4),
        ("dirección", "Via./ Alameda 8", 4),
        ("dirección", "Avda./ Constitución 12", 0),
        ("dirección", "Avda./ Constitución nº12", 0),
        ("dirección", "Call./ Ñamo nº5", 0),
        ("dirección", "Avda./ €on$ti↓uciøn_nº12", 5),
        ("teléfono", "123456789", 0),
        ("teléfono", "12345678", 6),
        ("teléfono", "1234567890", 6),
        ("teléfono", "12E45&78@", 6),
        ("correo", "1-5_vide0.lol@lugar.dom", 0),
        ("correo", "1-5_vide0.lollugar.dom", 7),
        ("correo", "1-5_vide@.lol@lugar.dom", 7),
        ("correo", "1-5_vide0.lol@1ugard0m", 7),
        ("correo", "1-5_vide0.lol@lu.gar.dom", 7),
        ("correo", "↓-5_vid€0.lol@lugar.dom", 7),
        ("correo", "1-5_vide0.lol@lUgar.d0m", 7),
        ("preferente", "True", 0),
        ("preferente", "False", 0),
        ("preferente", "true", 8)
    ]
)
def test_comprobar_adecuacion(inCampo, inValor, outFallo):
    assert comprobar_adecuacion(inCampo, inValor) == outFallo


@pytest.mark.parametrize(
    "inClaves, inDiccionario, outReferencias",
    [
        (["345876123J"],
         {"345876123J": {"nombre": "Juana", "dirección": "C./Olavide 3", "teléfono": "123456789",
                         "correo": "juanilla@colo.es", "preferente": False},
        "123456789P": {"nombre": "Ángel", "dirección": "Avda./ Alameda 7", "teléfono": "666123987",
                          "correo": "a.arrieta@yahoo.com", "preferente": True}},
        ["345876123J: Juana"]),
        (["345876123J", "123456789P"],
         {"345876123J": {"nombre": "Juana", "dirección": "C./Olavide 3", "teléfono": "123456789",
                         "correo": "juanilla@colo.es", "preferente": False},
          "123456789P": {"nombre": "Ángel", "dirección": "Avda./ Alameda 7", "teléfono": "666123987",
                         "correo": "a.arrieta@yahoo.com", "preferente": True}},
         ["345876123J: Juana", "123456789P: Ángel"])
    ]
)
def test_nombres_clientes(inClaves, inDiccionario, outReferencias):
    assert nombres_clientes(inClaves, inDiccionario) == outReferencias
