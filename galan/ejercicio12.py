import os
#declarar variables
edad_papa,edad_mama,edad_hijo,suma_edades=0,0,0,0

#pedir las variables via argumentos
edad_papa=int(os.sys.argv[1])
edad_mama=int(os.sys.argv[2])
edad_hijo=int(os.sys.argv[3])
suma_edades=edad_hijo+edad_mama+edad_papa

#impresion
print("#################################")
print("###############EDADES############")
print("# edad del papa",edad_papa)
print("# edad de la mama:",edad_mama)
print("# edad del hijo:",edad_hijo)
print("# suma de edades:",suma_edades)
print("#################################")

#validacion
superado=(suma_edades>120)

#condicional doble
if(superado==True):
    print("LA SUMA DE EDADES HA SUPERADO LOS 100 AÑOS")
#fin_if
else:
    print("LA SUMA DE LAS EDADES NO HA SUPERADO LOS 100 AÑOS")
#fin_else