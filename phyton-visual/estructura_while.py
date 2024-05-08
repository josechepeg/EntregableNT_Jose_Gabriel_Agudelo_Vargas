#Cree un bucle que permita agregar a una lista 5 colores


mi_lista_colores = []

contador_colores = 0

while contador_colores < 5:

    color = input("Agrege un color")

    mi_lista_colores.append(color)

    contador_colores+=1

print(mi_lista_colores)