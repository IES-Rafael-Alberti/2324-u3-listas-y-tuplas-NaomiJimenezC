"""
Escribir un programa que almacene el abecedario en una lista,
elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
"""
#procesado
def borrar_letras_multiplos_de_3(abecedario:list):
    del abecedario[::3]

#salida
def mostrar_abecedario(abecedario:list):
    return f"Este es el abecedario resultante: {abecedario}"

if __name__ == "__main__":
    #Entrada
    abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    #procesado
    borrar_letras_multiplos_de_3(abecedario)
    #salida
    salida_final= mostrar_abecedario(abecedario)
    print(salida_final)
