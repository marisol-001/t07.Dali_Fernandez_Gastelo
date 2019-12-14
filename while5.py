#INPUT
nota=0
nota_invalida=(nota<1 or nota>20)
#mientras nota es invalida
while(nota_invalida):
    nota=int(input("ingrese nota del alumno:"))
    nota_invalida=(nota<0 or nota>20)
#fin_while
print("nota valida",nota)


