from sys import argv
import numpy as np
from collections import defaultdict, deque

def neighbors(x,y,z):
    if x < 24:
        yield x+1,y,z
    if x > 0:
        yield x-1,y,z
    if y < 24:
        yield x,y+1,z
    if y > 0:
        yield x,y-1,z
    if z < 24:
        yield x,y,z+1
    if z > 0:
        yield x,y,z-1
    
points = []
scan = np.zeros([25,25,25], dtype=int)
        
with open(argv[1]) as f:
    for line in f:
        x,y,z = [int(i) + 1 for i in line.rstrip().split(',')]
        points.append((x,y,z))
        scan[x,y,z] = 1

faces = 0
num_faces = defaultdict(int)
for point in points:
    for x,y,z in neighbors(point[0],point[1],point[2]):
        if scan[x,y,z] == 0:
            faces += 1
            num_faces[(x,y,z)] += 1

print('Part 1:', faces)

# find all the reachable voxels
reachable = set()
# anything with a 0 coordinate is reachable
for x,y,z in num_faces:
    if not all((x,y,z)):
        reachable.add((x,y,z))

reachable.add((24,24,24))
queue = deque()
queue.append((24,24,24))
points = set(points)
while (queue):
    x,y,z = queue.popleft()
    for x1,y1,z1 in neighbors(x,y,z):
        if (x1,y1,z1) not in reachable and (x1,y1,z1) not in points:
            reachable.add((x1,y1,z1))
            queue.append((x1,y1,z1))

for k,v in num_faces.items():
    if k not in reachable:
        faces -= v
print('Part 2:', faces)

        
        
