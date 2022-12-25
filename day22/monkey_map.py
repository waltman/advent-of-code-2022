from sys import argv
import numpy as np
from itertools import product

def draw_grid(grid):
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            print(grid[row,col], end='')
        print()

delta = {
    'R': (0,1),
    'L': (0,-1),
    'U': (-1,0),
    'D': (1,0),
}

right_turn = {
    'R': 'D',
    'D': 'L',
    'L': 'U',
    'U': 'R',
}

left_turn = {
    'R': 'U',
    'D': 'R',
    'L': 'D',
    'U': 'L',
}

score = {
    'R': 0,
    'D': 1,
    'L': 2,
    'U': 3,
}

def first_col(grid, row):
    for col in range(grid.shape[1]):
        if grid[row,col] != ' ':
            return col

def last_col(grid, row):
    for col in range(grid.shape[1]-1, -1, -1):
        if grid[row,col] != ' ':
            return col

def first_row(grid, col):
    for row in range(grid.shape[0]):
        if grid[row,col] != ' ':
            return row

def last_row(grid, col):
    for row in range(grid.shape[0]-1, -1, -1):
        if grid[row,col] != ' ':
            return row

# parse input into an np.array
with open(argv[1]) as f:
    longest = 0
    lines = []
    state = 'map'
    for line in f:
        line = line.rstrip()
        if state == 'map':
            if line == '':
                state = 'path'
            else:
                lines.append(line.rstrip())
                longest = max(longest, len(lines[-1]))
        else:
            path = line

    grid = np.zeros([len(lines), longest], dtype=str)
    rows = grid.shape[0]
    cols = grid.shape[1]
    for row, col in product(range(rows), range(cols)):
        grid[row,col] = lines[row][col] if col < len(lines[row]) else ' '

facing =  'R'
row = 0
col = first_col(grid, row)

# now walk the path
dist = 0
idx = 0
for idx in range(len(path) + 1):
    if idx < len(path) and '0' <= path[idx] <= '9':
        dist = dist * 10 + int(path[idx])
    else:
#        print(dist, facing)
        drow, dcol = delta[facing]
        for _ in range(dist):
            new_row = row + drow
            if new_row < 0:
                new_row = last_row(grid, col)
            elif new_row >= rows:
                new_row = first_row(grid, col)
            elif grid[new_row,col] == ' ' and facing == 'U':
                new_row = last_row(grid, col)
            elif grid[new_row,col] == ' ' and facing == 'D':
                new_row = first_row(grid, col)

            new_col = col + dcol
            if new_col < 0:
                new_col = last_col(grid, row)
            elif new_col >= cols:
                new_col = first_col(grid, row)
            elif grid[row,new_col] == ' ' and facing == 'L':
                new_col = last_col(grid, row)
            elif grid[row,new_col] == ' ' and facing == 'R':
                new_col = first_col(grid, row)

            if grid[new_row, new_col] == '#':
                break
            else:
                row, col = new_row, new_col

#        print(row, col)

        if idx < len(path):
            if path[idx] == 'R':
                facing = right_turn[facing]
            else:
                facing = left_turn[facing]

            dist = 0

print(row, col)
print('Part 1:', (row+1) * 1000 + (col+1) * 4 + score[facing])
