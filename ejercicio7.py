import os
#declarar variables
alumno,trabajos_de_programacion,trabajos_de_analisis,trabajos_de_matematica,tareas_excesivas,total_tareas="",0,0,0,0,0

#pedir las variables via argumentos
alumno=os.sys.argv[1]
trabajos_de_programacion=int(os.sys.argv[2])
trabajos_de_analisis=int(os.sys.argv[3])
trabajos_de_matematica=int(os.sys.argv[4])
total_tareas=trabajos_de_matematica+trabajos_de_analisis+trabajos_de_programacion

#validacion
tareas_excesivas=(total_tareas>10)

#impresion
print("#################################")
print("##############TAREAS#############")
print("# alumno:",alumno)
print("# Trabajos de programacion:",trabajos_de_programacion)
print("# Trabajos de analisis:",trabajos_de_analisis)
print("# Trabajos de matematica:",trabajos_de_matematica)
print("# Total de Tareas:",total_tareas)
print("#################################")

#condicional simple
if(tareas_excesivas==True):
    print("!SUFRE ! ")
#fin_if