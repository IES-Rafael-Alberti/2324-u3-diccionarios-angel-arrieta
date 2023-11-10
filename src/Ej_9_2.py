"""
Ejercicio 3.2.9¶

Escribir un programa que gestione las facturas pendientes de cobro de una empresa.
Las facturas se almacenarán en un diccionario donde la clave de cada factura
será el número de factura y el valor el coste de la factura.
El programa debe preguntar al usuario si quiere añadir una nueva factura,
pagar una existente o terminar.
Si desea añadir una nueva factura se preguntará por el número de factura
y su coste y se añadirá al diccionario.
Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario.
Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada
hasta el momento y la cantidad pendiente de cobro.

            elif error == 3:  # Más de un '.' en el dinero
                print(f"Importe mal introducido en intento de nueva factura: {nueva_factura}")
"""


def control_factura(factura: str) -> int:
    """
    Función que controla la adecuación de una nueva factura antes
    de insertarla en la contabilidad de la empresa
    -----------------
    factura: str
        Referencia del dinero que se ha de pagar de cierta adquisición

    return: int
        Número devuelto dependiendo del error que se detecte,
        devuelve 0 si no hay errores. Numeración de los errores:
            0 - El formato de la factura es correcto
            1 - El formato de la factura es incorrecto
            2 - Carácter no digito encontrado en algún valor de la factura
            3 - El identificativo no puede empezar por 0
            4 - Formato del dinero inválido
    """
    fallo = 0
    import re
    if re.search(":", factura) is None:
        fallo = 1
    elif factura.count(":") > 1:
        fallo = 1
    else:
        factura_desglosada = []
        for dato in factura.split(":"):
            factura_desglosada.append(dato.strip())
        identificativo, dinero = factura_desglosada
        if len(identificativo) == 0 or len(dinero) == 0:
            fallo = 1
        elif re.search("\D", identificativo) is not None:
            fallo = 2
        elif re.search("[^\d.]", dinero) is not None:
            fallo = 2
        elif re.search("^0", identificativo) is not None:
            fallo = 3
        elif dinero.count(".") > 1:
            fallo = 4
    return fallo


def control_identificador(identidad: str) -> int:
    """
    Función que controla la adecuación del identificador antes
    de pagarla en la contabilidad de la empresa
    ---------------------
    identidad: str
        Referencia que asocia a una compra el importe qué se debe pagar

    return: int
        Número devuelto dependiendo del error que se detecte,
        devuelve 0 si no hay errores. Numeración de los errores:
            0 - El formato de la identidad es correcto
            5 - La identidad introducida esta vacía
            6 - Carácter no digito encontrado en la identidad
    """
    fallo = 0
    import re
    if len(identidad) < 1:
        fallo = 5
    elif re.search("\D", identidad) is not None:
        fallo = 6
    return fallo


def recoger_identificadores(facturas_clientes: dict) -> list:
    lista_identificadores = list(facturas_clientes.keys())
    return lista_identificadores


def deuda_clientes(facturas: dict) -> int:
    suma_total = 0
    importes_compras = list(facturas.values())
    for valor in importes_compras:
        suma_total += valor
    return round(suma_total, 2)


if __name__ == "__main__":
    contabilidad = {}
    error = 0
    dinero_cobrado = 0
    opcion = ""
    # Proceso
    while opcion != 0:
        try:
            opcion = int(input("\nContabilidad Revilofe S.A.\n"  # Entrada
                               "________________________________\n"
                               f"{len(contabilidad)} facturas almacenadas\n"
                               "--------------------------------\n"
                               "1 - Añadir factura\n"
                               "2 - Pagar factura\n"
                               "0 - Salir del programa\n> "))
            if opcion == 1:
                if len(contabilidad) == 0:
                    identificadores = ""
                else:
                    identificadores = recoger_identificadores(contabilidad)
                nueva_factura = str(input("\nFormato para añadir factura: {nºidentificación: importe}\n"
                                          f"Identificadores existentes: {identificadores}\n> "))  # Entrada
                error = control_factura(nueva_factura)
                if error != 0:
                    raise ValueError(error)
                identificador, importe = nueva_factura.split(":")
                if identificadores.count(identificador) > 0:
                    print("\nIdentificador existente. Facturación invalidada")
                else:
                    contabilidad.update({int(identificador.strip()): float(importe.strip())})
                    if len(contabilidad) == 0:
                        pendiente = 0
                    else:
                        pendiente = deuda_clientes(contabilidad)
                    print(f"\n{dinero_cobrado} importe ya cobrado. {pendiente} por cobrar")
            elif opcion == 2:
                if len(contabilidad) == 0:
                    identificadores = ""
                else:
                    identificadores = recoger_identificadores(contabilidad)
                factura_que_pagar = str(input("\nIndique que factura le van a pagar\n"  # Entrada
                                              f"Identificadores existentes: [{identificadores}]\n> "))
                error = control_identificador(factura_que_pagar)
                if error != 0:
                    raise ValueError(error)
                factura_que_pagar = int(factura_que_pagar.strip())
                if identificadores.count(factura_que_pagar) == 0:
                    print("\nFactura inexistente. Cobro invalidado")
                else:
                    dinero_cobrado += contabilidad.get(factura_que_pagar)
                    contabilidad.pop(factura_que_pagar)
                    if len(contabilidad) == 0:
                        pendiente = 0
                    else:
                        pendiente = deuda_clientes(contabilidad)
                    print(f"\nFactura {factura_que_pagar} pagada. {dinero_cobrado} importe ya cobrado. "
                          f"{pendiente} por cobrar")
            # Salida
            elif opcion == 0:
                print("\nAdios, vuelva pronto")
            else:
                print("\nOpción no reconocida")

        except ValueError:
            if error == 1:
                print(f"\nFormato de factura incorrecto: {nueva_factura}.\n"
                      "Ejemplos válidos: [66: 40.75] ó [007051: 178.33]")
            elif error == 2:
                print(f"\nNo digito encontrado en intento de nueva factura: {nueva_factura}")
            elif error == 3:
                print(f"\nEl identificador en el nuevo intento de factura no puede empezar por 0: {nueva_factura}")
            elif error == 4:
                print(f"\nImporte mal introducido en intento de nueva factura: {nueva_factura}")
            elif error == 5:
                print("\nIntroduzca al menos un identificador")
            elif error == 6:
                print(f"\nNo digito encontrado en la factura a pagar: {factura_que_pagar}")

