#INPUT
peso=0
peso_invalido=(peso<25 or peso>60)
#mientras el peso sea invalido
while(peso_invalido):
    peso=int(input("ingrse su peso:"))
    peso_invalido=(peso<25 or peso>60)
#fin_while
