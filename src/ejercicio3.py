"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje
En <asignatura> has sacado <nota> donde <asignatura> 
es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
"""

#Entrada
def ingresar_nota_asignatura(lista_asignaturas:list)->list:
    asigntara_con_su_nota = []
    for asignatura in lista_asignaturas:
        nota_ingresada = input("INgrese la nota que ha sacado en la asignatura: ")
        while nota_ingresada.isdecimal() != True:
            nota_ingresada = input("INgrese la nota que ha sacado en la asignatura: ")
        asigntara_con_su_nota.append((asignatura,nota_ingresada))
    return asigntara_con_su_nota
#Procesado


#Salida

if __name__ == "__main__":
    print()