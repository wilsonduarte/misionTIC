def validar_nota (nota):
    if nota < 0 or nota > 5:
        return "Nota fuera de rango"


#algoritmo
    if nota >= 3:
        mensaje = "Ganó el curso"
    else :
        mensaje = "Perdió el curso"
    return f"su nota es: {mensaje}"

nota = float(input("Ingrese la nota definitiva: "))
print(validar_nota(nota))

