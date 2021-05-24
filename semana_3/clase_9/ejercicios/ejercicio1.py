#Escribir un programa que pida al usuario un número entero positivo 
# y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
def enteros():
    entero = int(input("ingrese un entero positivo: "))
    for numero in range(entero, -1, -1):
        print(numero, end = ", ")

enteros()