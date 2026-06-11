class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

class EstudianteBecado(Estudiante):
    def __init__(self, nombre, nota, beca):
        super().__init__(nombre, nota)
        self.beca = beca

class Curso:
    def __init__(self):
        self.lista = []

mi_curso = Curso()
est1 = Estudiante("Ana", 85)
est2 = EstudianteBecado("Luis", 92, 50)
est3 = Estudiante("Carlos", 78)
est4 = Estudiante("Marta", 92)

mi_curso.lista.append(est1)
mi_curso.lista.append(est2)
mi_curso.lista.append(est3)
mi_curso.lista.append(est4)

mayor = 0
nombre_mayor = ""

for est in mi_curso.lista:
    if est.nota > mayor:
        mayor = est.nota
        nombre_mayor = est.nombre

print(nombre_mayor)
print(mayor)