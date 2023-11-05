"""
Escribir un programa que almacene en una lista los números del 1 al 10
y los muestre por pantalla en orden inverso separados por comas.
"""

#Procesado
def invertir_lista(lista_a_invertir:list)->list:
    return sorted(lista_a_invertir,reverse=True)
#Salida

def mostrar_resultado_invertido(numeros_invertidos:list)->str:
    mensaje = "El resultado de la inversión es: "
    for numero in numeros_invertidos:
        if numero != numeros_invertidos[-1]:
            mensaje += str(numero) +","
        else:
            mensaje += str(numero) +"."
    return mensaje

if __name__ == "__main__":
    numeros = [1,2,3,4,5,6,7,8,9,10]
    #Procesado
    numeros_invertidos = invertir_lista(numeros)
    #Salida
    resultado_invertido = mostrar_resultado_invertido(numeros_invertidos)
    print(resultado_invertido)
    