from flightplan import *
option = -1
while option != 0:
     print ('Estas son las opciones del menu:')
     print ('\t1: \tCargar plan de vuelo desde fichero')
     print ('\t2: \tPlot del plan de vuelo')
     print ('\t3: \tEliminar waypoint')
     print ('\t0: \tSalir')
     option = eval (input ('Elije una opción: '))
     if option == 1:
         fileName = input ('Escribe el nombre del fichero: ')
         fp = LoadFlightPlan(fileName)
     if option == 2:
         PlotFlightPlan(fp)
     if option == 3:
         name = input('Escribe el nombre del waypoint: ')
         RemoveWaypoint(fp, name)
print ('Gracias por usar nuestro programa')