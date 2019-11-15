import os
#declarar variales
cliente,mesero,dulces,pu_dulces,total_dulces,queques,pu_queques,total_de_queques,hamburguesas,pu_hamburguesas,total_hamburguesas,consumo,igv,total_pagar="","",0,0,0,0,0,0,0,0,0,0,0,0

#pedir las variables via argumentos
cliente=os.sys.argv[1]
mesero=os.sys.argv[2]
dulces=int(os.sys.argv[3])
pu_dulces=int(os.sys.argv[4])
total_dulces=dulces*pu_dulces
queques=int(os.sys.argv[5])
pu_queques=int(os.sys.argv[6])
total_de_queques=queques*pu_queques
hamburguesas=int(os.sys.argv[7])
pu_hamburguesas=int(os.sys.argv[8])
total_hamburguesas=hamburguesas*pu_hamburguesas
consumo=total_dulces+total_de_queques+total_hamburguesas
igv=0.18*consumo
total_pagar=consumo+igv

#impresion
print("####################FACTURA################")
print("## CLIENTE:",cliente,"  Mesero:",mesero," #")
print("##############################################")
print("# producto        cantidad  P.U  total     #")
print("# dulces:",dulces,"  ",pu_dulces,"  ",total_dulces,"#")
print("# queuqes:",queques,"  ",pu_queques,"  ",total_de_queques,"#")
print("# hamburguesas:",hamburguesas,"  ",pu_hamburguesas,"  ",total_hamburguesas,"#")
print("# consumo:", consumo, "                            #")
print("# IGV:", igv ,"                                    #")
print("# total a pagar:", total_pagar, "                  #")
print("##############################################")

#validacion
comprador_compulsivo=(total_pagar>1000)
#condicional simple
if(comprador_compulsivo==True):
    print("Comprador compulsivo")
#fin_if