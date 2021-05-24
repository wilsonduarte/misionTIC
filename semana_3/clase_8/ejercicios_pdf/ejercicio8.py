#Realizar un programa que permita cargar dos listas de 15 valores cada una. 
# Informar con un mensaje cuál de las dos listas tiene un valor acumulado mayor 
# (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales") 
# Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.

#Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida 
# de la base y la altura de un triángulo. El programa deberá informar: 
# a) De cada triángulo la medida de su base, su altura y su superficie. 
# b) La cantidad de triángulos cuya superficie es mayor a 12.

def triangulos():
    x = 1 
    base = 0
    altura = 0
    triangulos_mayores = 0
    resultados = []
    n=int(input("¿Cuantos triángulos ingresará?: "))
    while x <= n:
        base = int(input("ingrese la medida de la base: "))
        altura = int(input("ingrese la altura del triángulo: "))
        superficie = (base * altura) / 2
        if superficie > 12 :
            triangulos_mayores += 1
        resultado = "Triangulo # " + str(x) +  ": Base: " + str(base) + ", Altura: " + str(altura) + ", superficie: " + str(superficie)
        resultados.append(resultado)
        x = x + 1
    print("La cantidad de superficies mayores a 12 es: ", triangulos_mayores)
    return resultados


resultados = triangulos()
for resultado in resultados : 
    print(resultado)