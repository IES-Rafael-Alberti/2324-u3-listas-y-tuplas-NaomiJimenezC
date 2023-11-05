from src.ejercicio3 import asociar_nota_con_asignatura

def test_asociar_nota_con_asignatura():
    assert asociar_nota_con_asignatura(["Matemáticas","Física"],[5,5]) == [("Matemáticas",5),("Física",5)]
    