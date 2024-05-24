

usuarios = {}

def registrar_usuario():

  id_user = int(input("Ingrese el Id"))
  name_user = input("Nombre")
  email_user = input("Correo")
  clave = input("Clave")
  usuarios[id_user] = {"nombre": name_user, "mail": email_user, "clave": clave}




def ver_usuario():
  for key, value in usuarios.items():
     print(key, value)
 

registrar_usuario(); 

registrar_usuario();

ver_usuario();