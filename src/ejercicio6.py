"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. 
Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""
#Entrada
def ingresar_nota_asignatura(lista_asignaturas:list)->list:
    notas_asignaturas = []
    for asignatura in lista_asignaturas:
        nota_ingresada = input(f"INgrese la nota que ha sacado en {asignatura}: ")
        while nota_ingresada.isdecimal() != True:
            nota_ingresada = input(f"INgrese la nota que ha sacado en {asignatura}: ")
        notas_asignaturas.append(int(nota_ingresada))
    return notas_asignaturas
#Procesado
def asociar_nota_con_asignatura(asignaturas:list,notas_asignaturas:list)->list:
    resultados_finales = []
    for notas_finales in zip(asignaturas,notas_asignaturas):
        resultados_finales.append(notas_finales)
    return resultados_finales

def quitar_aprobados(notas_asignaturas:list)->list:
    suspensos = []
    for aprobado in notas_asignaturas:
        if aprobado[1] < 5:
            suspensos.append(aprobado)
    return suspensos
#Salida

def mostrar_suspensos(asignaturas_a_repetir:list)->str:
    mensaje_final = "Las asignaturas que tienes que repetir son: \n"
    for asignatura_a_repetir in asignaturas_a_repetir:
        mensaje_final += f"{asignatura_a_repetir[0]}\n"
    return mensaje_final

if __name__ == "__main__":
    #Entrada
    asignaturas = ["Matemáticas","Física","Química","Historia","Lengua"]
    notas_asignaturas = ingresar_nota_asignatura(asignaturas)
    #Procesado
    notas_asociadas = asociar_nota_con_asignatura(asignaturas,notas_asignaturas)
    suspensos = quitar_aprobados(notas_asociadas)
    #Salida
    mensaje_para_repetidores = mostrar_suspensos(suspensos)
    print(mensaje_para_repetidores)