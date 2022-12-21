from sys import argv
import numpy as np

def neighbors(x,y,z):
    yield x+1,y,z
    yield x-1,y,z
    yield x,y+1,z
    yield x,y-1,z
    yield x,y,z+1
    yield x,y,z-1
    

points = []
scan = np.zeros([25,25,25])

with open(argv[1]) as f:
    for line in f:
        x,y,z = [int(i)+1 for i in line.rstrip().split(',')]
        points.append((x,y,z))
        scan[x,z,y] = 1

faces = 0
for point in points:
    for x,z,y in neighbors(point[0],point[1],point[2]):
        if scan[x,y,z] == 0:
            faces += 1

print('Part 1:', faces)
