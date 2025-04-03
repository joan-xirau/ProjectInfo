import math
import matplotlib.pyplot as plt
from Node import *
from Segment import *

class Graph:
    def __init__(self):
        self.nodes = []
        self.segments = []

def AddNode(g, n):
    for node in g.nodes:
        if node.name == n.name:
            return False
    g.nodes.append(n)
    return True

def AddSegment(g,name, nameOriginNode, nameDestinationNode):
    origin = None
    destination = None
    for node in g.nodes:
        if node.name == nameOriginNode:
            origin = node
        if node.name == nameDestinationNode:
            destination = node
    if origin is None or destination is None:
        return False
    segment_name = name
    new_segment = Segment(segment_name, origin, destination)
    g.segments.append(new_segment)
    AddNeighbor(origin, destination)
    return True

def GetClosest(g, x, y):
    closest = None
    min_dist = float('inf')
    for node in g.nodes:
        dx = node.x - x
        dy = node.y - y
        dist = math.sqrt(dx**2 + dy**2)
        if dist < min_dist:
            min_dist = dist
            closest = node
    return closest

def Plot(g):
    plt.figure()
    for seg in g.segments:
        ox, oy = seg.origin.x, seg.origin.y
        dx, dy = seg.destination.x, seg.destination.y
        plt.plot([ox, dx], [oy, dy], 'k-')
        mid_x, mid_y = (ox + dx)/2, (oy + dy)/2
        plt.text(mid_x, mid_y, f"{seg.cost:.1f}", ha='center', va='center', backgroundcolor='white')
    for node in g.nodes:
        plt.plot(node.x, node.y, 'bo')
        plt.text(node.x, node.y, node.name, ha='right', va='bottom')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Graph Plot')
    plt.grid(True)
    plt.show()

def PlotNode(g, nameOrigin):
    origin = None
    for node in g.nodes:
        if node.name == nameOrigin:
            origin = node
            break
    if not origin:
        return False
    node_colors = []
    neighbor_names = [n.name for n in origin.neighbors]
    for node in g.nodes:
        if node.name == nameOrigin:
            node_colors.append('blue')
        elif node.name in neighbor_names:
            node_colors.append('green')
        else:
            node_colors.append('gray')
    plt.figure()
    for node, color in zip(g.nodes, node_colors):
        plt.plot(node.x, node.y, 'o', color=color, markersize=8)
        plt.text(node.x, node.y, node.name, ha='right', va='bottom')
    for seg in g.segments:
        if seg.origin.name == nameOrigin and seg.destination.name in neighbor_names:
            ox, oy = seg.origin.x, seg.origin.y
            dx, dy = seg.destination.x, seg.destination.y
            plt.plot([ox, dx], [oy, dy], 'r-')
            mid_x, mid_y = (ox + dx)/2, (oy + dy)/2
            plt.text(mid_x, mid_y, f"{seg.cost:.1f}", ha='center', va='center', color='red')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'Graph Plot for Node {nameOrigin}')
    plt.grid(True)
    plt.show()
    return True


def ReadGraphFromFile(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            file.close()
    except IOError:
        return None

    g = Graph()
    estado = None
    for line in lines:
        splited = line.split(" ")
        if splited != ['\n']:
            if "NODES" in line :
                estado = "NODES"
                continue
            elif "SEGMENTS" in line:
                estado = "SEGMENTS"
                continue
            if estado == "NODES":
                AddNode(g, Node(splited[0],float(splited[1]),float(splited[2])))
            elif estado == "SEGMENTS":
                AddSegment(g, splited[0], splited[1], splited[2])


    return g