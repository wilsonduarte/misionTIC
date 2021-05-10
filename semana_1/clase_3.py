def refrescos_sobrantes(refrescos_x_caja, no_cajas, no_personas):
    total_refrescos = refrescos_x_caja * no_cajas
    sobrantes = total_refrescos % no_personas
    return sobrantes
     
def precio_por_kilo(peso_empaque, precio_empaque, peso_total = 1000):
    #procesar algoritmo
    precio_gramo = precio_empaque / peso_empaque
    precio_kilo = precio_gramo * peso_total

    #salida
    return round(precio_kilo, 2) 

