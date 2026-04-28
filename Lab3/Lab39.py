# Definimos una cadena de texto para las pruebas
frase = "bienvenido al laboratorio de programación"

# 1. Usando capitalize(): Pone la primera letra en mayúscula
print(frase.capitalize())

# 2. Usando center(): Centra el texto rodeándolo de un carácter (ej. asteriscos)
# El primer número es el ancho total de la línea
print(frase.center(60, "*"))

# 3. Usando count(): Cuenta cuántas veces aparece una letra o palabra
cantidad_aes = frase.count("a")
print(f"La letra 'a' aparece {cantidad_aes} veces en la frase.")