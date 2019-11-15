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
print("# piloto:",piloto)
print("# km de pista:",km_de_pista)
print("# nmro de vueltas:",nro_vueltas)
print("# km recorridos:",km_recorridos)
print("#################################")

#validcion
meta=(km_recorridos>100)

#condicional multiple
if(meta==True):
    print("¡WINNER!")
#fin_if
else:
    print("SIGUE INTENTADOLO")
#fin_else
if(km_recorridos<20):
    print("Falta mucho ¡esfuezate mas!")
#fin_if
if(km_recorridos>=20 and km_recorridos<50):
    print("Falta poco ¡esfuezate un poco mas!")
#fin_if
if(km_recorridos>=50 and km_recorridos<70):
    print("Falta muy poco ¡vamos tu puedes!")
#fin_if