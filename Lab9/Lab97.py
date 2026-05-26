#Métodos finales: no se pueden sobrescribir en subclases
from typing import final

class Padre:
    @final
    def metodo_sagrado(self):
        print("No me cambies.")

class Hijo(Padre):
    #Intentar sobrescribir el método final causará un error de linter
    def metodo_sagrado(self): #ERROR: no se puede sobrescribir un método final
        print("Intento cambiar el método sagrado.")
        