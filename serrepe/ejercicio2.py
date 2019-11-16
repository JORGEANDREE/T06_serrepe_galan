import os
#declarar variables
dinero,pu_ticket,nro_tickes=0.0,0.0,0.0

#pedir las variables via argumentos
dinero=float(os.sys.argv[1])
pu_ticket=float(os.sys.argv[2])
nro_tickes=dinero//pu_ticket
#impresion
print("#################################")
print("###############JUEGOS############")
print("# Dinero",dinero)
print("# precio unitario del ticket:",pu_ticket)
print("# NRO ticket:",nro_tickes)
print("#################################")

#validacion
vale=(nro_tickes>100.0)

#condicional simple
if(vale==True):
    print("GANASTE UN VALE PARA UN JUEGO MAS")
#fin_if
