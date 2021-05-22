#Realizar un programa que imprima 25 términos de la serie 11 - 22 - 33 - 44, etc. (No se
#ingresan valores por teclado)
def serie_sucesiva():
    serie = 11
    x =1 
    while x <= 25:
        x = x + 1
        print(serie)
        serie = serie + 11


serie_sucesiva()