from Node import *
n1 = Node ('aaa', 0, 0)
n2 = Node ('bbb', 3, 4)
print (Distance(n1,n2))
print (AddNeighbor(n1, n2))
print (AddNeighbor(n1, n2))
AddNeighbor(n2,n1)
print (n1.__dict__)
for n in n1.neighbors:
 print ( n.__dict__)