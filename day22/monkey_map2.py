from sys import argv
import numpy as np
from itertools import product

def draw_grid(grid):
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            print(grid[row,col], end='')
        print()

def face(grid, row, col):
    dim = grid.shape[0] // 3

    if 0 <= row < dim:
        return 1
    elif dim <= row < dim * 2:
        return (col // dim) + 2
    else:
        return (col // dim) + 3

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

def first_col(grid, row, col):
    f = face(grid, row, col)
    print('first_col', row, col, f)
    if f == 1:
        offset = row-0
        return 11-offset, 15, 'L'
    elif f == 4:
        offset = row-4
        return 8, 15-offset, 'D'
    elif f == 6:
        offset = row-8
        return 3-offset, 11, 'L'

def last_col(grid, row, col):
    f = face(grid, row, col)
    print('last_row', row, col, f)
    if f == 1:
        offset = row-0
        return 4, 7-offset, 'D'
    elif f == 2:
        offset = row-4
        return 15-offset, 11, 'U'
    elif f == 5:
        offset = row-4
        return 7, 7-offset, 'U'

def first_row(grid, row, col):
    f = face(grid, row, col)
    print('first_row', row, col, f)
    if f == 2:
        offset = col-0
        return 11, 11-offset, 'U'
    elif f == 3:
        offset =col-4
        return 11-offset, 8, 'R'
    elif f == 5:
        offset = col-8
        return 7, 3-offset, 'U'
    elif f == 6:
        offset = col-12
        return 7-offset, 0, 'R'

def last_row(grid, row, col):
    f = face(grid, row, col)
    print('last_row', row, col, f)
    if f == 2:
        offset = col-0
        return 0, 11-offset, 'D'
    elif f == 3:
        offset = col-4
        return 7-offset, 8, 'R'
    elif f == 1:
        offset = col-8
        return 4, 3-offset, 'D'
    elif f == 6:
        offset = col-12
        return 7-offset, 12, 'R'

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
col = 8

# now walk the path
dist = 0
idx = 0
for idx in range(len(path) + 1):
    if idx < len(path) and '0' <= path[idx] <= '9':
        dist = dist * 10 + int(path[idx])
    else:
#        print(dist, facing)
        for _ in range(dist):
            drow, dcol = delta[facing]
            if drow != 0:
                new_row = row + drow
                if new_row < 0:
                    new_row, new_col, new_facing = last_row(grid, row, col)
                elif new_row >= rows:
                    new_row, new_col, new_facing = first_row(grid, row, col)
                elif grid[new_row,col] == ' ' and facing == 'U':
                    new_row, new_col, new_facing = last_row(grid, row, col)
                elif grid[new_row,col] == ' ' and facing == 'D':
                    new_row, new_col, new_facing = first_row(grid, row, col)
                else:
                    new_col, new_facing = col, facing

            else:
                new_col = col + dcol
                if new_col < 0:
                    new_row, new_col, new_facing = last_col(grid, row, col)
                elif new_col >= cols:
                    new_row, new_col, new_facing = first_col(grid, row, col)
                elif grid[row,new_col] == ' ' and facing == 'L':
                    new_row, new_col, new_facing = last_col(grid, row, col)
                elif grid[row,new_col] == ' ' and facing == 'R':
                    new_row, new_col, new_facing = first_col(grid, row, col)
                else:
                    new_row, new_facing = row, facing

            if grid[new_row, new_col] == '#':
                break
            else:
                row, col, facing = new_row, new_col, new_facing
                print(f'{row=}, {col=}, {facing=}')

#        print(row, col)

        if idx < len(path):
            if path[idx] == 'R':
                facing = right_turn[facing]
            else:
                facing = left_turn[facing]

            dist = 0

print(row, col)
print('Part 2:', (row+1) * 1000 + (col+1) * 4 + score[facing])
