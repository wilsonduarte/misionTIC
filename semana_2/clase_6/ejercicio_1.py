#ejercicio 1
def mensaje_nota(nota):
    #validacion de entradas
    if nota < 0 or nota > 5.0:
        return "Nota fuera de rango"

    #algoritmo
    felicitaciones = " "
    if nota >= 4:
        felicitaciones = "Felicitaciones!"
    return f"Su nota es {nota} {felicitaciones}"


nota = float(input("Ingrese la nota definitiva: "))
print(mensaje_nota(nota))


