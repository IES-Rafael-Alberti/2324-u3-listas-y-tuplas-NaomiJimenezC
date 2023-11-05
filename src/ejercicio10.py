"""
Escribir un programa que almacene en una lista los siguientes precios: 50, 75, 46, 22, 80, 65, 8 y muestre por pantalla el menor y el mayor de los precios.
"""

#Procesado
def ordenar_precios(lista_precios:list):
    lista_precios.sort()
#Salida
def mostrar_precios_ordenados(lista_precios:list)->str:
    return f"Estos son los precios ordenados: {lista_precios}"

if __name__ == "__main__":
    lista_precios = [50, 75, 46, 22, 80, 65, 8]
    
    #procesado
    ordenar_precios(lista_precios)
    #salida
    mostrar_precios_ordenados = mostrar_precios_ordenados(lista_precios)
    print(mostrar_precios_ordenados)