producto = []

producto1 = [1, "Hot Wheels", "8500", 3, "Juguetes de carros"]
producto2 = [2, "T.rex jurassic world", "399.000", 1, "Juguetes de dinosaurios"]
producto3 = [3, "Papitas de limón", "2800", 4, "grasas y comida"]
producto4 = [4, "Chocolatina Jet", "1200", 7, "Chocolates"]
producto5 = [5, "Guitarra eléctrica", "3.500.000", 1, "Instrumentos"]

producto.append(producto1)
producto.append(producto2)
producto.append(producto3)
producto.append(producto4)
producto.append(producto5)

campos = 5

i = 0

while i < campos:
    valor = input("Ingrese campo")
    producto.append(valor)
    i+=1


encabezados = ("Id", "Nombre", "Precio", "Cantidad", "Categoria")

for encabezado in encabezados:
        print(encabezado, end="\t")
print()
for item in producto:
    print(item, end="\t")