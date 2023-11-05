from src.ejercicio10 import ordenar_precios



def test_ordenar_precios():
    precios = [50, 75, 46, 22, 80, 65, 8]
    ordenar_precios(precios)
    
    assert precios == [8,22,46,50,65,75,80]
    