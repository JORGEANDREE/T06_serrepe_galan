import os
#declarar variables
computadoras,laptops,celulares,total=0,0,0,0

#pedir las variables via argumentos
computadoras=int(os.sys.argv[1])
laptops=int(os.sys.argv[2])
celulares=int(os.sys.argv[3])
total=computadoras+laptops+celulares

#impresion
print("#################################")
print("###############TIENDA ELECTRONICA############")
print("# N-computadoras",computadoras)
print("# N-laptops:",laptops)
print("# N-celulares:",celulares)
print("# Total:",total)
print("#################################")

#validacion
ganaste=(total>100)

#condicional simple
if(ganaste==True):
    print("GANASTE UN CELULAR ULTIMO MODELO")
#fin_if
