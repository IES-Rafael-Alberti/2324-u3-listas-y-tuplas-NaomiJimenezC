from math import sqrt
"""
Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.
"""

#Entrada
def introducir_muestra_numeros():
    muestra_numero = input("Ingrese una serie de numero separados por comas (1,2,3,4): ")
    lista_numeros_convertidos = muestra_numero.split(",")
    numeros_finales = []
    for numero in lista_numeros_convertidos:
        numeros_finales.append(int(numero))
    return numeros_finales
#Procesado
def calcular_media(lista_numeros:list)->float:
    return sum(lista_numeros)/len(lista_numeros)

def calcular_desviacion_tipica(serie_numeros:list,media:float)->float:
    resultados_sin_raiz_cuadrada = []
    for numero in serie_numeros:
        resultado = (numero-media)**2
        resultados_sin_raiz_cuadrada.append(resultado)
    resultado = sqrt(sum(resultados_sin_raiz_cuadrada)/len(serie_numeros))
    return round(resultado,3)

#Salida

def mostrar_resultados(media:float,desviacion_tipica:float)->str:
    return f"La media es {media} y la desviacion típica es {float}"

if __name__ == "__main__":
    #entrada
    serie_numeros = introducir_muestra_numeros()
    #procesado
    media = calcular_media(serie_numeros)
    desviacion_tipica = calcular_desviacion_tipica(serie_numeros,media)
    #salida
    mostrar_resultados(media,desviacion_tipica)
    print(mostrar_resultados)

