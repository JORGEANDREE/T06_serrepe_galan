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

#condicional simple
if(aprobado==True):
    print("APROBADO!")
#fin_if
