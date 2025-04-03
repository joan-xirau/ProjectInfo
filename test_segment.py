from Node import *
from Segment import *

n1 = Node ('aaa', 0, 0)
n2 = Node ('bbb', 3, 4)
n3 = Node("ccc", 3,5 )

s1 = Segment("s1" , n1, n2)
s2 = Segment("s2" , n2, n3)

print("Segmento 1:",s1.name, "Nodo origen:", s1.origin.name, "Nodo Destino", s1.destination.name)
print("Segmento 2:",s2.name, "Nodo origen:", s2.origin.name, "Nodo Destino", s2.destination.name)