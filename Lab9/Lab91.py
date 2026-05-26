#Parte A: Clases Abstractas e Interfaces
#Clase Abstracta en Python
from abc import ABC, abstractmethod

class Vehicle(ABC): #Heredar de ABC la hace abstracta

    @abstractmethod
    def arrancar(self):
        """Método abstracto: obligatorio implementar hijo."""
        pass

    def pitar(self):
        """Método normal: ya tiene lógica heredable."""
        print("¡Beep beep!")

class Moto(Vehicle):
    def arrancar(self):
        print("La moto ha arrancado.")
       
#Uso
#mi_vehiculo = Vehicle() #ERROR: no se puede instanciar
mi_moto = Moto()
mi_moto.arrancar() #Imprime: La moto ha arrancado.
mi_moto.pitar()    #Imprime: ¡Beep beep!