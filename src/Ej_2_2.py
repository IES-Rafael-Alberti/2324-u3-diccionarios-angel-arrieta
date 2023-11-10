"""
Ejercicio 3.2.2¶

Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono
y lo guarde en un diccionario. Después debe mostrar por pantalla
el mensaje <nombre> tiene <edad> años, vive en <dirección> y
su número de teléfono es <teléfono>.
"""


def adecuacion(info: str) -> list:
    datos = info.split(",")
    informacion = []
    for dato in datos:
        informacion.append(dato.strip())
    return informacion


def control(datos: list) -> int:
    """
    Función encargado de controlar la adecuación de los datos introducidos
    ----------------------
    datos: list
        Información a guardar en el diccionario

    return: int
        Número devuelto dependiendo del error que se detecte,
        devuelve 0 si no hay errores. Numeración de los errores:
            1 - Se han introducido más o menos datos de los requeridos
            2 - Hay caracteres no alfabeticos en el nombre
            3 - Hay caracteres no digito en la edad
            4 - Edad ilógica
            5 - Hay caracteres no digito en el telefono
            6 - Longitud del telefono no permitida

    """
    fallo = 0
    import re
    nombre = datos[0]
    edad = datos[1]
    telefono = datos[3]
    if len(datos) != 4:
        fallo = 1
    elif re.search("[^a-zA-Z ÁáÉéÍíÓóÚúÑñ]", nombre) is not None:
        fallo = 2
    elif re.search("\D", edad) is not None:
        fallo = 3
    elif int(edad) < 1:
        fallo = 4
    elif re.search("\D", telefono) is not None:
        fallo = 5
    elif len(telefono) != 9:
        fallo = 6
    return fallo


def agenda(datos: list) -> dict:
    """
    Función que convierte en un contacto los datos introducidos
    ------------------------------------------------------------
    datos: list
        Información a pasar al contacto

    return: dict
        Contacto ya creado
    """
    claves = ["nombre", "edad", "dirección", "teléfono"]
    contacto = {}
    for informacion in datos:
        contacto.update({claves[datos.index(informacion)]: informacion})
    return contacto


if __name__ == "__main__":
    error = 0
    try:
        # Entrada
        info = str(input("Dime tu nombre, edad, dirección y teléfono\ndividido por comas y en ese orden\n> "))
        # Proceso
        info_preparada = adecuacion(info)
        error = control(info_preparada)
        if error != 0:
            raise ValueError(error)
        contacto = agenda(info_preparada)
    # Salida
        print(f"{contacto['nombre']} tiene {contacto['edad']} años, vive en {contacto['dirección']} "
        f"y su número de teléfono es {contacto['teléfono']}")

    except ValueError:
        if error == 1:
            print("No se han intoducido la cantidad de datos adecuados")
        elif error == 2:
            print("Hay caracteres no alfabeticos en el nombre\n"
            "(solo se permiten de la A a la Z en minus y mayus, y espacios ' ')")
        elif error == 3:
            print("Hay caracteres no digito en la edad (escribir edad en numérico. Ej: 27)")
        elif error == 4:
            print("Edad ilógica. (Es menor que 1)")
        elif error == 5:
            print("Formato del telefono no permitido. (Formato admitido: 123456789 )")
        elif error == 6:
            print("Longitud del telefono no admitida. (Formato admitido: 123456789 )")
