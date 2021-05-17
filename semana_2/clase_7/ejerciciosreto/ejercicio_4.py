#Leer un número entero de dos dígitos menor que 20 y determinar si es primo.
def numero_primo(entero):
    if entero > 20 :
        return "El númerono es menor que 20"
    

entero = input("Ingrese un número entero menor que 20: ")
print(numero_primo(entero))
