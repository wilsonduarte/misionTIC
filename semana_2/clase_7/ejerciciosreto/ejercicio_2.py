#Leer un número entero y determinar si tiene 3 dígitos.
def cuantos_digitos(entero):
    
    if len(entero) == 3 :
        return "tiene tres dígitos"
    else:
        return "no tiene tres dígitos"

entero = input("Ingrese un número entero: ")
print("El número ", entero, cuantos_digitos(entero))