#Solicitar el ingreso de una clave por teclado y almacenarla en una cadena de caracteres. 
# Controlar que el string ingresado tenga entre 10 y 20 caracteres para que sea válido, 
# en caso contrario mostrar un mensaje de error.
def clave():
    contraseña = input("Ingrese la contraseña entre 10 y 20 caracteres: ")
    if len(contraseña) < 10 or len(contraseña) > 20:
        print("Error, La contraseña debe tener entre 10 y 20 caracteres")
    else :
        print("La contraseña tiene: ", len(contraseña), " caracteres")
clave()
