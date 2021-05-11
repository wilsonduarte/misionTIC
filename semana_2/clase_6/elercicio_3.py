def definir_edad(nombre, edad):
    if edad < 0 :
      return "Error"

#algoritmo

    if edad < 18 :
        return nombre + " Es menor de edad"
    else :
        return nombre + " es mayor de edad"


nombre = input("Ingrese el nombre de la persona: ")
edad = int(input("Ingrese la edad de la persona: "))
print(definir_edad(nombre, edad))