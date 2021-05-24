#Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas. 
# Contar la cantidad de vocales. Crear un segundo string con toda la oración en minúsculas 
# para que sea más fácil disponer la condición que verifica que es una vocal.
def alfabeto():
    vocales=0
    frase = input("Ingrese la frase: ")
    frase2 = frase.lower()
    for letras in frase2:
        if letras in "aeiou":
            vocales+=1
    print(frase2)
    print("cantidad de vocales", vocales)
    
alfabeto()