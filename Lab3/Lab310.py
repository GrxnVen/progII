# Definimos diferentes cadenas para probar las validaciones
dato1 = "12345"
dato2 = "python"
dato3 = "Hola Mundo"

# 1. Usando isnumeric(): Verifica si todos los caracteres son números
print(f"¿Es '{dato1}' un número? {dato1.isnumeric()}")

# 2. Usando islower(): Verifica si todo el texto está en minúsculas
print(f"¿Está '{dato2}' todo en minúsculas? {dato2.islower()}")

# 3. Usando isalpha(): Verifica si el texto contiene solo letras (sin espacios ni números)
# Nota: dará False en dato3 porque tiene un espacio
print(f"¿Contiene '{dato3}' solo letras? {dato3.isalpha()}")