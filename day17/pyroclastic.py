from sys import argv
import numpy as np

class Jet:
    def __init__(self, pattern):
        self.pattern = pattern
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        res = self.pattern[self.idx % len(self.pattern)]
        self.idx += 1
        return res

    def __getitem__(self, idx):
        return self.pattern[idx % len(self.pattern)]

def draw_cave(cave):
    for row in range(cave.shape[0]-1, -1, -1):
        print('|', end='')
        for col in range(7):
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
cave = np.zeros([HEIGHT, 7], dtype=int)

with open(argv[1]) as f:
    pattern = f.read().rstrip()
    jet = Jet(pattern)

cave[0,2:2+rocks[0].shape[1]] = rocks[0]
print(cave)
draw_cave(cave)

