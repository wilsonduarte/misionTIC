#La empresa ABCD tiene hasta 100 empleados. La compañía decide crear un número
#de identificación único UID para cada uno de sus empleados. La compañía le ha
#asignado la tarea de validar los UIDsgenerados aleatoriamente. Un UID válido debe
#cumplir con las siguientes reglas:
#* Debe contener por lo menos dos letras mayúsculas en el alfabeto inglés.
#* Debe tener por lo menos 3 dígitos.
#* Contener únicamente dígitos alfanuméricos.
#* No tener repeticiones.
#* Contener exactamente 10 caracteres.

uids = ["B1CD102354", "B1CDEF2354"]
for uid in uids:
    cond = []
    # Debe contener por lo menos dos letras mayúsculas en el alfabeto inglés.
    cond.append( len(list(filter(lambda x: x.isupper(), list(uid)))) >= 2 )
    # Debe tener por lo menos 3 dígitos.
    cond.append( len(list(filter(lambda x: x.isdigit(), list(uid)))) >= 3 )
    # Contener únicamente dígitos alfanuméricos.
    cond.append( len(list(filter(lambda x: not(x.isalnum()), list(uid)))) == 0 )
    # No tener repeticiones.
    cond.append( len(uid) == len(set(uid)) )
    # Contener exactamente 10 caracteres.
    cond.append( len(uid) == 10 )

    print("Válido") if all(cond) else print("Inválido")