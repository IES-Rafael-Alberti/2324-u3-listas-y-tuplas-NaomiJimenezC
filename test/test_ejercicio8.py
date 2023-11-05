from src.ejercicio8 import calcular_palindromo


def test_calcular_palindromo_correcto():
    palabra_palindroma = "radar"
    
    assert calcular_palindromo(palabra_palindroma) == True

def test_calcular_palindromo_incorrecto():
    palabra_palindroma = "tomate"
    assert calcular_palindromo(palabra_palindroma) == False