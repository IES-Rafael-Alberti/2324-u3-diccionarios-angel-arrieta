"""
Ejercicio 3.2.8¶

Escribir un programa que cree un diccionario de traducción español-inglés.
El usuario introducirá las palabras en español e inglés separadas por dos puntos,
y cada par <palabra>:<traducción> separados por comas.
El programa debe crear un diccionario con las palabras y sus traducciones.
Después pedirá una frase en español y utilizará el diccionario
para traducirla palabra a palabra.
Si una palabra no está en el diccionario debe dejarla sin traducir.
"""


def dividir_traducciones(diccion: str) -> list:
    lista_bruta = []
    dividido = diccion.split(",")
    for referencia in dividido:
        lista_bruta.append(referencia.strip())
    return lista_bruta


def adecuar_diccionario(listado: list) -> dict:
    """ Función que se encarga de convertir los duós de traducción en un diccionario """
    diccionario_adecuado = {}
    for referencia in listado:
        espanol, ingles = referencia.split(":")
        diccionario_adecuado.update({espanol.lower().strip(): ingles.strip()})
    return diccionario_adecuado


def adecuar_frase(frase_bruta: str) -> list:
    """ Función que se encarga de convertir las palabras de la frase en una lista """
    frase = []
    frase_dividida = frase_bruta.split(" ")
    for palabra in frase_dividida:
        frase.append(palabra.lower())
    return frase


def traducir(frase: list, diccionario: dict) -> str:
    """ Función que traduce la frase en español al íngles.
        Si en la frase se encuentra alguna palabra no registrada en el diccionario,
        esta no se traduce y se mantiene en español."""
    traducir = []
    for palabra_espanola in frase:
        anadir = diccionario.get(palabra_espanola, palabra_espanola)
        traducir.append(anadir)
    traducido = " ".join(traducir)
    return traducido


def control_division(listado: list) -> int:
    """
    Función que se encarga de controlar que las palabras sean lógicas
    -----------
    listado: list
        Listado con las traducciones a registrar

    return: int
        Número devuelto dependiendo del error que se detecte,
        devuelve 0 si no hay errores. Numeración de los errores:
            0 - si la referencia introducida es lógica
            1 - alguna referencia introducida tiene carece de ':'
            2 - alguna referencia introducida tiene más de un ':'
    """
    fallo = 0
    import re
    for referencia in listado:
        if re.search("[:]", referencia) is None:
            fallo = 1
            return fallo
        elif referencia.count(":") > 1:
            fallo = 2
            return fallo
    return fallo


def repeticion(listado: list) -> int:
    """ Función que se encarga de encontrar traducciones repetidas.
        Si alguna palabra española, tiene más de una traducción:
        Devuelve el error número 3"""
    espanol = []
    fallo = 0
    for referencia in listado:
        espanola, ingles = referencia.split(":")
        espanol.append(espanola.strip())
    for palabra in espanol:
        if espanol.count(palabra) > 1:
            fallo = 3
            return fallo
    return fallo


def control_dict(traducciones: dict) -> int or str:
    """
    Función que se encarga de controlar que las palabras sean lógicas
    -----------
    traducciones: dict
        Diccionario donde se encuentran las traducciones registradas

    return: int or str
        Valor devuelto dependiendo del error que se detecte,
        devuelve 0 si no hay errores. Devolución de los errores:
            0 - si las palabras introducidas son lógicas
            4 - si una palabra introducida está vacía
            f"{palabra_con_el_error}" - si en alguna palabra introducida se encuentran carácteres que no son alfabéticos
                                        respecto a su idioma
    """
    fallo = 0
    import re
    espanol = list(traducciones.keys())
    english = list(traducciones.values())
    for clave in espanol:
        if len(clave) < 1:
            fallo = 4
            return fallo
        elif re.search("[^A-Za-zÁáÉéÍíÓóÚúÑñÜü]", clave) is not None:
            fallo = clave
            return fallo
    for valor in english:
        if len(valor) < 1:
            fallo = 4
            return fallo
        elif re.search("[^A-Za-z]", valor) is not None:
            fallo = valor
            return fallo
    return fallo


def control_frase(frase: list) -> int:
    """
    Función que se encarga de controlar que las palabras de la frase en español sean lógicas
    -----------
    frase: str
        Frase en español a revisar su lógica gramátical

    return: int
        Número devuelto dependiendo del error que se detecte,
        devuelve 0 si no hay errores. Numeración de los errores:
            0 - si las palabras introducidas son lógicas
            5 - si en alguna palabra introducida se encuentran carácteres que no son alfabéticos
    """
    fallo = 0
    import re
    for palabra in frase:
        if re.search("[^A-Za-zÁáÉéÍíÓóÚúÑñÜü]", palabra) is not None:
            fallo = 5
            return fallo
    return fallo


if __name__ == "__main__":
    error = 0
    try:
        # Entrada
        diccionario_bruto = str(input("Introduce tu diccionario español-ingles. Sigue el siguiente formato:\n"
                                "[palabra-en-español: palabra-en-ingles, español: ingles, español: ingles, ...]\n> "))
        # Proceso
        diccionario_dividido = dividir_traducciones(diccionario_bruto)
        error = control_division(diccionario_dividido)
        if error != 0:
            raise ValueError(error)
        error = repeticion(diccionario_dividido)
        if error != 0:
            raise ValueError(error)
        diccionario = adecuar_diccionario(diccionario_dividido)
        error = control_dict(diccionario)
        if error != 0:
            raise ValueError(error)
        frase_en_espanol = str(input("Dime una frase en español para traducir al ingles\n"
                                     "(Use solo espacios para dividir las palabras)\n> "))  # Entrada
        frase_adaptada = adecuar_frase(frase_en_espanol)
        error = control_frase(frase_adaptada)
        if error != 0:
            raise ValueError(error)
        frase_traducida = traducir(frase_adaptada, diccionario)
    # Salida
        print(f"{frase_en_espanol}.\nSegún el diccionario provisto, la traducción es la siguiente:\n{frase_traducida}.")

    except ValueError:
        if error == 1:
            print("Se ha introducido una traducción con error de forma.\n"
                  "En una referencia no se ha encontrado ningún ':'\n"
                  "(Formato solicitado: [palabra-en-español: palabra-en-ingles, español: ingles, español: ingles, ...]")
        elif error == 2:
            print("Se ha introducido una traducción con error de forma.\n"
                  "En una referencia se ha encontrado mas de ún ':'\n"
                  "(Formato solicitado: [palabra-en-español: palabra-en-ingles, español: ingles, español: ingles, ...]")
        elif error == 3:
            print("Se ha encontrado una traducción repetida.\n"
                  "Se ha encontrado una referencia en español más de una vez")
        elif error == 4:
            print("Se ha encontrado una referencia vacía.\n")
        elif type(error) == str:
            print(f"{error} contiene carácteres no reconocibles en su idioma.\n"
                  f"(Formato traducción: [español: ingles, ...])")
        elif error == 5:
            print("Se ha encontrado algún carácter ortográficamente irreconocible en la frase\n"
                  "Carácteres reconocidos: [A-Za-zÁáÉéÍíÓóÚúÑñÜü]")
