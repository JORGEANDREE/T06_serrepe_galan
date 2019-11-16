import os
#declarar variables
condicional_simple,condicional_doble,condicional_multiple,tarea=0,0,0,0

#pedir las variables via argumentos
condicional_simple=int(os.sys.argv[1])
condicional_doble=int(os.sys.argv[2])
condicional_multiple=int(os.sys.argv[3])
tarea=condicional_simple+condicional_doble+condicional_multiple

#impresion
print("#################################")
print("###############TRABAJO06############")
print("# N-condicinal simple",condicional_simple)
print("# N-condiconal doble:",condicional_doble)
print("# N-condicinal multiple:",condicional_multiple)
print("# TAREA:",tarea)
print("#################################")

#validacion
completado=(tarea>=60)

#condicional simple
if(completado==True):
    print("TAREA COMPLETADA")
#fin_if
