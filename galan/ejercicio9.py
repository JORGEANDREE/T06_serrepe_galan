import os
#declarar variables
residuos_plasticos,residuos_de_vidrio,residuos_papel,reciclados=0,0,0,0

#pedir las variables via argumentos
residuos_plasticos=int(os.sys.argv[1])
residuos_de_vidrio=int(os.sys.argv[2])
residuos_papel=int(os.sys.argv[3])
reciclados=residuos_papel+residuos_de_vidrio+residuos_plasticos

#impresion
print("#################################")
print("###############RECICLADORA############")
print("# residuos platicos",residuos_plasticos)
print("# residuos de vidrio:",residuos_de_vidrio)
print("# residuos de papel:",residuos_papel)
print("# total reciclados:",reciclados)
print("#################################")

#validacion
total=(reciclados>100)

#condicional simple
if(total==True):
    print("RECICLA SALVA EL MUNDO")
#fin_if
