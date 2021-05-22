#Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida 
# de la base y la altura de un triángulo. El programa deberá informar: 
# a) De cada triángulo la medida de su base, su altura y su superficie. 
# b) La cantidad de triángulos cuya superficie es mayor a 12.

def triangulos():
    x = 1 
    base = 0
    altura = 0
    resultados = []
    n=int(input("¿Cuantos triángulos ingresará?: "))
    while x <= n:
        base = int(input("ingrese la medida de la base: "))
        altura = int(input("ingrese la altura del triángulo: "))
        superficie = (base * altura) / 2
        resultado = "Triangulo # " + str(x) +  ": Base: " + str(base) + ", Altura: " + str(altura) + ", superficie: " + str(superficie)
        resultados.append(resultado)
        x = x + 1
    return resultados


resultados = triangulos()
for resultado in resultados : 
    print(resultado)

