import math
class Waypoint:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat =lat
        self.lon = lon

    

def ShowWaypoint(waypoint):
        print('Nombre:{0}, lat:{1}, lon:{2}'
        .format (
        waypoint.name,
        waypoint.lat,
        waypoint.lon
        ))
    


def haversine_distance(waypoint1, waypoint2):
    R = 6371
    lat1 = float(waypoint1.lat)
    lat2 = float(waypoint2.lat)

    lon1 = float(waypoint1.lon)
    lon2 = float(waypoint2.lon)

    # Convertir grados a radianes
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    
    # Diferencias en coordenadas
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    # Aplicar la fórmula de Haversine
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    distancia = R * c
    
    return distancia

