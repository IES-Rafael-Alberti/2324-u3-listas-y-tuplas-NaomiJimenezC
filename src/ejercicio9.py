"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
"""
#Entrada
def ingresar_palabra()->str:
    palabra_ingresada = input("Ingrese una palabra: ")
    while len(palabra_ingresada.strip()) < 1 or palabra_ingresada.isalpha() != True:
        palabra_ingresada = input("Ingrese una palabra: ")
    return palabra_ingresada
#Procesado

def contador_vocales(palabra_a_contar:str)->dict:
    vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for letra in palabra_a_contar.lower():
        if letra in vocales:
                vocales[letra] += 1
    return vocales

#Salida

def mostrar_conteo(resultado_conteo:dict)-> str:
    mensaje_resultado = "Estos los resultados: \n"
    for vocal,resultado in resultado_conteo.items():
        mensaje_resultado += f"{vocal}= resultado \n"
    return mensaje_resultado
        
if __name__ == "__main__":
    palabra_ingresada = ingresar_palabra()
    
    conteo = contador_vocales(palabra_ingresada)
    
    resultado = mostrar_conteo(conteo)
    
    print(resultado)