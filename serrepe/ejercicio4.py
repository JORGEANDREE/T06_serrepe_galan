import os
#declarar variables
trabajador,meses_trabajando,pago_por_mes,sueldo="",0,0.0,0.0

#pedir las variables via argumentos
trabajador=os.sys.argv[1]
meses_trabajando=int(os.sys.argv[2])
pago_por_mes=float(os.sys.argv[3])
sueldo=meses_trabajando*pago_por_mes
#impresion
print("#################################")
print("###############SUELDO############")
print("# Trabajador:",trabajador)
print("# Meses de trabajo:",meses_trabajando)
print("# Pago por mes:",pago_por_mes)
print("# sueldo:",sueldo)
print("#################################")

#validacion
bono=(sueldo>2000)

#condicional simple
if(bono==True):
    print("ganaste un bono de 500 soles")
#fin_if
