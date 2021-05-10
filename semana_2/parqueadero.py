def ubicar_bus(total_parqueaderos, numero_bus):
    #validar las entradas
    if total_parqueaderos % 3 != 0:
        return "Error: el número de parqueaderos no es múltiplo de 3"
    if numero_bus > total_parqueaderos:
        return "Error: el número de buses excede el total de parqueaderos"
    total_lotes = 3
    parqueaderos_lote = total_parqueaderos / total_lotes

    if numero_bus <= parqueaderos_lote:
        return 1
    if numero_bus <= 2 * parqueaderos_lote:
        return 2
    if numero_bus <= 3 * parqueaderos_lote:
        return 3
    pass

print(ubicar_bus(3, 1))
print(ubicar_bus(3, 2))
print(ubicar_bus(3, 3))
print(ubicar_bus(90, 90))
print(ubicar_bus(90, 91))
