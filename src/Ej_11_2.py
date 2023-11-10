"""
Ejercicio 3.2.11¶

El directorio de los clientes de una empresa está organizado en una cadena de texto
como la de más abajo, donde cada línea contiene la información del nombre, email,
teléfono, nif, y el descuento que se le aplica. Las líneas se separan
con el carácter de cambio de línea \n y la primera línea contiene los nombres
de los campos con la información contenida en el directorio.

"nif;nombre;email;teléfono;descuento\n
01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n
71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\"

Escribir un programa que genere un diccionario con la información del directorio, donde cada
elemento corresponda a un cliente y tenga por clave su nif y por valor otro diccionario
con el resto de la información del cliente.
Los diccionarios con la información de cada cliente tendrán como claves los nombres de los campos
y como valores la información de cada cliente correspondientes a los campos.
Es decir, un diccionario como el siguiente

{'01234567L': {'nombre': 'Luis González', 'email': 'luisgonzalez@mail.com', 'teléfono': '656343576', 'descuento': 12.5},
 '71476342J': {'nombre': 'Macarena Ramírez', 'email': 'macarena@mail.com', 'teléfono': '692839321', 'descuento': 8.0}}
"""


def dividir(cadena_bruta: str) -> tuple:
    listado = cadena_bruta.split("\n")
    cabecera = listado.pop(0)
    return cabecera, listado


def personas(listado: list) -> list:
    informacion = []
    for linea in listado:
        datos = linea.split(";")
        informacion.append(datos)
    return informacion


def diccionario(asociacion: list, info_personas: list) -> dict:
    diccionario = {}
    for persona in info_personas:
        individuo = {}
        for valor in persona:
            if valor == persona[0]:
                nif = persona[0]
            else:
                individuo.update({asociacion[persona.index(valor)]: valor})
        diccionario.update({nif: individuo})
    return diccionario


if __name__ == "__main__":
    # Entrada
    directorio = ("nif;nombre;email;teléfono;descuento\n"
                  "01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n"
                  "71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n"
                  "63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n"
                  "98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7")
    # Proceso
    referencia, directorio_dividido = dividir(directorio)
    claves = referencia.split(";")
    datos_personas = personas(directorio_dividido)
    clientes = diccionario(claves, datos_personas)
    # Salida
    print(clientes)

