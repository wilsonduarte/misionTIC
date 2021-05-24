#Se realiza la carga de 10 valores enteros por teclado. Se desea conocer: 
# a) La cantidad de valores ingresados negativos. b) La cantidad de valores ingresados positivos. 
# c) La cantidad de múltiplos de 15. d) El valor acumulado de los números ingresados que son pares.
def valores_enteros():
    negativos=0
    positivos=0
    multiplo_15=0
    suma = 0
    for item in range(10): 
        numero = int(input("Ingrese el número "+str(item+1)+":"))
        if numero < 0 :
            negativos += 1
        else:
            positivos += 1
        if numero%15 == 0:
            multiplo_15 += 1
        if numero%2==0:
            suma+=numero
    print("El número de valores negativos es: ", negativos)
    print("El número de valores positivos es: ", positivos)
    print("El número de múltipos de 15 es: ", multiplo_15)
    print("La suma de los pares es: ", suma)
    

valores_enteros()
