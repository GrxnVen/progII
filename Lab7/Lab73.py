# Lab 7 - Ejercicio 3
# Herramienta para analizar una cadena de texto

import string

def contar_palabras_unicas(texto):
    # Quitar signos de puntuacion y pasar a minusculas
    for signo in string.punctuation:
        texto = texto.replace(signo, "")
    texto = texto.lower()
    palabras = texto.split()

    # Guardar palabras sin repetir
    unicas = []
    for p in palabras:
        if p not in unicas:
            unicas.append(p)

    return len(unicas)


def palabra_mas_larga(texto):
    # Quitar puntuacion
    for signo in string.punctuation:
        texto = texto.replace(signo, "")
    palabras = texto.split()

    mas_larga = ""
    for p in palabras:
        if len(p) > len(mas_larga):
            mas_larga = p

    return mas_larga


def frecuencia_caracteres(texto):
    texto = texto.lower()

    # Contar letras (sin espacios)
    conteo = {}
    total = 0
    for c in texto:
        if c != " " and c.isalpha():
            total += 1
            if c in conteo:
                conteo[c] += 1
            else:
                conteo[c] = 1

    # Mostrar resultados
    print("\nFrecuencia de caracteres:")
    for letra in sorted(conteo):
        porcentaje = (conteo[letra] / total) * 100
        print(f"  '{letra}': {conteo[letra]} veces ({porcentaje:.2f}%)")


# --- Flujo principal ---
texto = input("Ingresa un texto largo: ")

print("\n===== REPORTE DE TEXTO =====")
print("Palabras unicas:", contar_palabras_unicas(texto))
print("Palabra mas larga:", palabra_mas_larga(texto))
frecuencia_caracteres(texto)
print("============================")