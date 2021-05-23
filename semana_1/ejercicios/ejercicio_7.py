def calcular_peso_paquete(no_payasos, no_munecas):
    peso_total_payasos = peso_payaso * no_payasos
    peso_total_munecas = peso_muneca * no_munecas
    peso_total =peso_total_payasos + peso_total_munecas
    return peso_total


peso_payaso = 112
peso_muneca = 75

no_payasos = int(input("Ingrese el número de payasos vendidos: "))
no_munecas = int(input("Ingrese el número de muñecas vendidas: "))

peso_paquete = (calcular_peso_paquete(no_payasos, no_munecas)) / 100

print("El peso total del paquete es : ", peso_paquete, "kilos")