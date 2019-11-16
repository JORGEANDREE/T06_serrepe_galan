import os
#declarar variables
correo,contraseña,correos_enviados,correos_recibidos,correos_excesivos="","",0,0,0

#pedir las variables via argumentos
correo=os.sys.argv[1]
contraseña=os.sys.argv[2]
correos_enviados=int(os.sys.argv[3])
correos_recibidos=int(os.sys.argv[4])

#validacion
correos_excesivos=(correos_recibidos+correos_enviados>100)
#impresion
print("#################################")
print("###############GMAIL#############")
print("# Email:",correo)
print("# contraseña:",contraseña)
print("####### BIENVENIDO A GMAIL ######")
print("# correos enviados:",correos_enviados)
print("# correos reciidos:",correos_recibidos)
print("# salir ")
print("#################################")

#condicional simple
if(correos_excesivos==True):
    print("Bandeja llena !ELIMINE ARCHIVOS! ")
#fin_if