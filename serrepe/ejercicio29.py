import os
#declarar variables
persona,litros_de_agua,comida,mochila_supervivencia="",0,0,0

#pedir las variables via argumentos
persona=os.sys.argv[1]
litros_de_agua=int(os.sys.argv[2])
comida=int(os.sys.argv[3])
mochila_supervivencia=litros_de_agua+comida


#impresion
print("#################################")
print("##############Mochila#############")
print("# persona:",persona)
print("# Litros de agua:",litros_de_agua)
print("# comida:",comida)
print("# mochila de supervivencia:",mochila_supervivencia,"Kg")
print("#################################")

#condicional multiple
if(mochila_supervivencia<10):
    print("carga moderada ")
#fin_if
if(mochila_supervivencia>=10 and mochila_supervivencia<30):
    print("carga media")
#fin_if
if(mochila_supervivencia>=30 and mochila_supervivencia<50):
    print("carga excesiva ")
#fin_if