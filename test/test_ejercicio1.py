from src.ejercicio1 import mostrar_asignaturas_curso

def test_comprobar_mensaje_asignaturas():
    assert mostrar_asignaturas_curso(["Matemáticas","Física","Química","Historia","Lengua"]) == "Las asignaturas de este curso son: Matemáticas,Física,Química,Historia,Lengua."
    
    