import os
#declarar variables
ladrillos,cemento,piedras,arena_de_construccion,total=0,0,0,0,0

#pedir las variables via argumentos
ladrillos=int(os.sys.argv[1])
cemento=int(os.sys.argv[2])
piedras=int(os.sys.argv[3])
arena_de_construccion=int(os.sys.argv[4])
total=ladrillos+cemento+piedras+arena_de_construccion

#impresion
print("#################################")
print("###############CONTRUCCION############")
print("# ladrillos",ladrillos)
print("# cemento:",cemento)
print("# arena de construccion:",arena_de_construccion)
print("# total:",total)
print("#################################")

#condicional multiple
if(total<100):
    print("CASA EN CONSTRUCCION")
#fin_if
if(total>=100 and total<200):
    print("CASA CASI TERMINADA")
#fin_if
if(total<=300):
    print("CASA TERMINADA")
#fin_if