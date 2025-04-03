from waypoint import *
import matplotlib.pyplot as plt


class flightplan:
    def __init__(self, name, waypoints = []):
        self.name = name
        self.waypoints = waypoints

    
def AddWaypoint(fp, wp):
    fp.waypoints.append(wp)
    
def ShowFlightPlan(fp):
    for waypoint in fp.waypoints:
        print(f"Nombre: {waypoint.name}, Latitud: {waypoint.lat} , Longitud: {waypoint.lon}")
    

def FindWaypoint(fp, name):
    for waypoint in fp.waypoints:
        if waypoint.name == name:
            return waypoint

def RemoveWaypoint(fp,name):
    i = 0
    for waypoint in fp.waypoints:
        if waypoint.name == name:
            del fp.waypoints[i]
    i +=1

    

def FlightPlanLength (fp):
    i = 0
    suma = 0
    while i < (len(fp.waypoints) - 1):
        suma += haversine_distance(fp.waypoints[i], fp.waypoints[i + 1])
        i +=1
    return suma


import matplotlib.pyplot as plt

def PlotFlightPlan(fp):
    waypoints = fp.waypoints
    
    for i, wp in enumerate(waypoints):
        plt.plot(wp.lon, wp.lat, 'o', color='red', markersize=5)
        plt.text(float(wp.lon) + 0.2, float(wp.lat) + 0.2, wp.name,
                 color='green', weight='bold', fontsize=6)
        
        # Dibujar flecha al siguiente waypoint
        if i < len(waypoints) - 1:
            next_wp = waypoints[i + 1]
            dx = float(next_wp.lon) - float(wp.lon)
            dy = float(next_wp.lat) - float(wp.lat)
            plt.arrow(wp.lon, wp.lat, dx * 0.9, dy * 0.9,
                      head_width=0.4, head_length=0.4, fc='blue', ec='blue')

    # Coordenadas de un punto en el extremo Noroeste de la península ibérica
    latNW = 43.62481631158062
    lonNW = -8.902207838560653
    # Coordenadas de un punto en el extremo Sureste de la península ibérica
    latSE = 35.98754955400314
    lonSE = 3.8847514743561953

    plt.axis([lonNW, lonSE, latSE, latNW])
    plt.grid(color='red', linestyle='dashed', linewidth=0.5)
    plt.title('Tu plan de vuelo: ' + fp.name)
    plt.show()



def LoadFlightPlan (fileName):
    file = open(fileName, "r")
    for line in file:
        plan = flightplan("plan")
        separado = line.split()
        wp = Waypoint(separado[0], separado[1], separado[2])
        AddWaypoint(plan, wp)
    
    return plan

def SaveFlightplan (plan, fileName):
    file = open(fileName, "w")
    for waypoint in plan.waypoints:
        file.write(str(waypoint.name) + " " + str(waypoint.lat) + " " + str(waypoint.lon) + "\n")

fp = LoadFlightPlan("flightplan.txt")
print(float(fp.waypoints[3].lon) + float(fp.waypoints[2].lon))
PlotFlightPlan(fp)

