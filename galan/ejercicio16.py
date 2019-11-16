import os
#declarar variables
#calcular el peso
peso,masa,gravedad=0.0,0.0,0.0

#pedir las variables via argumentos
masa=float(os.sys.argv[1])
gravedad=float(os.sys.argv[2])
peso=masa*gravedad

#mostrar valores
print("la masa es:",masa)
print("la gravedad es:",gravedad)
print("el peso es:",peso)

#validacion
peso_maximo=(peso>80)

#condicional doble
if(peso_maximo==True):
    print("EL PESO ES MAXIMO")
#fin_if
else:
    print("EL PESO ES MINIMO")
#fin_else
