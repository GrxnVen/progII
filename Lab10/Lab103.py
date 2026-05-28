with open("archivo_demo.txt", "a") as f:
    f.write("¡Ahora el archivo tiene más contenido!")

with open("archivo_demo.txt") as f:
    print(f.read())

with open("archivo_demo.txt", "w") as f:
    f.write("¡Ups! ¡He borrado el contenido")

with open("archivo_demo.txt") as f:
    print(f.read())