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

#condicional multiple
if(nro_tickes<10):
    print("GANASTE 1 VALES PARA UN JUEGO MAS")
#fin_if
if(nro_tickes>=10 and nro_tickes<20):
    print("GANASTE 2 VALES PARA UN JUEGO MAS")
#fin_if
if(nro_tickes>=20 and nro_tickes<30):
    print("GANASTE 3 VALES PARA UN JUEGO MAS")
#fin_if
