import os
#declarar variables (area de un rectangulo)
base,altura,area=0.0,0.0,0.0

#pedir las variables via argumentos
base=float(os.sys.argv[1])
altura=float(os.sys.argv[2])
area=base*area

#impresion
print("#################################")
print("###############AREA##############")
print("# Base",base)
print("# altura:",altura)
print("# area:",area)
print("#################################")


#condicional multiple
if(area<100):
    print("AREA MINIMA")
#fin_if
if(area>=100 and area<200):
    print("AREA MEDIANA")
#fin_if
if(area>=200 and area<400):
    print("AREA MAXIMA")
#fin_if