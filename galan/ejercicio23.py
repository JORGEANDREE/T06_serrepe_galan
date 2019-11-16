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
print("# total:",total)
print("#################################")

#condicional multiple
if(total<100):
    print("GANASTE UN USB")
#fin_if
if(total>=100 and total<150):
    print("GANASTE UN CELULAR ULTIMO MODELO")
#fin_if
if(total>=150 and total<350):
    print("GANASTE UNA LAPTOP")
#fin_if