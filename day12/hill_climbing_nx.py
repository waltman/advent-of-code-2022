import sys
import numpy as np
import networkx as nx

def neighbors(row, col, shape):
    if row > 0:
        yield row-1, col
    if row < shape[0]-1:
        yield row+1, col
    if col > 0:
        yield row, col-1
    if col < shape[1]-1:
        yield row, col+1

# read the grid into a numpy array
with open(sys.argv[1]) as f:
    grid = np.array([[c for c in line.rstrip()] for line in f])

# find the start and finish
rows, cols = grid.shape
for row in range(rows):
    for col in range(cols):
        if grid[row,col] == 'S':
            start = row,col
            grid[row,col] = 'a'
        elif grid[row,col] == 'E':
            finish = row,col
            grid[row,col] = 'z'

# turn the grid into a directed graph
G = nx.DiGraph()
for row in range(rows):
    for col in range(cols):
        for neighbor in neighbors(row, col, grid.shape):
            if ord(grid[neighbor[0],neighbor[1]]) - ord(grid[row,col]) <= 1:
                G.add_edge((row,col), neighbor)
print('Part 1:', nx.shortest_path_length(G, start, finish))

# find all the low points
lows = []
for row in range(rows):
    for col in range(cols):
        if grid[row,col] == 'a':
            lows.append((row,col))
dists = nx.shortest_path_length(G, None, finish)
print('Part 2:', min(map(lambda x: dists.get(x, 1e300), lows)))
