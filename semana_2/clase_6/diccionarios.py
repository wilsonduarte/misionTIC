yo = {
    "nombre" : "Wilson",
    "nacionalidad" : "Colombiano",
    "edad" : 32
}

print(yo)
print("nombre: ", yo["nombre"])
#para modificarlo, se le asigna valor como variable: 
yo["nombre"] = "Wilson Duarte Otero"
print("nombre: ", yo["nombre"])
yo["edad"] += 3

print(yo)

#agregar diccionario a un diccionario
yo["mascota"] = {"nombre" : "Lucho", "edad" : 8} 
print(yo)