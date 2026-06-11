#Convertir metros a millas usando POO
class Conversor:
    def __init__(self):
        # Tomamos en cuenta el factor de conversión básico (1 metro = 0.00062137 millas)
        self.factor = 0.00062137

    def metros_a_millas(self, metros):
        # Operación directa multiplicando por el factor
        resultado = metros * self.factor
        return resultado

# --- PROGRAMA PRINCIPAL ---
# 1. Creamos la "máquina" conversora
mi_conversor = Conversor()

# 2. Pedimos los metros al usuario por consola (usando float para los decimales)
metros_ingresados = float(input("Ingrese la longitud en metros: "))

# 3. Usamos el objeto para hacer el cálculo
millas_calculadas = mi_conversor.metros_a_millas(metros_ingresados)

print("La longitud en millas es:")
print(millas_calculadas)