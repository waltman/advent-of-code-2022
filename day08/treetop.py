import sys
import numpy as np

def is_visible(grid, row, col):
    if grid[row,col] > max(grid[0:row,col]): # up
        return True
    elif grid[row,col] > max(grid[row+1:,col]): # down
        return True
    elif grid[row,col] > max(grid[row,0:col]): # left
        return True
    elif grid[row,col] > max(grid[row,col+1:]): # right
        return True
    else:
        return False

with open(sys.argv[1]) as f:
    grid = np.array([[int(c) for c in line.rstrip()] for line in f])

rows, cols = grid.shape
num_visible = cols * 2 + 2 * (rows - 2)
for row in range(1, rows-1):
    for col in range(1, cols-1):
        if is_visible(grid, row, col):
            num_visible += 1

print('Part 1:', num_visible)
