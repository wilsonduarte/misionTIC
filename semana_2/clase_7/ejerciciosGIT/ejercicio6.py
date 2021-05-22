#Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar con
#un mensaje cuál de las dos listas tiene un valor acumulado mayor (mensajes "Lista 1
#mayor", "Lista 2 mayor", "Listas iguales")

def valor_acumulado():
    acumulado1 = sum(lista_1)
    acumulado2 = sum(lista_2)
    if acumulado1 > acumulado2:
        print("Lista 1 mayor")
        
    elif acumulado1 < acumulado2:
        print("Lista 2 mayor")
        
    elif acumulado1 == acumulado2:
        print("Listas iguales")
        

lista_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
lista_2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
valor_acumulado()