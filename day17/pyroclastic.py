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

# initialize the rocks
rocks = []
rocks.append(np.array([1,1,1,1]))
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

with open(argv[1]) as f:
    pattern = f.read().rstrip()
    jet = Jet(pattern)
