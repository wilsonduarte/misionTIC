#extraiga en un conjunto los digitos que existen en una frase
frase = "Hello 12345 world 5602"
print({x for x in frase if x in "1234567890"}) #tambien se puede if x.isdigit()
