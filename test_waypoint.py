from waypoint import *
from flightplan import *

wp1 = Waypoint("Nou Camp", 41.381623923229995, 2.122853541678448)
wp2 = Waypoint("Santiago Bernabeu", 40.453030507454244 , -3.6883551609249308)
wp3 = Waypoint("Balaidos",  42.211904178262195, -8.739772189675971)
wp4 = Waypoint("Sanchez Pizjuan", 37.38276157689335 ,-5.971691936532935)

ShowWaypoint(wp1)
print(haversine_distance(wp1,wp2))