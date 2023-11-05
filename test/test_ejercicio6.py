from src.ejercicio6 import *


def test_quitar_aprobados():
    asignaturas_con_sus_notas = [("Matemáticas",8),("Lengua",4),("Física",6),("Química",8),("Historia",2)]
    assert quitar_aprobados(asignaturas_con_sus_notas) == [("Lengua",4),("Historia",2)]