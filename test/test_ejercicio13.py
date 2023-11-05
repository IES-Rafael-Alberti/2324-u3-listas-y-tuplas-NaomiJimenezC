from src.ejercicio13 import *
from math import sqrt

def test_calcular_media():
    numeros = [1,2,3,4]
    assert calcular_media(numeros) == 2.5

def calcular_desviacion_tipica(serie_numeros:list,media:float)->float:
    resultados_sin_raiz_cuadrada = []
    for numero in serie_numeros:
        resultado = (numero-media)**2
        resultados_sin_raiz_cuadrada.append(resultado)
    resultado = sqrt(sum(resultados_sin_raiz_cuadrada)/len(serie_numeros))
    return round(resultado,3)
    
def test_calcular_desviacion_tipica():
    numeros = [1,2,3,4]
    media = 2.5
    assert calcular_desviacion_tipica(numeros,media) == 1.118