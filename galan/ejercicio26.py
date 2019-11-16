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


#condicional simple
if(peso<50):
    print("EL PESO ES MINIMO")
#fin_if
if(peso>=50 and peso<100):
    print("EL PESO ES MEDIANO")
#fin_if
if(peso>=100 and peso<150):
    print("EL PESO ES MAXIMO")
#fin_if