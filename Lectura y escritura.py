with open("notas.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Modulo 1: Completado\n")
    archivo.write("Modulo 2: Completado\n")

with open("notas.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:\n" + contenido)