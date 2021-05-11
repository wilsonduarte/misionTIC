def imprime_valor_movil(caracter):
    #algoritmo
    if caracter == "a" or caracter == "A":
        return "android"
    elif caracter == "i" or caracter == "I":
        return "IOS"
    else:
        return "Opcion inválida"

    
print(imprime_valor_movil(""))
print(imprime_valor_movil("A"))
print(imprime_valor_movil("a"))
print(imprime_valor_movil("i"))
print(imprime_valor_movil("I"))
print(imprime_valor_movil("ñ"))
print(imprime_valor_movil("aA"))