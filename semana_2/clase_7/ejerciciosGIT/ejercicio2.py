#A un trabajador le pagan según sus horas trabajadas por una tarifa de pago por hora. 
# Si la cantidad de horas trabajadas es mayor 40 horas. La tarifa se incrementa en un 50% 
# para las horas extras. Calcular el salario del trabajador dadas las horas trabajadas 
# y la tarifa ingresadas por el usuario.
def salario_trabajador(horas, tarifa):
    if horas <= 40: 
        
        return horas * tarifa
    else:
        hora_extra = (horas - 40) * (tarifa * 2)
        
        return (40 * tarifa) + hora_extra


horas = int(input("ingrese las horas trabajadas: "))
tarifa = int(input("Ingrese la tarifa: "))
print("El salario del trabajador es", salario_trabajador(horas, tarifa))
