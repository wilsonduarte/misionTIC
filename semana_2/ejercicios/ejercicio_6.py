def calcular_masa_corporal(peso, estatura):
    imc = peso / estatura**2
    return imc

estatura = float(input("Ingrese su estatura en metros: "))
peso = float(input("Ingrese su peso en kilos: "))
imc = round(calcular_masa_corporal(peso, estatura), 2)
print("Tu índice de masa corporal es: ", imc)