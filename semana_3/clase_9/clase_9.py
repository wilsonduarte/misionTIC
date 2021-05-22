for letra in "Wilson Duarte":
    print(letra, end = " ")
print()
for numero in range(10):
    print(10-numero)
print("Boooooom!")

for numero in range (50):
    print (2 * (numero+1), end = "-")
print()

for letra in "Wilson Duarte":
    if letra in  "aeiouAEIOU":
        print(letra, end = (" "))
print()

#listas
lista = [1, 2.5, "MisiónTIC", [5,6], {"nombre":"wilson", "apellido":"duarte", }, True]

lista = []
lista = list()

nombre = "pepe"
edad = 25
lista = [nombre, edad]
print(lista) #["pepe", 25]

nombres = ["ana", "bernardo"]
edades = [22, 21]
lista = [nombres, edades]
print(lista) #[[ana, bernardo], [22, 21]]

nombres += ["cristina"] #nombres = nombres + ["cristina"]
 

len(lista) #2
len(lista[0]) #3
#len mide la cantidad, ya sea de caracteres o de elementos en una lista
#se puede meter una o varias listas dentro de otra lista

