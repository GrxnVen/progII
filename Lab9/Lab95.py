#Métodos de Clase (@classmethod), l alternativa flexible.
class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def crear_anonimo(cls):
        #'cls' se refiere a la clase Usuario, no a una instancia.
        return cls("Anónimo", 0) #Crea un Usuario con datos por defecto

#Uso del contructor alternativo
invitado = Usuario.crear_anonimo()
print(invitado.nombre) #Imprime: Anónimo
print(invitado.edad) #Imprime: 0