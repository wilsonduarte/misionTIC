#Realizar un programa que lea los lados de n triángulos, e informar: 
# a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), 
# isósceles (dos lados iguales), o escaleno (ningún lado igual) 
# b) Cantidad de triángulos de cada tipo.

def tipo_de_triangulo():
    n = int(input("Ingrese el número de triángulos: "))
    x = 1 
    cant1 = 0
    cant2 = 0
    cant3 = 0
    while x <= n:
        lado_1 = int(input("Ingrese la longitud del lado 1: "))
        lado_2 = int(input("Ingrese la longitud del lado 2: "))
        lado_3 = int(input("Ingrese la longitud del lado 3: "))
        if lado_1==lado_2 and lado_2==lado_3 and lado_1==lado_3:
            print("El triángulo es equilátero")
            cant1 += 1
        elif lado_1 == lado_2 or lado_2 == lado_3 or lado_1 == lado_3:
            print("El triángulo es isóceles")
            cant2 += 1
        elif lado_1 != lado_2 and lado_2 != lado_3 and lado_1 != lado_3:
            print("El triángulo es escaleno")
            cant3 += 1
        x += 1
    print("Equiláteros: ", cant1)
    print("Isóceles: ", cant2)
    print("Escalenos: ", cant3)

tipo_de_triangulo()