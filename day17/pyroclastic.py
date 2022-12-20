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
    for row in range(cave.shape[0]-1, -1, -1):
        print('|', end='')
        for col in range(1,8):
            val = '@' if cave[row,col] else '.'
            print(val, end='')
        print('|')
    print('+-------+')

# initialize the rocks
rocks = []
rocks.append(np.array([[1,1,1,1]]))
rocks.append(np.array([[0,1,0],
                       [1,1,1],
                       [0,1,0]]))
rocks.append(np.array([[0,0,1],
                       [0,0,1],
                       [1,1,1]]))
rocks.append(np.array([[1],
                       [1],
                       [1],
                       [1]]))
rocks.append(np.array([[1,1],
                       [1,1]]))

# intialize the cave
HEIGHT = 10
cave = np.zeros([HEIGHT, 9], dtype=int)
cave[:,0] = 1
cave[:,8] = 1
print(cave)

with open(argv[1]) as f:
    pattern = f.read().rstrip()
    jet = Jet(pattern)

#cave[0,3:3+rocks[0].shape[1]] = rocks[0]
#draw_cave(cave)

height = 3
for rock_idx in range(1):
    rock = rocks[rock_idx % len(rocks)]
    lcol = 2
    rcol = lcol + rock.shape[1]-1
    row = height
    while True:
        next_cave = copy(cave)
        delta = next(jet)
#        row_range = range(row,row-rock.shape[0],-1)
#        col_range = range(lcol+delta, lcol+delta+rock.shape[1])
        next_cave[row:row-rock.shape[0]:-1,lcol+delta:lcol+delta+rock.shape[1]] += rock
#        next_cave[row_range, col_range] += rock
        if np.any(next_cave[row:row-rock.shape[0]:-1,lcol+delta:lcol+delta+rock.shape[1]].flatten() > 1):
            pass
        else:
            lcol += delta
        draw_cave(next_cave)

        next_cave = copy(cave)
        next_cave[row-1:row-1-rock.shape[0]:-1,lcol:lcol+rock.shape[1]] += rock
        if np.any(next_cave[row-1:row-1-rock.shape[0]:-1,lcol:lcol+rock.shape[1]].flatten() > 1):
            break
        else:
            row -= 1
        draw_cave(next_cave)
#        break

