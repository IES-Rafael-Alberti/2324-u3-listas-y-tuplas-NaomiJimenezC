"""
Escribir un programa que almacene las matrices A=(123456) y B=(−100111)
en una lista y muestre por pantalla su producto. Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.

"""

#Procesado


def multiplicar_vectores(vector1,vector2)->list:
    resultado = [[0,0],[0,0]]
    for fila_vector1 in range(len(vector1)):
        for columna_vector2 in range(len(vector2[0])):
            for fila_vector2 in range(len(vector2)):
                resultado[fila_vector1][columna_vector2] += vector1[fila_vector1][fila_vector2] * vector2[fila_vector2][columna_vector2]
    return resultado
#Salida

def mostrar_resultado(resultado_multiplicado:list)->str:
    return f"El resultado de multiplicar las dos matrices es de {resultado_multiplicado}"

if __name__ == "__main__":
    #entrada
    vector1 = [[1,2,3],[4,5,6]]
    vector2 = [[-1,0],[0,1],[1,1]]
    #procesado
    resultado = multiplicar_vectores(vector1,vector2)
    #salida
    mensaje_resultado = mostrar_resultado(resultado)
    print(mensaje_resultado)
    
    