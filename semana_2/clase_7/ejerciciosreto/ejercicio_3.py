#Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.
def determinar_pares(entero):
    if len(entero) < 2 or len(entero) > 2:
        return "Error, el número no tiene dos dígitos"
    ultimo_numero = int(entero[-1])
    penultimo_numero = int(entero[0])

    if  ultimo_numero % 2 == 0 and penultimo_numero % 2 == 0 :
        return "Los dos dígitos son pares"
    else:
        return "Los dos dígitos no son pares"


entero = input("Ingrese un número entero de dos dígitos: ")
print(determinar_pares(entero))