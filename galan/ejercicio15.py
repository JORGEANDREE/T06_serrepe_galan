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

#validacion
maxima=(area>70)

#condicional doble
if(maxima==True):
    print("AREA MAXIMA")
#fin_if
else:
    print("AREA MINIMA")
#fin_else