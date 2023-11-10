"""
Ejercicio 3.2.10¶

Escribir un programa que permita gestionar la base de datos de clientes de una empresa.
Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF,
y el valor será otro diccionario con los datos del cliente
(nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True
si se trata de un cliente preferente.
El programa debe preguntar al usuario por una opción del siguiente menú:
(1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente,
(4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar.
En función de la opción elegida el programa tendrá que hacer lo siguiente:
    1. Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
    2. Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
    3. Preguntar por el NIF del cliente y mostrar sus datos.
    4. Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
    5. Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
    6. Terminar el programa.
"""


def comprobar_adecuacion(campo: str, info: str) -> int:
    """
    Función que se encarga que según el campo, la información asociada
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
        1 - si el NIF no sigue el formato debido
        2 - si el nombre contiene algún carácter que no sea alfabético, espacio y vocal mayúscula o minúscula con acento
        3 - si el formato de dirección es incorrecto
        4 - si la vía de la dirección no está registrada correctamente
        5 - si en el nombre de la dirección se encuentran carácteres no palabra
        6 - si el teléfono no se adecua al formato [123456789]
        7 - si el correo electrónico no se adecua al formato [individuo@nombredominio.dominio]
        8 - si alguna parte del correo electrónico contiene carácteres no permitidos
        9 - si el campo preferente no es booleano
    """
    fallo = 0
    import re
    if campo == "NIF":
        if re.search("^[1-9][0-9]{8}[A-Z]$", info) is None:
            fallo = 1
    elif campo == "nombre":
        if re.search("[^A-Za-z ÁáÉéÍíÓóÚúÑñ]", info) is not None:
            fallo = 2
    elif campo == "dirección":
        if re.search("/", info) is None:
            fallo = 3
        elif info.count("/") > 1:
            fallo = 3
        else:
            via, direccion = info.split("/")
            if re.match("C[.]|Call[.]|Cam[.]|Carr[.]|Avd[.]|Avda[.]|Pl[.]|Urb[.]|Trav[.]", via.strip()) is None:
                fallo = 4
            elif re.search("[^A-Za-z 0-9ÁáÉéÍíÓóÚúÑñº]", direccion.strip()) is not None:
                fallo = 5
    elif campo == "teléfono":
        if len(info) != 9:
            fallo = 6
        elif re.search("\D", info) is not None:
            fallo = 6
    elif campo == "correo":
        if re.search("@", info) is None:
            fallo = 7
        elif info.count("@") > 1:
            fallo = 7
        else:
            nombre, servicio = info.split("@")
            if re.search("[.]", servicio) is None:
                fallo = 7
            elif servicio.count(".") > 1:
                fallo = 7
            else:
                nombre_dominio, dominio = servicio.split(".")
                if re.search("[^A-Za-z_.0-9-]", nombre) is not None:
                    fallo = 7
                elif re.search("[^a-z]", nombre_dominio) is not None:
                    fallo = 7
                elif re.search("[^a-z]", dominio) is not None:
                    fallo = 7
    elif campo == "preferente":
        if re.match("True|False", info) is None:
            fallo = 8
    return fallo


def nombres_clientes(lista_claves: list, diccionario: dict) -> list:
    """ Función que crea una lista con los nombres asociados a los NIFs"""
    duplas_nif_nombre = []
    for dni in lista_claves:
        datos_cliente = diccionario.get(dni)
        nombre = datos_cliente.get("nombre")
        duplas_nif_nombre.append(f"{dni}: {nombre}")
    return duplas_nif_nombre


if __name__ == "__main__":
    clientes = {}
    error = 0
    opcion = ""
    # Proceso
    while opcion != 6:
        try:
            opcion = int(input("\nBBDD de Banco Arrieta\n"  # Entrada
                               "________________________________\n"
                               f"{len(clientes)} clientes\n"
                               "--------------------------------\n"
                               "0 - Salir del programa\n"
                               "1 - Añadir cliente\n"
                               "2 - Eliminar cliente\n"
                               "3 - Mostrar cliente\n"
                               "4 - Listar todos los clientes\n"
                               "5 - Listar clientes preferentes\n"
                               "6 - Terminar\n> "))
            if opcion == 1:
                claves = ["nombre", "dirección", "teléfono", "correo", "preferente"]
                nif = str(input("\nNIF del cliente\n> "))
                error = comprobar_adecuacion("NIF", nif)
                if error != 0:
                    raise ValueError(error)
                cliente = {}
                for clave in claves:
                    nuevo_dato = input(f"\n{clave} del cliente\n> ")  # Entrada
                    error = comprobar_adecuacion(clave, nuevo_dato)
                    if error != 0:
                        raise ValueError(error)
                    if clave == "preferente":
                        if nuevo_dato == "True":
                            nuevo_dato = True
                        elif nuevo_dato == "False":
                            nuevo_dato = False
                    cliente.update({clave: nuevo_dato})
                clientes.update({nif: cliente})
            elif opcion == 2:
                if len(clientes) == 0:
                    print("\n No hay clientes para eliminar")
                else:
                    print(f"\nNIFS: {list(clientes.keys())}")
                    eliminar = str(input("\nQue cliente desea borrar de la base de datos\n> "))
                    error = comprobar_adecuacion("NIF", eliminar)
                    if error != 0:
                        raise ValueError(error)
                    clientes.pop(eliminar)
            elif opcion == 3:
                if len(clientes) == 0:
                    print("\n No hay clientes para mostrar")
                else:
                    print(f"\nNIFS: {list(clientes.keys())}")
                    buscar = str(input("\nQue cliente desea mostrar de la base de datos\n> "))
                    error = comprobar_adecuacion("NIF", buscar)
                    if error != 0:
                        raise ValueError(error)
                    informacion = "\n"
                    datos_brutos = clientes.get(buscar)
                    for clave in datos_brutos:
                        informacion += f"{clave}: {datos_brutos.get(clave)}\n"
                    print(informacion[:-1])
            elif opcion == 4:
                if len(clientes) == 0:
                    print("\n No hay clientes para mostrar")
                else:
                    mensaje = "\nClientes:"
                    identificadores = list(clientes.keys())
                    nombres = nombres_clientes(identificadores, clientes)
                    for referencia in nombres:
                        mensaje += f"\n{referencia}"
                    print(mensaje)
            elif opcion == 5:
                if len(clientes) == 0:
                    print("\n No hay clientes para mostrar")
                else:
                    identificadores = list(clientes.keys())
                    iden_preferentes = []
                    for nif in identificadores:
                        datos = clientes.get(nif)
                        if datos.get("preferente") is True:
                            iden_preferentes.append(nif)
                    if len(iden_preferentes) == 0:
                        print("\n No hay clientes preferentes")
                    else:
                        mensaje = "\nPreferentes:"
                        clientes_preferentes = nombres_clientes(iden_preferentes, clientes)
                        for referencia in clientes_preferentes:
                            mensaje += f"\n{referencia}"
                        print(mensaje)
            # Salida
            elif opcion == 6:
                print("\nAdios, vuelva pronto")
            else:
                print("\nOpción no reconocida")

        except ValueError:
            if error == 1:
                print("El NIF introducido no sigue el formato debido: [123456789A] (No puede empezar por 0)\n")
            elif error == 2:
                print("El nombre contiene algún carácter que no es alfabético, "
                      "espacio, vocal mayúscula o minúscula con o sin acento\n")
            elif error == 3:
                print("La dirección no sigue el formato debido: [C./, Avda./, ... + nombre dirección y número edificio]\n")
            elif error == 4:
                print("La vía introducida no es reconocida por la Base de datos. Vías Reconocidas:\n"
                      "[C./, Call./, Cam./, Carr./, Avd./, Avda./, Pl./, Urb./, Trav./]\n")
            elif error == 5:
                print("El nombre de la dirección contiene algún carácter que no es palabra, espacio, , º,\n"
                      "vocal mayúscula o minúscula con acento. Carácteres palabra: [A-Za-z]\n")
            elif error == 6:
                print("El teléfono no se adecua al formato debido. Ejemplo: [123456789] (longitud admitida, 9)\n")
            elif error == 7:
                print("El correo electrónico no se adecua al formato debido. Ejemplo:[individuo@nombredominio.dominio]\n")
            elif error == 8:
                print("Alguna parte del correo electrónico contiene carácteres no permitidos. Formato:[individuo@nombredominio.dominio]\n"
                      "Carácteres permitidos: en individuo: [A-Z, a-z, _, ., 0-9, -] en dominio y nombre_dom: [a-z]\n")
            elif error == 9:
                print("Preferente no se puede pasar a tipo booleano")
