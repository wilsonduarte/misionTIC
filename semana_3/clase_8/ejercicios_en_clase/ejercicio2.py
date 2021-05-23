#factorial de n
def factorial(numero):
    if numero < 0:
        return "Número erróneo"
    respuesta = 1
    while numero > 0:
        respuesta *= numero 
        numero -= 1
    return respuesta;

print(factorial(6))