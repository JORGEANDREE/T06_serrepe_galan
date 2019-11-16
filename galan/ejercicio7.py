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

#validacion
bandeja_llena=(total>120)

#condicional simple
if(bandeja_llena==True):
    print("BANDEJA LLENA !REVISE SUS NOTIFICACIONES!")
#fin_if
