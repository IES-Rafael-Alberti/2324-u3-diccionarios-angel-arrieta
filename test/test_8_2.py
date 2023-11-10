import pytest
from src.Ej_8_2 import dividir_traducciones, control_division, adecuar_diccionario, control_dict, adecuar_frase, control_frase, traducir, repeticion


@pytest.mark.parametrize(
    "inDict_Bruto, outParejas",
    [
        ("Mi: My, pana: friend, amigo: friend", ["Mi: My", "pana: friend", "amigo: friend"]),
        ("Me: I, gusta: like, mi: my, almuerzo: lunch", ["Me: I", "gusta: like", "mi: my", "almuerzo: lunch"])
    ]
)
def test_dividir_traducciones(inDict_Bruto, outParejas):
    assert dividir_traducciones(inDict_Bruto) == outParejas


@pytest.mark.parametrize(
    "inParejas, outDiccionario",
    [
        (["Mi: My", "pana: friend", "amigo: friend"],
         {"mi": "My", "pana": "friend", "amigo": "friend"}),
        (["Me: I", "gusta: like", "mi: my", "almuerzo: lunch"],
         {"me": "I", "gusta": "like", "mi": "my", "almuerzo": "lunch"})
    ]
)
def test_adecuar_diccionario(inParejas, outDiccionario):
    assert adecuar_diccionario(inParejas) == outDiccionario


@pytest.mark.parametrize(
    "inFrase, outLista",
    [
        ("Mi pana Miguel. Mi amigo Juan", ["mi", "pana", "miguel.", "mi", "amigo", "juan"]),
        ("Me gusta mi almuerzo", ["me", "gusta", "mi", "almuerzo"])
    ]
)
def test_adecuar_frase(inFrase, outLista):
    assert adecuar_frase(inFrase) == outLista


@pytest.mark.parametrize(
    "inFrase_Listada, inDiccionario, outTraduccion",
    [
        (["me", "gusta", "mi", "almuerzo"],
         {"me": "I", "gusta": "like", "mi": "my", "almuerzo": "lunch"},
         "I like my lunch"),
        (["mi", "pana", "miguel", "mi", "amigo", "juan"],
         {"mi": "My", "pana": "friend", "amigo": "friend"},
         "My friend miguel My friend juan")
    ]
)
def test_traducir(inFrase_Listada, inDiccionario, outTraduccion):
    assert traducir(inFrase_Listada, inDiccionario) == outTraduccion


@pytest.mark.parametrize(
    "inListado, outError",
    [
        (["Mi: My", "pana: friend", "amigo: friend"], 0),
        (["Me - I", "gusta - like", "mi - my", "almuerzo - lunch"], 1),
        (["Mi: My", "pana:amigo: friend"], 2)
    ]
)
def test_control_division(inListado, outError):
    assert control_division(inListado) == outError


@pytest.mark.parametrize(
    "inListado, outError",
    [
        (["Mi: My", "pana: friend", "amigo: friend"], 0),
        (["Me: I", "gusta: like", "mi: my", "almuerzo: lunch"], 0),
        (["Mi: My", "amigo: friend", "amigo: friend"], 3),
        (["Me: I", "gusta: like", "Me: my", "almuerzo: lunch"], 3)
    ]
)
def test_repeticion(inListado, outError):
    assert repeticion(inListado) == outError


@pytest.mark.parametrize(
    "inDiccionario, outError",
    [
        ({"mi": "my", "pana": "friend", "amigo": "friend"}, 0),
        ({"me": "i", "gusta": "like", "mi": "my", "almuerzo": "lunch"}, 0),
        ({"me": "i", "gusta": "like", "mi": "my", "": "lunch"}, 4),
        ({"mi": "my", "pana": "", "amigo": "friend"}, 4),
        ({"mi": "my", "p4na": "friend", "amigo": "friend"}, "p4na"),
        ({"me": "i", "gusta": "like", "mi": "my", "almuerzo": "luñch"}, "luñch")
    ]
)
def test_control_dict(inDiccionario, outError):
    assert control_dict(inDiccionario) == outError


@pytest.mark.parametrize(
    "inFrase_Listada, outError",
    [
        (["mi", "pana", "miguel", "mi", "amigo", "juan"], 0),
        (["me", "gusta", "mi", "almuerzo"], 0),
        (["mi", "pana", "miguel.", "mi", "amigo", "juan"], 5),
        (["me", "gust4", "mi", "almuerzo"], 5)
    ]
)
def test_control_frase(inFrase_Listada, outError):
    assert control_frase(inFrase_Listada) == outError
