"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje
En <asignatura> has sacado <nota> donde <asignatura> 
es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
"""

#Entrada
def ingresar_nota_asignatura(lista_asignaturas:list)->list:
    notas_asignaturas = []
    for asignatura in lista_asignaturas:
        nota_ingresada = input(f"INgrese la nota que ha sacado en {asignatura}: ")
        while nota_ingresada.isdecimal() != True:
            nota_ingresada = input(f"INgrese la nota que ha sacado en {asignatura}: ")
        notas_asignaturas.append((nota_ingresada))
    return notas_asignaturas
#Procesado

def asociar_nota_con_asignatura(asignaturas:list,notas_asignaturas:list)->list:
    resultados_finales = []
    for notas_finales in zip(asignaturas,notas_asignaturas):
        resultados_finales.append(notas_finales)
    return resultados_finales

#Salida

def mostrar_notas_asignatura(notas_finales:list)->str:
    mensaje_final = ""
    for nota_final in notas_finales:
        mensaje_final += f"En {nota_final[0]} has sacado {nota_final[1]} \n"
    return mensaje_final

if __name__ == "__main__":
    #Entrada
    asignaturas = ["Matemáticas","Física","Química","Historia","Lengua"]
    notas = ingresar_nota_asignatura(asignaturas)
    #Procesado
    notas_asociadas = asociar_nota_con_asignatura(asignaturas,notas)
    #Salida
    mensaje_notas = mostrar_notas_asignatura(notas_asociadas)
    print(mensaje_notas)