#Escribir un programa que pida al usuario un número entero y muestre por pantalla un 
# triángulo rectángulo como el de más abajo, de altura el número introducido.
#1
#3 1
#5 3 1
#7 5 3 1
#9 7 5 3 1
def triangulo_impares():
    numero=int(input("Ingrese el numero: "))
    for n in range(numero):
        print((n+3),(n+1))
triangulo_impares()