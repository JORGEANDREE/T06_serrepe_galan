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
print("# residuos de papel:",edad_hijo)
print("# total reciclados:",reciclados)
print("#################################")

#condicional multiple
if(reciclados<60):
    print("RECICLA TU PUEDES HACER UN MUNDO MEJOR")
#fin_if
if(reciclados>=60 and reciclados<100):
    print("RECICLA SALA EL MUNDO")
#fin_if
if(reciclados>=100 and reciclados<200):
    print("NO A MAS CONTAMINACION")
#fin_if