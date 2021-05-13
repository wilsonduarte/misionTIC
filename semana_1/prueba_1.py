def simular_recaudo_producto(precio_base, cantidad, porcentaje_actual=0):
    
    valor_recaudado = precio_base * cantidad * ((19 - porcentaje_actual)/100)
    return round(valor_recaudado, 2)

precio_base = float(input("ingrese el precio base del producto: "))
cantidad = int(input("Ingrese la cantidad que se espera vender: "))
porcentaje_actual = int(input("Ingrese el porcentaje de iva del producto: ") or "0")
print(porcentaje_actual)
print("El valor que se recaudaría para el producto simulado es: ", calcular_recaudo_producto(precio_base, cantidad, porcentaje_actual))
