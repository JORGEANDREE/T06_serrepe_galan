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

#validacion
exceso_de_animales=(total_granja>50)

#condicional doble
if(exceso_de_animales==True):
    print("GRANJA LLENA")
#fin_if
else:
    print("numero de animales moderado")
#fin_else