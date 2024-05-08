mi_lista_edad = {19,17,23,28,21,17,64}


lista_nombre = []



for i in mi_lista_edad:
    print(i)


for i in range(len(mi_lista_edad)):

     nombre = input("Agregue un nombre")
     lista_nombre.append(nombre)

     print(lista_nombre)

#for anidado


     for i in lista_nombre:
          for j in mi_lista_edad:
               print(f"Nombre{i} Edad {j}")