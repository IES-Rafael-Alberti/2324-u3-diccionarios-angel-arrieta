"""
Ejercicio 3.2.7¶

Escribir un programa que cree un diccionario simulando una cesta de la compra.
El programa debe preguntar el artículo y su precio y añadir el par al diccionario,
hasta que el usuario decida terminar. Después se debe mostrar por pantalla
la lista de la compra y el coste total, con el siguiente formato.
"""


def control_articulo(mercancia: str) -> int:
    """
    Función que controla que la mercancía a añadir sea lógica
    --------------
    mercancia: str
        Nombre de la mercancía a comprar

    return: int
        Número devuelto dependiendo del error que se detecte,
        devuelve 0 si no hay errores. Numeración de los errores:
        0 - si la mercancía introducida tiene lógica
        1 - si en la mercancía se encuentran carácteres que no son alfabéticos, espacio o guion
    """
    fallo = 0
    import re
    if re.search("[^A-Za-zÁáÉéÍíÓóÚú -]", mercancia) is not None:
        fallo = 1
    return fallo


def control_valor(precio: str) -> int:
    """
    Función que controla que el precio introducido tenga sentido
    --------------
    precio: str
        Precio de la mercancía a comprar

    return: int
        Número devuelto dependiendo del error que se detecte,
        devuelve 0 si no hay errores. Numeración de los errores:
        0 - si el precio introducido tiene lógica
        2 - si en el precio introducido encuentran carácteres que no son dígito, punto ó hay más de un punto
    """
    fallo = 0
    import re
    if precio.count(".") > 1:
        fallo = 2
    elif re.search("[^0-9.]", precio) is not None:
        fallo = 2
    return fallo


def cesta(lista_de_compra: dict) -> str:
    factura = ""
    total = 0
    articulos = list(lista_de_compra.keys())
    for mercancia in articulos:
        factura += f"{mercancia}: {lista_de_compra.get(mercancia)}\n"
    precios = list(lista_de_compra.values())
    for precio in precios:
        total += precio
    factura += f"Total: {round(total, 2)}"
    return factura


if __name__ == "__main__":
    lista_de_la_compra = {}
    error = 0
    articulo = ""
    try:
        # Proceso
        while articulo != "terminar":
            # Entrada
            articulo = str(input("¿Que artículo desa comprar?\n(inserte 'terminar' para acabar el programa)\n> "))
            if articulo != "terminar":
                error = control_articulo(articulo)
                if error != 0:
                    raise ValueError(error)
                valor = str(input(f"Inserte precio de {articulo}\n> "))
                error = control_valor(articulo)
                if error != 0:
                    raise ValueError(error)
                lista_de_la_compra.update({articulo: float(valor)})
            # Salida
            else:
                ""
        if len(lista_de_la_compra) < 1:
            print("Lista de la compra vacía")
        else:
            ticket = cesta(lista_de_la_compra)
            print(ticket)

    except ValueError:
        if error == 1:
            print(f"{articulo} contiene carácteres no reconocibles\n(Carácteres reconocidos: "
                    f"['A'-'Z', 'a'-'z', 'Á', 'á', 'É', 'é', 'Í', 'í', 'Ó', 'ó', 'Ú', 'ú', ' ',  '-'])")
        elif error == 2:
            print(f"{valor} contiene carácteres no reconocibles\n"
                    f"(Solo se reconoce del 0 al 9 y '.' solo una vez como separador decimal)")
