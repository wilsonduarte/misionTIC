def tarifas(estrato):
    if estrato == 1:
        return {"cargo_fijo" : 2500, "metros" : 2200, "basuras" : 5500}
    elif estrato == 2:
        return {}

def factura_agua (estrato, metros):
    #validar
    if estrato < 1 or estrato > 6 :
        return "Error, estrato fuera de rango"
    if metros < 0 :
        return "Error, los metros consumidos deben ser mayores a cero"
    
    #algoritmo
    if estrato == 1 :
        cargo_fijo = 2500
    elif estrato == 2 :
        cargo_fijo = 2800
    elif estrato == 3 :
        cargo_fijo = 3000
    elif estrato == 4 :
        cargo_fijo = 3300
    elif estrato == 5 :
        cargo_fijo = 3700
    elif estrato == 6 :
        cargo_fijo = 4400
    
    if estrato == 1:
        consumo = metros * 2200 
    elif estrato == 2:
        consumo = metros * 2350
    elif estrato == 3:
        consumo = metros * 2600
    elif estrato == 4:
        consumo = metros * 3400
    elif estrato == 5:
        consumo = metros * 3900
    elif estrato == 6:
        consumo = metros * 4800
    
    if estrato == 1:
        basuras_alcantarillado = 5500
    elif estrato == 2:
        basuras_alcantarillado = 6200
    elif estrato == 3:
        basuras_alcantarillado = 7400
    elif estrato == 4:
        basuras_alcantarillado = 8600
    elif estrato == 5:
        basuras_alcantarillado = 9700
    elif estrato == 6:
        basuras_alcantarillado = 11000

    return cargo_fijo + consumo + basuras_alcantarillado

print("El total de la factura es: ", factura_agua(1, 1))
print("El total de la factura es: ", factura_agua(4, 3))
print("El total de la factura es: ", factura_agua(7, 2))


