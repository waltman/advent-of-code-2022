from sys import argv
import numpy as np
from copy import copy
from collections import defaultdict

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

    def offset(self):
        return self.idx % len(self.pattern)

def draw_cave(cave):
    for row in range(cave.shape[0]-1, 0, -1):
        print('|', end='')
        for col in range(1,8):
            val = '#' if cave[row,col] else '.'
            print(val, end='')
        print('|')
    print('+-------+')
    print()

def dump_cave(cave):
    count = defaultdict(int)
    vals = []
    st = ''
    for row in range(1, cave.shape[0]-1):
        val = 0
        for col in range(1,8):
            val = val * 2 + cave[row,col]
        count[val] += 1
        vals.append(val)
        st += chr(val)
    tups = [(v,k) for k,v in count.items()]
    print(sorted(tups))
    print(st)
#    print(count)
#    print(vals)

def last_n_rows(cave, currow, n):
    st = ''
    for row in range(currow - n + 1, currow+1):
        val = 0
        for col in range(1,8):
            val = val * 2 + cave[row,col]
        st += chr(val)
    return st

def move_lr(cave, rock, delta, row, lcol):
    cave_copy = copy(cave)
    trow = row + rock.shape[0] - 1
    rcol = lcol + rock.shape[1]
    cave_copy[row:trow+1, lcol+delta:rcol+delta] += rock
    if np.any(cave_copy[row:trow+1, lcol+delta:rcol+delta].flatten() > 1):
        return cave, lcol # hit something so don't move
    else:
        return cave_copy, lcol + delta

def move_down(cave, rock, row, lcol):
    cave_copy = copy(cave)
    trow = row + rock.shape[0] - 1
    rcol = lcol + rock.shape[1]
    cave_copy[row-1:trow, lcol:rcol] += rock
    if np.any(cave_copy[row-1:trow, lcol:rcol].flatten() > 1):
        return cave, row # hit something so don't move
    else:
        return cave_copy, row-1

# initialize the rocks
rocks = []
rocks.append(np.array([[1,1,1,1]]))
rocks.append(np.array([[0,1,0],
                       [1,1,1],
                       [0,1,0]]))
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
HEIGHT = 10000
CACHE = 50
cave = np.zeros([HEIGHT+1, 9], dtype=int)
cave[0,:] = 1
cave[:,0] = 1
cave[:,8] = 1
TARGET_ROCK_IDX = 1000000000000

with open(argv[1]) as f:
    pattern = f.read().rstrip()
    jet = Jet(pattern)

height = 1
seen = dict()
for rock_idx in range(5000):
    rock = rocks[rock_idx % len(rocks)]
    lcol = 3
    rcol = lcol + rock.shape[1]-1
    row = height + 3
    while True:
        delta = next(jet)
        cave_copy, lcol = move_lr(cave, rock, delta, row, lcol)
        
        cave_copy, new_row = move_down(cave, rock, row, lcol)

        if new_row == row:
            trow = row + rock.shape[0] - 1
            rcol = lcol + rock.shape[1]
            cave[row:trow+1, lcol:rcol] += rock
            height = max(height, trow+1)

            # save what we've already seen
            if height > CACHE:
                k = (last_n_rows(cave, height, CACHE), jet.offset(), rock_idx % len(rocks))
                v = (height, rock_idx)
                if k in seen:
                    print(f'Key last seen at {seen[k]}. New value: {v}. Offset: ({v[0] - seen[k][0]}, {v[1] - seen[k][1]})')
                    dheight = v[0] - seen[k][0]
                    drock = v[1] - seen[k][1]
                    remaining = TARGET_ROCK_IDX - rock_idx
                    cycles = remaining // drock
                    extras = remaining % drock
                    print(cycles, extras)
                else:
                    seen[k] = v
            break
        else:
            row = new_row
