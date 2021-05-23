#Realizar un programa que imprima 25 términos de la serie 11 - 22 - 33 - 44, etc. 
# (No se ingresan valores por teclado)

def aumento():
    x = 1
    numero = 11
    while x <= 25:
        print(numero, end = " ")
        numero += 11
        x +=1
    return

aumento()