from sys import argv
import numpy as np
from itertools import product
from collections import defaultdict

def show_grid(grid):
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            print('#' if grid[row,col] else '.', end='')
        print()

def isolated(grid, elf):
    row, col = elf
    if np.any(grid[row-1,col-1:col+2]):
        return False
    elif grid[row,col-1] or grid[row,col+1]:
        return False
    elif np.any(grid[row+1,col-1:col+2]):
        return False
    else:
        return True

def check_north(grid, elf):
    row, col = elf
    if np.any(grid[row-1,col-1:col+2]):
        return 0,0
    else:
        return row-1,col

def check_south(grid, elf):
    row, col = elf
    if np.any(grid[row+1,col-1:col+2]):
        return 0,0
    else:
        return row+1,col

def check_west(grid, elf):
    row, col = elf
    if np.any(grid[row-1:row+2,col-1]):
        return 0,0
    else:
        return row,col-1

def check_east(grid, elf):
    row, col = elf
    if np.any(grid[row-1:row+2,col+1]):
        return 0,0
    else:
        return row,col+1

def num_empty(grid):
    # find dimensions
    min_row = min_col = 1e300
    max_row = max_col = -1
    for row, col in product(range(grid.shape[0]), range(grid.shape[1])):
        if grid[row,col]:
            min_row = min(min_row, row)
            min_col = min(min_col, col)
            max_row = max(max_row, row)
            max_col = max(max_col, col)

    cnt = sum([grid[row,col] for row,col in product(range(min_row, max_row+1), range(min_col, max_col+1))])
    return (max_row-min_row+1) * (max_col-min_col+1) - cnt

def dims(grid):
    # find dimensions
    min_row = min_col = 1e300
    max_row = max_col = -1
    for row, col in product(range(grid.shape[0]), range(grid.shape[1])):
        if grid[row,col]:
            min_row = min(min_row, row)
            min_col = min(min_col, col)
            max_row = max(max_row, row)
            max_col = max(max_col, col)

    return min_row, min_col, max_row, max_col

EDGE = 100
ROUNDS = 10
rules = [check_north, check_south, check_west, check_east]
grid = np.zeros([500,500], dtype=int)
row = EDGE
elves = []
with open(argv[1]) as f:
    for line in f:
        for i in range(len(line)-1):
            if line[i] == '#':
                grid[row,i+EDGE] = 1
                elves.append((row, i+EDGE))
        row += 1

rule_idx = 0
rnd = 1
while True:
    print('Round', rnd, dims(grid))
    # find proposed new position for each elf
    new_pos = {}
    proposed = defaultdict(int)
    done = True
    for elf in elves:
        if isolated(grid, elf):
            continue
        for idx in range(rule_idx, rule_idx + 4):
            row, col = rules[idx%4](grid, elf)
            if any([row,col]):
                new_pos[elf] = (row,col)
                proposed[(row,col)] += 1
                break

    # move there if we can
    for i in range(len(elves)):
        elf = elves[i]
        if elf in new_pos:
            row, col = new_pos[elf]
            if proposed[(row,col)] == 1:
                grid[elf[0],elf[1]] = 0
                grid[row,col] = 1
                elves[i] = ((row,col))
                done = False

    # show the new grid
#    print('Round', round)
#    show_grid(grid)
    
    if not done:
        rule_idx += 1
        rnd += 1
    else:
        break

print('Part 2:', rnd)
