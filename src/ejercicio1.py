"""
Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista y la muestre por pantalla.
"""

#Entrada
#Procesado
def crear_lista_asignaturas()->list:
    return ["Matemáticas","Física","Química","Historia","Lengua"]
#Salida
def mostrar_asignaturas_curso(asignaturas:list)->str:
    mensaje_asignaturas = "Las asignaturas de este curso son: "
    for asignatura in asignaturas:
        if asignatura != asignaturas[-1]:
            mensaje_asignaturas += asignatura + ","
        else:
            mensaje_asignaturas += asignatura + "."
    return mensaje_asignaturas

if __name__ == "__main__":
    asignaturas = crear_lista_asignaturas()
    mensaje_asignaturas = mostrar_asignaturas_curso(asignaturas)
    
    print(mensaje_asignaturas)