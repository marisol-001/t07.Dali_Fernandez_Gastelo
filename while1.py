#INPUT
numero=0
numero_invalido=(numero<20 or numero>60)
#mientras numero sea invalido
while(numero_invalido):
    numero=int(input("ingrese numero:"))
    numero_invalido=(numero<20 or numero>60)
#fin_while
print("numero valido",numero)
