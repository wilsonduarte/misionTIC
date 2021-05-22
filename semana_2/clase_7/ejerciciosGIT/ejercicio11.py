#Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos muestre 
# la tabla de multiplicar del mismo (los primeros 12 términos) Ejemplo: Si ingreso 3 deberá 
# aparecer en pantalla los valores 3, 6, 9, hasta el 36.

def tablas_multiplicar():
    numero = int(input("Ingrese un número del 1 al 10: "))
    if numero < 1 or numero > 10:
        return print("El número no está dentro del rango")
    tabla = []
    x = 1
    multiplo = 0
    while x <=12:
        multiplo = multiplo + numero
        tabla.append(multiplo)
        x += 1
    print(tabla)
    return tabla
    
    
tabla = tablas_multiplicar()
for multiplo in tabla:
    print(multiplo)