class Matematicas:
    def __init__(self, numero):
       self.numero = numero
    
    def calcular_factorial(self):
        factorial = 1
        for i in range(1, self.numero +1):
            factorial *= i
        return factorial
num = int(input("Introduce un número entero: "))
operación = Matematicas(num)
print(f"El factorial de {num} es: {operación.calcular_factorial()}")