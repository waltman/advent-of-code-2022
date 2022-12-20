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

with open(argv[1]) as f:
    pattern = f.read().rstrip()
    jet = Jet(pattern)

for i in range(80):
    print(next(jet), end='')
#    print(jet[i], end='')
