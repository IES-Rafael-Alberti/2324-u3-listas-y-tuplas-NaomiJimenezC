"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> sobre cada una 
de las asignaturas de la lista.
"""

#Salida
def decir_asignatura_estudiada(asignatura:str)->str:
    return f"Yo estudio {asignatura}"


if __name__ == "__main__":
    asignaturas = ["Matemáticas","Física","Química","Historia","Lengua"]
    
    for asignatura in asignaturas:
        print(decir_asignatura_estudiada(asignatura))