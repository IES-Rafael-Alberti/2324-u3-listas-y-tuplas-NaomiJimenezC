from src.ejercicio11 import calcular_producto_escalar

def test_calcular_producto_escalar():
    vector1 = (1,2,3)
    vector2 = (-1,0,2)
    assert calcular_producto_escalar(vector1,vector2) == 5