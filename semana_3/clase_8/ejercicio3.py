#fibonacci
def fibonacci(numero):
    #validacion
    n = numero
    if n < 0 :
        return "numero erroneo"
    
    if n == 0 :
        return 1

    #inicializacion
    respuesta = 0
    fib_2 = 0 #fib(n-2)
    fib_1 = 1#fib(n-1)

    #condicion
    while n > 2: 
        respuesta = fib_1 + fib_2
        print(respuesta, end=" ")
        fib_2 = fib_1
        fib_1 = respuesta
        n -= 1
        
    return respuesta
    
fibonacci(5)


    



