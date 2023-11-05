from src.ejercicio9 import contador_vocales


def test_contar_vocales():
    palabra_a_testear = "patata"
    assert contador_vocales(palabra_a_testear) == {"a": 3, "e": 0, "i": 0, "o": 0, "u": 0}   
    
contador_vocales("patata")