#Leer un número entero de dos dígitos y determinar si ambos dígitos son pares
def enteros_pares(entero):
    if entero < 10 or entero > 99:
        return "El número no es de dos dígitos"
    else:
        entero = str(entero)
        if int(entero[0]) % 2 == 0 and int(entero[1]) % 2 == 0:
            return "Los dos dígitos son pares"
        else:
            return "Los dos dígitos no son pares"

entero = int(input("Ingrese un entero de dos dígitos: "))
print(enteros_pares(entero))
