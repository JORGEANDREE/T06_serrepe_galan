import os
#declarar variables
jabones,shampo,acondicionador,pu_jabones,pu_shampo,pu_acondicionador,total=0,0,0,0,0,0,0

#pedir las variables via argumentos
jabones=int(os.sys.argv[1])
shampo=int(os.sys.argv[2])
acondicionador=int(os.sys.argv[3])
pu_acondicionador=int(os.sys.argv[4])
pu_jabones=int(os.sys.argv[5])
pu_shampo=int(os.sys.argv[6])
total=(jabones*pu_jabones)+(shampo*pu_shampo)+(acondicionador*pu_acondicionador)
#impresion
print("#################################")
print("###############COMPRAS###########")
print("# jabones",jabones,"  p.u:",pu_jabones)
print("# shampo:",shampo,"   p.u:",pu_shampo)
print("# acondicinador:",acondicionador, "  pu:",pu_acondicionador)
print("# Total:",total,"$")
print("#################################")

#condicional multiple
if(total<100):
    print("GANASTE UN VALE DE 10$ EN PRODCUTOS DE ASEO PERSONAL!")
#fin_if
if(total>=100 and total<200):
    print("GANASTE UN VALE DE 20$ EN PRODCUTOS DE ASEO PERSONAL!")
#fin_if
if(total>=200 and total<300):
    print("GANASTE UN VALE DE 30$ EN PRODCUTOS DE ASEO PERSONAL!")
#fin_if