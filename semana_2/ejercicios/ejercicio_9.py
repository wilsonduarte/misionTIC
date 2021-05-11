def calculadora_ahorros(dinero_ahorro):
    ahorro_total = ano_1 + ano_2 + ano_3
    return ahorro_total


dinero_ahorro = float(input("ingrese la cantidad en pesos que desea depositar en su cuenta: "))

ano_1 = round(dinero_ahorro + (dinero_ahorro * 0.04), 2)
ano_2 = round(ano_1 + (ano_1 * 0.04), 2)
ano_3 = round(ano_2 + (ano_2 * 0.04),2)
calculadora_ahorros(dinero_ahorro)
print("tras el primer año, usted ahorrará: ", ano_1, "pesos")
print("tras el segundo año, usted ahorrará: ", ano_2, "pesos")
print("tras el tercer año, usted ahorrará: ", ano_3, "pesos")