def total_factura(valor_sin_iva, porcentaje_iva = 19):
    valor_con_iva = (valor_sin_iva + (valor_sin_iva * (porcentaje_iva / 100)))
    return valor_con_iva

valor_sin_iva = float(input("Ingrese el valor sin iva: "))
porcentaje_iva = input("ingrese el porcentaje de iva: ")
if porcentaje_iva == "":    
    porcentaje_iva = 19
porcentaje_iva = float(porcentaje_iva)

valor_con_iva = total_factura(valor_sin_iva, porcentaje_iva)
print("EL valor total de su factura es: ", valor_con_iva)