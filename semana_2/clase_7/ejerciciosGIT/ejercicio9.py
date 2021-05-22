#Desarrollar un programa que solicite la carga de 10 números e imprima la suma 
# de los últimos 5 valores ingresados.

def suma_ultimos():
    x = 1
    numero = 0
    numeros = []
    while x <=10:
        numero = int(input("Ingrese el número "+str(x)+": "))
        numeros.append(numero)
        x = x+1

    suma = sum(numeros[4:9])
    print(suma)
    return suma

suma_ultimos()
