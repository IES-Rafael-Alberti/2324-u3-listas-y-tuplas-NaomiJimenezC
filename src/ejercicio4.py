"""
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""

#Entrada
def meter_numeros_ganadores()->list:
    numeros_ganadores = []
    while len(numeros_ganadores) != 6:
        numero_ganador = input("Ingrese un número ganador: ")
        if numero_ganador.isdecimal():
            numeros_ganadores.append(int(numero_ganador))
    return numeros_ganadores
#Procesado
def ordenar_numeros(numeros_a_ordenar:list) -> list:
    return sorted(numeros_a_ordenar)
#Salida

def mostrar_numeros_ganadores(numeros_ganadores_ordenados:list)->str:
    mensaje_ganadores = "Estos son los números ganadores: \n"
    for numero_ganador in numeros_ganadores_ordenados:
        mensaje_ganadores += str(numero_ganador) + "\n"
    return mensaje_ganadores
if __name__ == "__main__":
    #Entrada
    numeros_ganadores_introducidos = meter_numeros_ganadores()
    #Procesado
    ganadores_ordenados = ordenar_numeros(numeros_ganadores_introducidos)
    #Salida
    anuncio_de_los_ganadores = mostrar_numeros_ganadores(ganadores_ordenados)
    print(anuncio_de_los_ganadores)