import sys
import numpy as np

def is_visible(grid, row, col):
    if grid[row,col] > max(grid[0:row,col], default=0): # up
        return True
    elif grid[row,col] > max(grid[row+1:,col], default=0): # down
        return True
    elif grid[row,col] > max(grid[row,0:col], default=0): # left
        return True
    elif grid[row,col] > max(grid[row,col+1:], default=0): # right
        return True
    else:
        return False

def visible_trees(grid, row, col, dr, dc):
    rows, cols = grid.shape
    rr = row + dr
    cc = col + dc
    cnt = 0
    while rr >= 0 and rr < rows and cc >= 0 and cc < cols:
        cnt += 1
        if grid[rr,cc] >= grid[row,col]:
            break
        else:
            rr += dr
            cc += dc
    return cnt

def scenic_score(grid, row, col):
    up    = visible_trees(grid, row, col, -1,  0)
    down  = visible_trees(grid, row, col,  1,  0)
    left  = visible_trees(grid, row, col,  0, -1)
    right = visible_trees(grid, row, col,  0,  1)
    return up * down * left * right
    
with open(sys.argv[1]) as f:
    grid = np.array([[int(c) for c in line.rstrip()] for line in f])

rows, cols = grid.shape
num_visible = 0
max_score = 0
for row in range(0, rows):
    for col in range(0, cols):
        if is_visible(grid, row, col):
            num_visible += 1
        score = scenic_score(grid, row, col)
        max_score = max(max_score, score)

print('Part 1:', num_visible)
print('Part 2:', max_score)
