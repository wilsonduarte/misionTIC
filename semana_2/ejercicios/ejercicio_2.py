def calcular_factorial(entero):
    entero = int(entero)
    if entero <= 1:
        return 1
    factorial = entero * calcular_factorial(entero-1)
    return factorial 
    
entero = input("Ingrese un número entero positivo: ")

factorial = calcular_factorial(entero)
print("El factorial de: ", entero, "es: ", factorial)
