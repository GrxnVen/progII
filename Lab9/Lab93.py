#Parte B: Atributos y Métodos estáticos

class Persona:
    #Atributo estático (compartido por todas las instancias)
    contador = 0

    def __init__(self):
        Persona.contador += 1 #se accede al nombre de la clase