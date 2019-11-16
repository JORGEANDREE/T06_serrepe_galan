import os
#declarar valores
nota1,nota2,nota3,promedio=0.0,0.0,0.0,0.0

#pedir variables via argumentos
nota1=float(os.sys.argv[1])
nota2=float(os.sys.argv[2])
nota3=float(os.sys.argv[3])
promedio=(nota1+nota2+nota3)/3

#validacion
aprobado=(promedio>10.5)

#condicional multiple
if(aprobado==True):
    print("APROBADO¡")
#fin_if
else:
    print("desaprobado")
#fin_else
if(promedio>11 and promedio<=15):
    print("bien")
#fin_if
if(promedio>15 and promedio<17):
    print("muy bien")
#fin_if
if(promedio>18 and promedio<=20):
    print("EXCELENTE")
#Fin__if
