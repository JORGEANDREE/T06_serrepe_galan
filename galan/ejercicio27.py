import os
#declarar variables
mensajes,notificaciones,llamadas,total=0,0,0,0

#pedir las variables via argumentos
mensajes=int(os.sys.argv[1])
notificaciones=int(os.sys.argv[2])
llamadas=int(os.sys.argv[3])
total=mensajes+llamadas+notificaciones

#impresion
print("#################################")
print("##############CELULAR############")
print("# mensajes",mensajes)
print("# notificaciones:",notificaciones)
print("# llamadas:",llamadas)
print("# total:",total)
print("#################################")


#condicional multiple
if(total<90):
    print("Tienes Pocas notofocaciones")
#fin_if
if(total>=90 and total<150):
    print("el numero de notifcaciones es alta")
#fin_if
if(total>=150 and total<250):
    print("excesivas notificaciones")
#fin_if