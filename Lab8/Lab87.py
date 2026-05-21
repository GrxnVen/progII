class Persona:
    def __init__(self, nom, ape):
        self.nombre = nom
        self.apellido = ape
    
    def imprimir_nombre(self):
        print(self.nombre, self.apellido)

p1 = Persona("Fulano", "De tal")
p1.imprimir_nombre()

class Estudiante(Persona):
    pass

x = Estudiante("Mengano", "De tal")
x.imprimir_nombre()