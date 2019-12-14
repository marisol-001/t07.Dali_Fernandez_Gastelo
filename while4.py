#INPUT
marca_computadora=""
marca_invalida=(marca_computadora!="lenovo" and marca_computadora!="HP" and marca_computadora!="cybert")
while(marca_invalida):
    marca_computadora=str(input("ingrese marca de computadora:"))
    marca_invalida=(marca_computadora!="lenovo" and marca_computadora!="HP" and marca_computadora!="cybert")
#fin_while
print("marca valida",marca_computadora)
