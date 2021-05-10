from clase_3 import refrescos_sobrantes, precio_por_kilo


var_1 = refrescos_sobrantes(24, 9, 56)
var_2 = refrescos_sobrantes(50, 2, 30)
personas = 10+30
var_3 = refrescos_sobrantes(12, 50, personas)

#print("Sobran", sobrantes, "refrescos")
print(var_1, var_2, var_3)


print("El precio por kilo es: ", precio_por_kilo(100, 5.95))
print("El precio por kilo es: ", precio_por_kilo(120, 6.25, 1))
print("El precio por kilo es: ", precio_por_kilo(500, 30 ))