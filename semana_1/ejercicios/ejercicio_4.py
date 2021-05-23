import math 

def calcular_area(radio):
    area_circulo = (math.pi) * radio**2
    return area_circulo

def calcular_volumen(altura):
    volumen_cilindro = area_circulo * altura
    return volumen_cilindro

radio = float(input("Ingrese el radio del círculo en cms: "))
area_circulo = round(calcular_area(radio), 2)


altura = float(input("Ingrese la altura del cilindro en cms: "))
volumen_cilindro = round(calcular_volumen(altura), 2)

print("El área del círculo es :", area_circulo, "cms2 Y su volumen es: ", volumen_cilindro, "cm3")