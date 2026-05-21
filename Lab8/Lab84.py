class Calculadora:
    def sumar(self, a, b):
        return a + b
    
    def multiplicar(self, a, b):
        return a * b
    
calc = Calculadora() # type: ignore
print(calc.sumar(5, 3))
print(calc.multiplicar (4, 7))