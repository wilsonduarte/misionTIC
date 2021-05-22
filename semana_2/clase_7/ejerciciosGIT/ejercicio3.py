#En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar
#un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados
#cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá
#informar el importe que gasta la empresa en sueldos al personal.

def sueldos_empleados():
    x=1
    n=int(input("Cuantos empleados ingresará: "))
    sueldo_bajo = 0
    sueldo_alto = 0
    sueldos_totales = 0

    while x<=n:
        sueldo=int(input("Ingrese el sueldo: "))
        if sueldo >= 100 and sueldo <= 300 :
            sueldo_bajo = sueldo_bajo + 1
            sueldos_totales = sueldos_totales + sueldo
        elif sueldo > 300 :
            sueldo_alto = sueldo_alto + 1
            sueldos_totales = sueldos_totales + sueldo
        x = x + 1
        
    print(sueldo_bajo, "empleados cobran entre $100 y #300")
    print(sueldo_alto, "empleados cobran más de $300")
    print("el importe gastado en sueldos es: ", sueldos_totales)

sueldos_empleados()