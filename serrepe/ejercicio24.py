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

#condicional multiple
if(sueldo<1000):
    print("ganaste un bono de 500 soles")
#fin_if
if(sueldo>=1000 and sueldo<2000):
    print("ganaste un bono de 250 soles")
#fin_if
if(sueldo>=2000 and sueldo<=3000):
    print("ganaste un bono de 100 soles")
#fin_if