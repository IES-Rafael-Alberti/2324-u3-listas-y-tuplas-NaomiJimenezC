
def test_eliminacion_de_letras_multiplos_de_3():
    abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    borrar_letras_multiplos_de_3(abecedario)
    assert abecedario == ["b", "c", "e", "f","h", "i","k", "l", "n", "ñ", "p", "q","s", "t","v", "w", "y", "z"]