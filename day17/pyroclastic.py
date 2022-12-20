from sys import argv
import numpy as np

class Jet:
    def __init__(self, pattern):
        self.pattern = pattern

    def __getitem__(self, idx):
        return self.pattern[idx % len(self.pattern)]

with open(argv[1]) as f:
    pattern = f.read().rstrip()
    jet = Jet(pattern)

for i in range(80):
    print(jet[i], end='')
