"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
"""

#entrada
def ingresar_palabra()->str:
    palabra_ingresada = input("Ingrese una palabra: ")
    while len(palabra_ingresada.strip()) < 1 or palabra_ingresada.isalpha() != True:
        palabra_ingresada = input("Ingrese una palabra: ")
    return palabra_ingresada
#procesado

def calcular_palindromo(palabra_palindroma:str)->bool:
    palabra_partida = list(palabra_palindroma)
    palabra_invertida = palabra_partida[::-1]
    
    if palabra_invertida == palabra_partida:
        return True
    else:
        return False

#salida

def mostras_si_palabra_palindroma(palabra_ingresada:str,resultado_comprobacion:bool)->str:
    if resultado_comprobacion:
        return f"{palabra_ingresada} sí es un palíndromo"
    else:
        return f"{palabra_ingresada}NO es un palíndromo"
    
if __name__ == "__main__":
    #entrada
    palabra_ingresada = ingresar_palabra()
    #procesado
    es_palindromo = calcular_palindromo(palabra_ingresada)
    #salida
    mostrar_resultado = mostras_si_palabra_palindroma(palabra_ingresada,es_palindromo)
    print(mostrar_resultado)