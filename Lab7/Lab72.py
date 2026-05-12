# Generar una matriz identidad de orden N (N debe ser par)

n = int(input("Ingresa un numero par para el orden de la matriz: "))

# Verificar que sea par
if n % 2 != 0:
    print("El numero no es par, intenta de nuevo.")
else:
    # Crear la matriz con puros ceros
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(0)
        matriz.append(fila)

    # Poner 1 en la diagonal
    for i in range(n):
        matriz[i][i] = 1

    # Imprimir la matriz
    print("\nMatriz identidad de orden", n)
    for fila in matriz:
        print(fila)