#leer un numero entero y determinar si es terminado en 4
def end_entero(entero):
    ultimo_numero = entero[-1]
    
    if ultimo_numero == "4":
        return "es terminado en 4"
    else:
        return "no es terminado en 4"

entero = input("Ingrese el número entero: ")
print("El número", entero, end_entero(entero))