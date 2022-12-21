from sys import argv
import numpy as np
import networkx as nx
from itertools import product

def neighbors(x,y,z):
    yield x+1,y,z
    if x > 0:
        yield x-1,y,z
    yield x,y+1,z
    if y > 0:
        yield x,y-1,z
    yield x,y,z+1
    if z > 0:
        yield x,y,z-1
    

points = []
scan = np.zeros([25,25,25])
G = nx.Graph()
for x,y,z in product(range(1,24),range(1,24),range(1,24)):
    for x1,y1,z1 in neighbors(x,y,z):
        G.add_edge((x,y,z), (x1,y1,z1))
G.add_edge((0,0,0),(1,1,1))
        
with open(argv[1]) as f:
    for line in f:
        x,y,z = [int(i) for i in line.rstrip().split(',')]
        points.append((x,y,z))
        scan[x,y,z] = 1
        G.remove_node((x,y,z))

faces = 0
face_points = []
for point in points:
    for x,z,y in neighbors(point[0],point[1],point[2]):
        if scan[x,y,z] == 0:
            faces += 1
            face_points.append((x,y,z))

print('Part 1:', faces)
print(G)
for fp in face_points:
#    print(fp, nx.shortest_path_length(G, source=fp, target=(0,0,0)), len(G[fp]))
    print(fp, len(G[fp]))

