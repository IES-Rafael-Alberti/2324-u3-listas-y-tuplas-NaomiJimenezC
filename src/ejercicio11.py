"""
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.
"""
#Procesado
def calcular_producto_escalar(vector1:tuple,vector2:tuple)-> int:
    resultados = []
    for producto1,producto2 in zip(vector1,vector2):
        resultados.append(producto1*producto2)
    return sum(resultados)
#Salida

def mostrar_producto_escalar(resultados:int)->str:
    return f"El producto escalar es igual a {resultados}"

if __name__ == "__main__":
    #entrada
    vector1 = (1,2,3)
    vector2 = (-1,0,2)
    
    #procesado
    producto_escalar = calcular_producto_escalar(vector1,vector2)
    #Salida
    mensaje_resultado = mostrar_producto_escalar(producto_escalar)
    
    print(mensaje_resultado)