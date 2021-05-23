#Escribir un programa que solicite ingresar 10 notas de alumnos 
# y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.

def notas_alumnos():
    x=1
    notas_mayores = 0
    notas_menores = 0
    while x <= 10:
        nota = int(input("Ingrese la nota del alumno "+str(x)+": "))
        
        if nota >= 7:
            notas_mayores += 1
        else :
            notas_menores += 1
        x += 1
    print("Cantidad de alumnos con nota mayor de 7: ", notas_mayores)
    print("Cantidad de alumnos con nota menor de 7: ", notas_menores)
    
    return

notas_alumnos()


