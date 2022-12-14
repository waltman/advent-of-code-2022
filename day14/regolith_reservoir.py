from sys import argv
import numpy as np
from itertools import product

def print_grid(grid, max_row, min_col, max_col):
    for row in range(max_row+1):
        for col in range(min_col, max_col+1):
            print(grid[row,col], end='')
        print()

grid = np.array([['.' for _ in range(530)] for _ in range(170)])
min_col = 1e300
max_col = -1e300
max_row = -1e300
with open(argv[1]) as f:
    for line in f:
        points = line.rstrip().split(' -> ')
        for i in range(len(points)):
            col, row = [int(x) for x in points[i].split(',')]
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            max_row = max(max_row, row)
            points[i] = (row, col)
        for i in range(1, len(points)):
            row_range = range(min(points[i-1][0], points[i][0]), max(points[i-1][0], points[i][0])+1)
            col_range = range(min(points[i-1][1], points[i][1]), max(points[i-1][1], points[i][1])+1)
            grid[row_range,col_range] = '#'

print_grid(grid, max_row, min_col, max_col)

sand = 0
while True:
    row = 0
    col = 500
    while True:
        if row > max_row:
            break
        if grid[row+1,col] == '.':
            row += 1
        elif grid[row+1,col-1] == '.':
            row += 1
            col -= 1
        elif grid[row+1,col+1] == '.':
            row += 1
            col += 1
        else:
            grid[row,col] = 'o'
            sand += 1
            break
    if row > max_row:
        break

print_grid(grid, max_row, min_col, max_col)
print('Part 1:', sand)
