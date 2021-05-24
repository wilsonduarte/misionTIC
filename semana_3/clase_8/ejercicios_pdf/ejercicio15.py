#Se cuenta con la siguiente información: Las edades de 5 estudiantes del turno mañana. 
# Las edades de 6 estudiantes del turno tarde. Las edades de 11 estudiantes del turno noche. 
# Las edades de cada estudiante deben ingresarse por teclado. 
# a) Obtener el promedio de las edades de cada turno (tres promedios) 
# b) Imprimir dichos promedios (promedio de cada turno) 
# c) Mostrar por pantalla un mensaje que indique cuál de los tres turnos 
# tiene un promedio de edades mayor.
def estudiantes():
    edades_manana=0
    edades_tarde=0
    edades_noche=0
    
    for f in range(5):
        edadam=int(input("Ingrese la edad del estudiante "+str(f+1)+": "))
        edades_manana += edadam
        
    for f in range(6):
        edadpm=int(input("Ingrese la edad del estudiante "+str(f+1)+": "))
        edades_tarde += edadpm
        
    for f in range(11):
        edadno=int(input("Ingrese la edad del estudiante "+str(f+1)+": "))
        edades_noche += edadno
        
    promedioam = edades_manana/5
    promediopm = edades_tarde/6
    promediono = edades_noche/11
    print("El promedio de la mañana es: ", promedioam)
    print("El promedio de la tarde es: ", promediopm)
    print("El promedio de la noche es: ", promediono)
    if promedioam > promediopm and promedioam > promediono:
        print("La jornada de la mañana tiene mayor promedio de edades")
    elif promediopm > promedioam and promediopm > promediono:
        print("La jornada de la tarde tiene mayor promedio de edades")
    elif promediono > promediopm and promediono > promedioam:
        print("La jornada de la noche tiene mayor promedio de edades")
        

estudiantes()