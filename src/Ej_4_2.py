"""
Ejercicio 3.2.4¶

Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por
pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
"""


def control_formato_fecha(fecha: str) -> int:
    """
    Función para controlar la corrección del formato de la fecha introducida
    ------------------
    El formato inicial debe ser DD/MM/AAAA
    fecha: string
        Fecha a cambiar de formato, el formato inicial debe ser DD/MM/AAAA

    return: int
        Devuelve 1 si la fecha no sigue el formato de
        introducción pedido, devuelve 0 si no hay errores.
    """
    import re
    fallo = 0
    if re.search("[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]", fecha) is None:
        fallo = 1
    return fallo


def adecuar_fecha(fecha: str) -> list:
    fecha_partida = []
    fecha_por_partes = fecha.split("/")
    for dato in fecha_por_partes:
        dato_numerico = int(dato)
        fecha_partida.append(dato_numerico)
    return fecha_partida


def control_fecha(fecha: list) -> int:
    """
    Función para controlar la corrección de la fecha introducida
    ------------------
    fecha: list
        Fecha a cambiar de formato, el formato inicial debe ser DD/MM/AAAA

    return: int
        Número devuelto dependiendo del error que se detecte,
        devuelve 0 si no hay errores. Numeración de los errores:
            2 - El mes no entra dentro de los valores permitidos
            3 - El día no entra dentro de los valores permitidos
            4 - El año no es bisiesto, no hay 29 febrero
            5 - Ese mes solo tiene 30 días
    """
    fallo = 0
    ano = fecha[2]
    mes = fecha[1]
    dia = fecha[0]
    meses_no_31dias = {2: 5, 4: 5, 6: 5, 9: 5, 11: 5}
    if ano % 4 == 0:
        if ano % 100 == 0:
            bisiesto = False
            if ano % 400 == 0:
                bisiesto = True
        else:
            bisiesto = True
    else:
        bisiesto = False
    if mes < 1 or mes > 12:
        fallo = 2
    elif dia < 1 or dia > 31:
        fallo = 3
    elif bisiesto is False and mes == 2:
        if dia == 29:
            fallo = 4
    elif dia == 31:
        fallo = meses_no_31dias.get(mes, 0)
    return fallo


def dividir_fecha(fecha: list) -> tuple:
    numero_dia = fecha[0]
    numero_mes = fecha[1]
    numero_ano = fecha[2]
    return numero_dia, numero_mes, numero_ano


def mes_escrito(lista_meses: dict, clave_mes: int) -> str:
    mes_escrito = lista_meses.get(clave_mes)
    return mes_escrito


if __name__ == "__main__":
    error = 0
    meses = {1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo", 6: "junio", 7: "julio",
                8: "agosto", 9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"}
    try:
        # Entrada
        fecha_introducida = str(input("Reformateador de fecha, introduce una fecha\n(Formato DD/MM/AAAA)\n> "))
        # Proceso
        error = control_formato_fecha(fecha_introducida)
        if error != 0:
            raise ValueError(error)
        fecha_usable = adecuar_fecha(fecha_introducida)
        error = control_fecha(fecha_usable)
        if error != 0:
            raise ValueError(error)
        dia, mes_numerico, ano = dividir_fecha(fecha_usable)
        mes = mes_escrito(meses, mes_numerico)
    # Salida
        print(f"{dia} de {mes} de {ano}")
    except ValueError:
        if error == 1:
            print(f"{fecha_introducida} no sigue el formato pedido (DD/MM/AAAA)")
        elif error == 2:
            print(f"Introduce un mes dentro de lo lógico (entre 1 y 12): {fecha_introducida}")
        elif error == 3:
            print(f"Introduce un día dentro de lo lógico (entre 1 y 31): {fecha_introducida}")
        elif error == 4:
            print(f"Febrero no tiene dia 29, el año no es bisiesto: {fecha_introducida}")
        elif error == 5:
            print(f"Ese més no tiene 31 días: {fecha_introducida}")
