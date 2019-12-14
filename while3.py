#INPUT
vocal=""
vocal_invalidad=(vocal!="a" and vocal!="e" and vocal!="i" and vocal!="o" and vocal!="u")
#Mientras vocal invalida
while(vocal_invalidad):
    vocal=str(input("ingrese vocal:"))
    vocal_invalidad=(vocal!="a" and vocal!="e" and vocal!="i" and vocal!="o" and vocal!="u")
#fin_while
print("vocal valida",vocal)
