"""
Ejercicio 3.2.6¶

Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona
(por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario.
Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""


def control_nombre(nombre: str) -> int:
    """
    Función que revisa que el nombre sea lógico
    -------------
    nombre: str
        nombre a revisar

    return: int
        Número devuelto dependiendo del error que se detecte,
        devuelve 0 si no hay errores. Numeración de los errores:
            0 - si el nombre es lógico.
            1 - si el nombre contiene algún carácter que no sea alfabético, espacio y vocal mayúscula o minúscula con acento
    """
    fallo = 0
    import re
    if re.search("[^A-Za-z ÁáÉéÍíÓóÚú]", nombre) is not None:
        fallo = 1
    return fallo


def control_edad(edad: str) -> int:
    """
    Función que revisa que la edad sea lógica
    -------------
    edad: str
        edad a revisar

    return: int
        Número devuelto dependiendo del error que se detecte,
        devuelve 0 si no hay errores. Numeración de los errores:
            0 - si la edad es lógica
            2 - si el formato de la edad no es correcto o si se encuentran carácteres no dígito
            3 - si la edad no tiene sentido
    """
    fallo = 0
    import re
    if re.search("^[0-9]$|^[0-9][1-9]$|^[0-9][0-9][0-9]$", edad) is None:
        fallo = 2
    elif int(edad) < 0 or int(edad) > 130:
        fallo = 3
    return fallo


def control_sexo(sexo: str) -> int:
    """
    Función que revisa que el sexo sea lógico
    -------------
    sexo: str
        cadena a revisar

    return: int
        Número devuelto dependiendo del error que se detecte,
        devuelve 0 si no hay errores. Numeración de los errores:
            0 - si el sexo es lógico
            4 - si el sexo no es reconocible
    """
    fallo = 0
    import re
    if re.search("^hombre$|^mujer$", sexo) is None:
        fallo = 4
    return fallo


def control_telefono(telefono: str) -> int:
    """
    telefono: str

    return: int
        Número devuelto dependiendo del error que se detecte,
        devuelve 0 si no hay errores. Numeración de los errores:
        0 - si el teléfono es lógico
        5 - si el teléfono no se adecua al formato [123456789]
    """
    fallo = 0
    import re
    if re.search("^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$", telefono) is None:
        fallo = 5
    return fallo


def datacion(datos: dict) -> str:
    informe = ""
    claves = list(datos.keys())
    for info in claves:
        informe += f"{info}: {datos.get(info)}\n"
    return informe[:-1]


if __name__ == "__main__":
    informe_personal = {}
    error = 0
    try:
        # Entrada
        nombre = str(input("Introduzca el nombre del sujeto del informe\n> "))
        error = control_nombre(nombre)
        if error != 0:
            raise ValueError(error)
        informe_personal.update({"Nombre": nombre})
        anadido = datacion(informe_personal)
        print(anadido)

        edad = str(input("Edad del sujeto (3 dígitos máximo)\n> "))
        error = control_edad(edad)
        if error != 0:
            raise ValueError(error)
        informe_personal.update({"Edad": int(edad)})
        anadido = datacion(informe_personal)
        print(anadido)

        sexo = str(input("Sexo del sujeto (hombre o mujer)\n> "))
        error = control_sexo(sexo)
        if error != 0:
            raise ValueError(error)
        informe_personal.update({"Sexo": sexo})
        anadido = datacion(informe_personal)
        print(anadido)

        telefono = str(input("Teléfono del sujeto\n> "))
        error = control_telefono(telefono)
        if error != 0:
            raise ValueError(error)
        informe_personal.update({"Teléfono": telefono})
        anadido = datacion(informe_personal)
        print(anadido)

        correo = str(input("Correo electrónico del sujeto\n> "))
        error = control_correo(correo)
    except ValueError:
        if error == 1:
            print(f"{nombre} contiene carácteres ilógicos para un nombre")
        elif error == 2:
            print(f"{edad} contiene carácteres ilógicos para un número o no se acepta el formato (3 dígitos máximo)")
        elif error == 3:
            print(f"{edad} es una edad ilógica para un ser humano")
        elif error == 4:
            print(f"{sexo} no es un sexo reconocido por el programa (hombre o mujer)")
        elif error == 5:
            print(f"{telefono} no es un formato de telefono aceptado (Ejemplo: [123456789])")

