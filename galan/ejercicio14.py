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

#validacion
cena_navideña=(total>100)

#condicional doble
if(cena_navideña==True):
    print("GANASTE UNA CENA NAVIDEÑA")
#fin_if
else:
    print("ganste un paneton")
#fin_else