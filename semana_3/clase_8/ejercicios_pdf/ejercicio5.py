#Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en pantalla 8 - 16 - 24, etc.

def multiplos_ocho():
    multiplo=8
    while multiplo <= 500:
        print(multiplo, end = " ")
        multiplo += 8
    return
multiplos_ocho()