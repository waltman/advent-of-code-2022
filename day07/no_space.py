from sys import argv

class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files_size = 0
        self.children = dict()

    def size(self) :
        return self.files_size + sum(map(lambda x: x.size(), self.children.values()))

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
                pwd.files_size += int(toks[0])

part1_sum = 0
queue = [root]
TOTAL_SPACE = 70000000
NEEDED_SPACE = 30000000
unused = TOTAL_SPACE - root.size()
target = NEEDED_SPACE - unused
min_target = 1e300

while queue:
    subdir = queue.pop()
    size = subdir.size()
    if size <= 100000:
        part1_sum += size
    if size >= target:
        min_target = min(min_target, size)
    for child in subdir.children.values():
        queue.append(child)

print('Part 1:', part1_sum)
print('Part 2:', min_target)
