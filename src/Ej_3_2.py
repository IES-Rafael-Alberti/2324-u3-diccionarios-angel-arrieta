"""
Ejercicio 3.2.3¶

Escribir un programa que guarde en un diccionario los precios de
las frutas de la tabla, pregunte al usuario por una fruta,
un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta.
Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
"""


def control_stock(fruta: str, frutas: dict) -> int:
    """
    Función encargada de controlar la adecuación de los datos introducidos
    ----------------------
    fruta: str
        Información a consultar en la frutería
    frutas: dict
        Stock disponible en la tienda

    return: int
        Número devuelto dependiendo del error que se detecte,
        devuelve 0 si no hay errores. Numeración de los errores:
            1 - Hay caracteres no alfabéticos en la fruta
            2 - No se encuentra esa fruta en la tienda
    """
    fallo = 0
    import re
    if re.search("[^a-z áéíóúñ]", fruta) is not None:
        fallo = 1
    elif frutas.get(fruta) is None:
        fallo = 2
    return fallo


def control_kg(kilos: str) -> int:
    """
    Función encargada de controlar la adecuación del peso introducido
    ----------------------
    kilos: str
        Peso a pedir en la frutería

    return: int
        Número devuelto dependiendo del error que se detecte,
        devuelve 0 si no hay errores. Numeración de los errores:
            3 - Hay caracteres no dígitos en el peso
            4 - Más de un punto '.' encontrado
            5 - Peso demasiado chico para una sola fruta
    """
    fallo = 0
    import re
    if re.search("[^0-9.]", kilos) is not None:
        fallo = 3
    elif kilos.count(".") > 1:
        fallo = 4
    elif float(kilos) < 0.07:
        fallo = 5
    return fallo


def pedido(fruta: str, kilos: int or float, frutas: dict) -> int or float:
    valor = frutas.get(fruta) * kilos
    return round(valor, 2)


if __name__ == "__main__":
    error = 0
    fruteria = {"plátano": 1.35, "manzana": 0.80, "pera": 0.85, "naranja": 0.70}
    try:
        # Entrada
        piezas = str(input(f"¿Que fruta quieres comprar? :\nCatálogo: {list(fruteria.keys())}\n> ")).lower()
        # Proceso
        error = control_stock(piezas, fruteria)
        if error != 0:
            raise ValueError(error)
        peso = input("¿Cuantos kilos? (Formato: 00.00):\n> ").strip()  # Entrada
        error = control_kg(peso)
        if error != 0:
            raise ValueError(error)
        precio = pedido(piezas, float(peso), fruteria)
    # Salida
        print(f"{peso}kg de {piezas} vale {precio}€")

    except ValueError:
        if error == 1:
            print(f"{piezas} tiene caracteres no alfabéticos")
        elif error == 2:
            print(f"{piezas} está mal escrita o no se encuentra en el catálogo de la tienda")
            print(f"Catálogo: {list(fruteria.keys())}")
        elif error == 3:
            print(f"{peso} no es un número (tiene carácteres no digito)")
        elif error == 4:
            print(f"Peso ilegible ({peso})")
        elif error == 5:
            print(f"Peso demasiado chico ({peso})")
