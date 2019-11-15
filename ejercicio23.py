import os
#declarar variables
correo,contraseña,correos_enviados,correos_recibidos,total_correos="","",0,0,0

#pedir las variables via argumentos
correo=os.sys.argv[1]
contraseña=os.sys.argv[2]
correos_enviados=int(os.sys.argv[3])
correos_recibidos=int(os.sys.argv[4])
total_correos=correos_recibidos+correos_enviados

#impresion
print("#################################")
print("###############GMAIL#############")
print("# email:",correo)
print("# contraseña:",contraseña)
print("####### BIENVENIDO A GMAIL ######")
print("# correos enviados:",correos_enviados)
print("# correos reciidos:",correos_recibidos)
print("# salir ")
print("#################################")

#condicional multiple
if(total_correos<10):
    print("bandeja casi vacia")
#fin_if
if(total_correos>20 and total_correos<50):
    print("bandeja media llena")
#fin_if
if(total_correos>60 and total_correos<100):
    print("bandeja llena")
#fin_if