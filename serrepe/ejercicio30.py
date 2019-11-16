import os
#declarar variables
perros,gatos,loros,total_granja=0,0,0,0

#pedir las variables via argumentos
perros=int(os.sys.argv[1])
gatos=int(os.sys.argv[2])
loros=int(os.sys.argv[3])
total_granja=perros+gatos+loros
#impresion
print("#################################")
print("###############GRANJA############")
print("# nro-perros",perros)
print("# nro-gatos:",gatos)
print("# nro-loros:",loros)
print("# total de animales:",total_granja)
print("#################################")

#condicional multiple
if(total_granja<1):
    print("GRANJA vacia")
#fin_if
if(total_granja>=1 and total_granja<20):
    print("GRANJA casi llena")
#fin_if
if(total_granja>=20 and total_granja<50):
    print("GRANJA llena")
#fin_if