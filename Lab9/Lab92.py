#Interfaces
from abc import ABC, abstractmethod

class Encriptador(ABC): #Actúa como interfaz pura.
    @abstractmethod
    def encriptar(self, datos: str) -> str:
        pass

    @abstractmethod
    def desencriptar (self, datos: str):
        pass

class EncriptadorAES(Encriptador):
    def encriptar(self, datos: str):

        def desencriptar(self, datos):
             return datos.replace("AES(", "").replace(")", "")
