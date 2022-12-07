from sys import argv

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = []
        self.children = dict()

    def size(self) :
        return sum([f.size for f in self.files]) + sum([child.size() for child in self.children.values()])

root = Dir('/', None)
pwd = root

with open(argv[1]) as f:
    for line in f:
        toks = line.rstrip().split(' ')
        if toks[0] == '$':
            if toks[1] == 'cd':
                if toks[2] == '/':
                    pwd = root
                elif toks[2] == '..':
                    pwd = pwd.parent
                else:
                    pwd = pwd.children[toks[2]]
            elif toks[1] == 'ls':
                pass
        else: # directory listing
            if toks[0] == 'dir':
                pwd.children[toks[1]] = Dir(toks[1], pwd)
            else:
                pwd.files.append(File(toks[1], int(toks[0])))

part1_sum = 0
queue = [root]
TOTAL_SPACE = 70000000
NEEDED_SPACE = 30000000
unused = TOTAL_SPACE - root.size()
target = NEEDED_SPACE - unused
targets = []

while queue:
    subdir = queue.pop()
    size = subdir.size()
    if size <= 100000:
        part1_sum += size
    if size >= target:
        targets.append(size)
    for child in subdir.children.values():
        queue.append(child)

print('Part 1:', part1_sum)
print('Part 2:', min(targets))
