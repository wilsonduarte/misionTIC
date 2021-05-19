def calculo_descuentos(cliente):
    
    data = {"nombre": cliente['nombre']}
    data['agujas'] = 0.0
    data['escolares'] = 0.0
    data['hogar'] = 0.0

    total = cliente['agujas'] + cliente['escolares'] + cliente['hogar']
    
    if cliente['nacional']:
        if total >= 200000000:
            data['agujas'] = 10.0
            data['escolares'] = 10.0
            data['hogar'] = 10.0
        elif cliente['agujas'] > 70000000 and cliente['escolares'] > 30000000 and cliente['hogar'] > 40000000 :
            data['agujas'] = 7.0
            data['escolares'] = 7.0
            data['hogar'] = 7.0
        elif (cliente['agujas'] > 70000000 or cliente['escolares'] > 30000000 or cliente['hogar'] > 40000000) :
            if cliente['agujas'] > 70000000 :
                data['agujas'] = 5.0
            if cliente['escolares'] > 30000000 :
                data['escolares'] = 5.0
            if cliente['hogar'] > 40000000 :
                data['hogar'] = 5.0
    else:
        if total >= 100000:
            data['agujas'] = 8.0
            data['escolares'] = 8.0
            data['hogar'] = 8.0
        elif cliente['agujas'] > 25000 and cliente['escolares'] > 10000 and cliente['hogar'] > 15000 :
            data['agujas'] = 5.0
            data['escolares'] = 5.0
            data['hogar'] = 5.0
        elif (cliente['agujas'] > 25000 or cliente['escolares'] > 10000 or cliente['hogar'] > 15000) :
            if cliente['agujas'] > 25000 :
                data['agujas'] = 3.0
            if cliente['escolares'] > 10000 :
                data['escolares'] = 3.0
            if cliente['hogar'] > 15000 :
                data['hogar'] = 3.0

    return data


cliente = {
    "nombre": "César Díaz",
    "nacional": True,
    "agujas": 70000000.0,
    "escolares": 30000000.0,
    "hogar": 40000000.0
}
result = calculo_descuentos(cliente)
print(result)

