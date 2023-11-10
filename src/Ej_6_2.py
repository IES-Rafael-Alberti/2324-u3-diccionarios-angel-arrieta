"""
Ejercicio 3.2.6¶

Escribir un programa que cree un diccionario vacío y lo vaya llenando con información sobre una persona
(por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario.
Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""


def control(campo: str, info: str) -> int:
    """
    Función que se encarga que según el campo, la información a añadir
    sea lógica en ese campo
    -------------
    campo: str
        Campo al que el dato debe adecuarse
    info: str
        Información que se une al campo

    return: int
         Número devuelto dependiendo del error que se detecte,
        devuelve 0 si no hay errores. Numeración de los errores:
        0 - si la información es lógica
        1 - si el nombre contiene algún carácter que no sea alfabético, espacio y vocal mayúscula o minúscula con acento
        2 - si el formato de la edad no es correcto o si se encuentran carácteres no dígito
        3 - si la edad no tiene sentido
        4 - si el sexo no es reconocible
        5 - si el teléfono no se adecua al formato [123456789]
        6 - si el correo electrónico no se adecua al formato [individuo@nombredominio.dominio]
    """
    fallo = 0
    import re
    if campo == "Nombre":
        if re.search("[^A-Za-z ÁáÉéÍíÓóÚúÑñ]", info) is not None:
            fallo = 1
    elif campo == "Edad":
        if re.search("^[0-9]$|^[0-9][0-9]$|^[0-9][0-9][0-9]$", info) is None:
            fallo = 2
        elif int(info) <= 0 or int(info) > 130:
            fallo = 3
    elif campo == "Sexo":
        if re.search("^hombre$|^mujer$", info.lower()) is None:
            fallo = 4
    elif campo == "Teléfono":
        if len(info) != 9:
            fallo = 5
        elif re.search("[^0-9]", info) is not None:
            fallo = 5
    elif campo == "Correo electrónico":
        if re.search("@", info) is None:
            fallo = 6
        elif info.count("@") > 1:
            fallo = 6
        else:
            nombre, servicio = info.split("@")
            if re.search("[.]", servicio) is None:
                fallo = 6
            elif servicio.count(".") > 1:
                fallo = 6
            else:
                nombre_dominio, dominio = servicio.split(".")
                if re.search("[^A-Za-z_.0-9-]", nombre) is not None:
                    fallo = 6
                elif re.search("[^a-z]", nombre_dominio) is not None:
                    fallo = 6
                elif re.search("[^a-z]", dominio) is not None:
                    fallo = 6
    return fallo


def datacion(datos: dict) -> str:
    informe = ""
    campos = list(datos.keys())
    for info in campos:
        informe += f"{info}: {datos.get(info)}\n"
    return informe[:-1]


if __name__ == "__main__":
    informe_personal = {}
    claves = ["Nombre", "Edad", "Sexo", "Teléfono", "Correo electrónico"]
    error = 0
    try:
        for clave in claves:
            # Entrada
            dato = str(input(f"{clave} del sujeto\n> "))
            # Proceso
            error = control(clave, dato)
            if error != 0:
                raise ValueError(error)
            informe_personal.update({clave: dato})
            anadido = datacion(informe_personal)
    # Salida
            print(anadido)

    except ValueError:
        if error == 1:
            print(f"'{dato}' contiene carácteres ilógicos para un nombre")
        elif error == 2:
            print(f"'{dato}' contiene carácteres ilógicos para un número o no se acepta el formato (3 dígitos máximo)")
        elif error == 3:
            print(f"'{dato}' es una edad ilógica para un ser humano")
        elif error == 4:
            print(f"'{dato}' no es un sexo reconocido por el programa (hombre o mujer)")
        elif error == 5:
            print(f"'{dato}' no es un formato de teléfono aceptado (Ejemplo: [123456789])")
        elif error == 6:
            print(f"'{dato}' no es un formato de correo eléctrónico aceptado\n"
                    f"(Ejemplo: [arb0l.3s@natural.es] | Ejemplo minimalista: [a@b.c])")
