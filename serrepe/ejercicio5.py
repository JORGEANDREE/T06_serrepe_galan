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
print("# Jabones",jabones,"  p.u:",pu_jabones)
print("# shampo:",shampo,"   p.u:",pu_shampo)
print("# acondicinador:",acondicionador, "  pu:",pu_acondicionador)
print("# Total:",total,"$")
print("#################################")

#validacion
bonus=(total>100.0)

#condicional simple
if(bonus==True):
    print("GANASTE UN SHAMPO!")
#fin_if