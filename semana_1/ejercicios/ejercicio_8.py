def calculadora_ventas_pan(no_panes_vendidos):
    total_final = no_panes_vendidos * precio_pan_ayer
    return total_final

precio_pan = 3.49
precio_pan_ayer = precio_pan * 0.4
descuento_unidad= precio_pan * 0.6
no_panes_vendidos = float(input("Ingrese el número de panes de ayer vendidos: "))
total_final = round(calculadora_ventas_pan(no_panes_vendidos), 2)

print("Precio de venta unidad: ", precio_pan, "Euros")
print("Valor descontado por unidad: ", descuento_unidad, "Euros")
print("Total a pagar: ", total_final , "Euros")