#Se ingresan un conjunto de n alturas de personas por teclado. 
# Mostrar la altura promedio de las personas.

def altura_promedio():
    n = int(input("Cuántos valores desea agregar? "))
    x = 1
    suma = 0
    while x <= n:
        altura = float(input("Ingrese la altura N°"+str(x)+" "))
        suma += altura
        x+=1
    promedio = suma/n
    print("El promedio de alturas es: ", round(promedio, 2), "cms")

altura_promedio()