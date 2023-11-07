"""
Ejercicio 3.2.1¶

Escribir un programa que guarde en una variable el diccionario
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
pregunte al usuario por una divisa y muestre su símbolo o un mensaje
de aviso si la divisa no está en el diccionario.
"""


def simbolo(divisa: str, divisas: dict) -> str:
    simbolo = divisas.get(divisa)
    return simbolo


def control(divisa: str, divisas: dict) -> int:
    divisa = divisa.lower()
    fallo = 0
    claves = list(divisas.keys())
    if claves.count(divisa) == 0:
        fallo = 1  # No está registrada la divisa
        return fallo
    return fallo


if __name__ == "__main__":
    divisas = {'euro': '€', 'dollar': '$', 'yen': '¥'}
    error = 0
    try:
        #  Entrada
        cual_divisa = str(input("Dime una divisa: "))
        #  Proceso
        error = control(cual_divisa, divisas)
        if error != 0:
            raise ValueError(error)
        simbolo_tu_divisa = simbolo(cual_divisa, divisas)
    #  Salida
        print(f"Símbolo de {cual_divisa}: {simbolo_tu_divisa}")

    except ValueError:
        if error == 1:
            print(f"Tu divisa {cual_divisa} no se encuentra en el diccionario")
