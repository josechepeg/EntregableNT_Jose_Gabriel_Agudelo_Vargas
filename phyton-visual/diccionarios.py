


producto = {"id": 1, "nombre": "Alpinito", "Precio":1500, "cantidad": 20, "estado": "disponible"}

print(producto["nombre"])

producto.update({"cantidad": 15})

print(producto["cantidad"])

print(len(producto))

for key, value in producto.items():
    print(key, value)


usuario = {}

id_user = int(input("Ingrese el Id"))

usuario.update({"id": id_user})
name_user = input("Nombre")
usuario.update({"nombre": name_user})
email_user = input("Correo")
usuario.update({"mail": email_user})
clave = input("Clave")
usuario.update({"clave": clave})

print(usuario)

usuario.popitem()

print(usuario)