import os
#declarar variables
persona,litros_de_agua,comida,mochila_supervivencia="",0,0,0

#pedir las variables via argumentos
persona=os.sys.argv[1]
litros_de_agua=int(os.sys.argv[2])
comida=int(os.sys.argv[3])
mochila_supervivencia=litros_de_agua+comida

#validacion
mochila_pesada=(mochila_supervivencia>40)

#impresion
print("#################################")
print("##############Mochila#############")
print("# persona:",persona)
print("# litros de agua:",litros_de_agua)
print("# comida:",comida)
print("# mochila de supervivencia:",mochila_supervivencia,"Kg")
print("#################################")

#condicional doble
if(mochila_pesada==True):
    print("mochila pesada !sobrepeso! ")
#fin_if
else:
    print("Mochila liviana")
#fin_else