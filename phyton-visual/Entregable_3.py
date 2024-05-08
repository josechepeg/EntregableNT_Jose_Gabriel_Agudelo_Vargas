

Num_usuarios = [1,2,3,4,5]


def imprimir_tabla_usuarios(usuarios):
    
    print("NumeroUsuario\tNombre\tApellido\tContraseña\tTeléfono\tCorreo")

    
    for usuario in usuarios:
        id, nombre, apellido, contraseña, telefono, correo = usuario
        print(f"{id}\t{nombre}\t{apellido}\t{contraseña}\t{telefono}\t{correo}")
        
if __name__ == "__main__":
 
    lista_usuarios = []

    
    for id_usuario in range(len(Num_usuarios)):
        nombre = input(f"Ingrese el nombre del usuario {id_usuario}: ")
        apellido = input(f"Ingrese el apellido del usuario {id_usuario}: ")
        contraseña = input(f"Ingrese la contraseña del usuario {id_usuario}: ")
        telefono = input(f"Ingrese el teléfono del usuario {id_usuario}: ")
        correo = input(f"Ingrese el correo del usuario {id_usuario}: ")

       
        lista_usuarios.append((id_usuario, nombre, apellido, contraseña, telefono, correo))

   
    imprimir_tabla_usuarios(lista_usuarios)
     