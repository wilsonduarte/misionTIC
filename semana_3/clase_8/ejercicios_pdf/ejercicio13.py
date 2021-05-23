#Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.
#Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante. 
# Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.

def coordenadas():
    plano1=0
    plano2=0
    plano3=0
    plano4=0
    n = int(input("Ingrese el número de puntos a ingresar: "))
    for item in range(n): # [0, 1, 2]
        coordenada_x = int(input("Ingrese la coordenada en x: "))
        coordenada_y = int(input("Ingrese la coordenada en y: "))
        if coordenada_x > 0 and coordenada_y > 0:
            plano1+=1
        elif coordenada_x < 0 and coordenada_y > 0:
            plano2+=1
        elif coordenada_x < 0 and coordenada_y < 0:
            plano3+=1
        elif coordenada_x > 0 and coordenada_y < 0:
            plano4+=1
    print("Puntos en el plano 1: ", plano1)
    print("Puntos en el plano 2: ", plano2)
    print("Puntos en el plano 3: ", plano3)
    print("Puntos en el plano 4: ", plano4)

    return
coordenadas()