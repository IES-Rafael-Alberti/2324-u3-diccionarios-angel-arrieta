"""
Ejercicio 3.2.5¶

Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso
{'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla
los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos,
donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos.
Al final debe mostrar también el número total de créditos del curso.
"""


def mensaje(curso: dict) -> str:
    mensaje = ""
    claves = list(curso.keys())
    for asignatura in claves:
        mensaje += f"{asignatura} tiene {curso.get(asignatura)} créditos\n"
    return mensaje[:-1]


def total_creditos(curso: dict) -> str:
    total = 0
    creditos = list(curso.values())
    for suma in creditos:
        total += suma
    mensaje = f"Créditos totales del curso: {total}"
    return mensaje


if __name__ == "__main__":
    # Entrada
    creditos_del_curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    # Proceso
    mensaje = mensaje(creditos_del_curso)
    creditos = total_creditos(creditos_del_curso)
    # Salida
    print(f"{mensaje}\n{creditos}")

