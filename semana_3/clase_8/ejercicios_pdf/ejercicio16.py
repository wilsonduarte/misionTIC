#Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron. 
# Tener en cuenta que un espacio en blanco es igual a " ", en cambio una cadena vacía es ""
def oracion():
    espacio=0
    frase = str(input("Ingrese la oración: "))
    for letra in frase:
        if letra in " ":
            espacio+=1
    print("se ingresaron ", espacio, " espacios en blanco.")

oracion()