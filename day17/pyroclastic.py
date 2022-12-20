from sys import argv
import numpy as np
from copy import copy

class Jet:
    def __init__(self, pattern):
        self.pattern = pattern
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        res = 1 if self.pattern[self.idx % len(self.pattern)] == '>' else -1
        self.idx += 1
        return res

    def __getitem__(self, idx):
        return 1 if self.pattern[idx % len(self.pattern)] == '>' else -1

def draw_cave(cave):
    for row in range(cave.shape[0]-1, 0, -1):
        print('|', end='')
        for col in range(1,8):
            val = '#' if cave[row,col] else '.'
            print(val, end='')
        print('|')
    print('+-------+')
    print()

def move_lr(cave, rock, delta, row, lcol):
    cave_copy = copy(cave)
    trow = row + rock.shape[0] - 1
    rcol = lcol + rock.shape[1]
    cave_copy[row:trow+1, lcol+delta:rcol+delta] += rock
    if np.any(cave_copy[row:trow+1, lcol+delta:rcol+delta].flatten() > 1):
#        cave_copy = copy(cave)
#        cave_copy[row:brow:-1, lcol:rcol] += rock
        return cave, lcol # hit something so don't move
    else:
        return cave_copy, lcol + delta

def move_down(cave, rock, row, lcol):
    cave_copy = copy(cave)
    trow = row + rock.shape[0] - 1
    rcol = lcol + rock.shape[1]
#    cave_copy[row-1:brow-1:-1, lcol:rcol] += rock
    cave_copy[row-1:trow, lcol:rcol] += rock
#    if np.any(cave_copy[row-1:brow-1:-1, lcol:rcol].flatten() > 1):
    if np.any(cave_copy[row-1:trow, lcol:rcol].flatten() > 1):
#        cave_copy = copy(cave)
#        cave_copy[row:brow:-1, lcol:rcol] += rock
        return cave, row # hit something so don't move
    else:
        return cave_copy, row-1

# initialize the rocks
rocks = []
rocks.append(np.array([[1,1,1,1]]))
rocks.append(np.array([[0,1,0],
                       [1,1,1],
                       [0,1,0]]))
# rocks.append(np.array([[0,0,1],
#                        [0,0,1],
#                        [1,1,1]]))
rocks.append(np.array([[1,1,1],
                       [0,0,1],
                       [0,0,1]]))
rocks.append(np.array([[1],
                       [1],
                       [1],
                       [1]]))
rocks.append(np.array([[1,1],
                       [1,1]]))

# intialize the cave
HEIGHT = 3500
cave = np.zeros([HEIGHT+1, 9], dtype=int)
cave[0,:] = 1
cave[:,0] = 1
cave[:,8] = 1
#print(cave)

with open(argv[1]) as f:
    pattern = f.read().rstrip()
    jet = Jet(pattern)

#cave[0,3:3+rocks[0].shape[1]] = rocks[0]
#draw_cave(cave)

height = 1
for rock_idx in range(2022):
    rock = rocks[rock_idx % len(rocks)]
    lcol = 3
    rcol = lcol + rock.shape[1]-1
    row = height + 3
#    print('start, row =', row, 'lcol =', lcol)
    while True:
        delta = next(jet)
        cave_copy, lcol = move_lr(cave, rock, delta, row, lcol)
#        print('move_lr, row =', row, 'lcol =', lcol)
        
        cave_copy, new_row = move_down(cave, rock, row, lcol)
#        print('move_down, row =', new_row, 'lcol =', lcol)

        if new_row == row:
            trow = row + rock.shape[0] - 1
            rcol = lcol + rock.shape[1]
            cave[row:trow+1, lcol:rcol] += rock
#            draw_cave(cave)
            height = max(height, trow+1)
            break
        else:
            row = new_row
print('Part 1:', height-1)
