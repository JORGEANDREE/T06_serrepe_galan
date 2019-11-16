import os
#declarar variables
piloto,km_de_pista,nro_vueltas,km_recorridos="",0.0,0,0.0

#pedir las variables via argumentos
piloto=os.sys.argv[1]
km_de_pista=float(os.sys.argv[2])
nro_vueltas=int(os.sys.argv[3])
km_recorridos=km_de_pista*nro_vueltas

#impresion
print("#################################")
print("#############CARRERAS############")
print("# Piloto:",piloto)
print("# km de pista:",km_de_pista)
print("# nmro de vueltas:",nro_vueltas)
print("# km recorridos:",km_recorridos)
print("#################################")

#validcion
meta=(km_recorridos>100)

#condicional simple
if(meta==True):
    print("¡WINNER!")
#fin_if