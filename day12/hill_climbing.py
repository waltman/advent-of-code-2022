import sys
import numpy as np
from collections import deque

def neighbors(row, col, shape):
    if row > 0:
        yield row-1, col
    if row < shape[0]-1:
        yield row+1, col
    if col > 0:
        yield row, col-1
    if col < shape[1]-1:
        yield row, col+1

def bfs(grid, start, finish):
    seen = set()
    queue = deque()
    queue.append((start[0], start[1], 0))
    while queue:
        row, col, steps = queue.popleft()
        if (row, col) == finish:
            return steps

        seen.add((row, col))
        for neighbor in neighbors(row, col, grid.shape):
            if neighbor not in seen and ord(grid[neighbor[0],neighbor[1]]) - ord(grid[row,col]) <= 1:
                seen.add((neighbor[0], neighbor[1]))
                queue.append((neighbor[0], neighbor[1], steps+1))
    return 1e300

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

print('Part 1:', bfs(grid, start, finish))

# find all the low points
lows = []
for row in range(rows):
    for col in range(cols):
        if grid[row,col] == 'a':
            lows.append((row,col))
print('Part 2:', min(map(lambda x: bfs(grid, x, finish), lows)))
