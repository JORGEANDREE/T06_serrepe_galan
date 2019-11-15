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
print("# dinero",dinero)
print("# precio unitario del ticket:",pu_ticket)
print("# NRO ticket:",nro_tickes)
print("#################################")

#validacion
vale=(nro_tickes>100.0)

#condicional doble
if(vale==True):
    print("GANASTE 1 VALE PARA UN JUEGO MAS")
#fin_if
else:
    print("SIGUE INTENTANDO")
#fin_else