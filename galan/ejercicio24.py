import os
#declarar variables
paneton,empanadas,chocolate,total=0,0,0,0

#pedir las variables via argumentos
paneton=int(os.sys.argv[1])
empanadas=int(os.sys.argv[2])
chocolate=int(os.sys.argv[3])
total=paneton+empanadas+chocolate

#impresion
print("#########################################")
print("###############VENTA NAVIDEÑA############")
print("# N-panetones:",paneton)
print("# N-empanadas:",empanadas)
print("# litros de chocolate:",chocolate)
print("# total$:",total)
print("########################################")

#condicional multiple
if(total<100):
    print("GANASTE UN PAVO")
#fin_if
if(total>=100 and total<200):
    print("GANASTE UN ARBOL DE NAVIDAD")
#fin_if
if(total>=200 and total<400):
    print("GANASTE UNA CENA NAVIDEÑA")
#fin_if