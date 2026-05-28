 
from abc import ABC, abstractmethod
import math
 
class FuncionMatematica(ABC):
    @abstractmethod
    def evaluar(self, x):
        pass
 
class FuncionLineal(FuncionMatematica):
    def __init__(self, m, b):
        self.m = m
        self.b = b
    def evaluar(self, x):
        return self.m * x + self.b
 
class FuncionCuadratica(FuncionMatematica):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def evaluar(self, x):
        return self.a * (x ** 2) + self.b * x + self.c
 
class FuncionExponencial(FuncionMatematica):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def evaluar(self, x):
        return self.a * math.exp(self.b * x)
 
# Lista de funciones, evaluadas todas en un mismo valor x
funciones = [FuncionLineal(2, 3), FuncionCuadratica(1, -2, 1), FuncionExponencial(2, 0.5)]
valor_x = 4
 
print(f"Evaluando funciones para x = {valor_x}:")
for func in funciones:
    print(f"Resultado de {type(func).__name__}: {func.evaluar(valor_x):.2f}")