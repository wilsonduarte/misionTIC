#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo
#  rectángulo como el de más abajo, de altura el número introducido.
def triangulo():
    numero = int(input("Infrese un numero entero: "))
    for n in range(numero):
        print("*"*(n+1))
triangulo()
