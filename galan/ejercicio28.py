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

#condicional multiple
if(completado==True):
    print("TAREA COMPLETADA")
#fin_if
else:
    print("TAREA IMCOMPLETA")
#fin_else
if(tarea>=1 and tarea<30):
    print("MEDIA TAREA COMPLETADA")
#fin_if
if(tarea>=30 and tarea<50):
    print("TE FALTA POCO ¡TU PUEDES TER,INAR TU TAREA!")
#fin_if