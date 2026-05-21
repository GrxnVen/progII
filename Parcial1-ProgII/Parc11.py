contador = 10
def proceso(valor):
    contador = 0
    for i in range(valor):
        contador += 1

    return contador

resultado = proceso(5)
print(contador)
print(resultado)
#!. El programa establece una función que calcula la suma de los números en un rango específico y a continuación muestra tanto una variable global como el resultado de dicha función.
#2. Porque una vive afuera de la función (global) y la otra vive solo adentro (local). No se mezclan.
#3. Significa que la variable solo existe dentro de la función y no afecta ni es afectada por variables con el mismo nombre.
#4. Si usamos global contador: dentro  de la función, entonces la variable contador dentro de la función se referiría a la variable global contador, y cualquier cambio en ella afectaría a la variable global. En este caso, el resultado sería 10 para ambas impresiones, ya que la función modificaría la variable global contador.
#5. Es, en sí, una suma que empieza en 0, luego se le suma 1 por cada iteración del bucle (1, luego 2, luego 3, y ultimo 4) hasta llegar a 5, y eso da como resultado 10.

#Rescribiendo el programa evitando el uso de variables globales:
def proceso(valor):
    contador = 0
    for i in range(valor):
        contador += i  
    return contador

resultado = proceso(5)
print(resultado)