import os
#declarar valores
peso1,peso2,peso3,peso4,peso_total=0.0,0.0,0.0,0.0,0.0

#pedir variables via argumentos
peso1=float(os.sys.argv[1])
peso2=float(os.sys.argv[2])
peso3=float(os.sys.argv[3])
peso4=float(os.sys.argv[4])
peso_total=peso1+peso2+peso3+peso4

#impresion
print("#################################")
print("###############PESO############")
print("# peso1",peso1)
print("# peso2:",peso2)
print("# peso3:",peso3)
print("# peso4:",peso4)
print("# peso total:",peso_total)
print("#################################")

#condicional multiple
if(peso_total<240):
    print("PESO NORMAL!")
#fin_if
if(peso_total>=240 and peso_total<360):
    print("PESO REGULAR")
#fin_if
if(peso_total>=360 and peso_total<450):
    print("SOBREPESO!")
#fin_if