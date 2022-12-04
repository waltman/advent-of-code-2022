from sys import argv

def contains(elf):
    if elf[0][0] >= elf[1][0] and elf[0][1] <= elf[1][1]:
        return True
    elif elf[1][0] >= elf[0][0] and elf[1][1] <= elf[0][1]:
        return True
    else:
        return False

def overlap(elf):
    if elf[1][0] <= elf[0][0] <= elf[1][1]:
        return True
    elif elf[1][0] <= elf[0][1] <= elf[1][1]:
        return True
    elif elf[0][0] <= elf[1][0] <= elf[0][1]:
        return True
    elif elf[0][0] <= elf[1][1] <= elf[0][1]:
        return True
    else:
        return False

elves = []
with open(argv[1]) as f:
    for line in f:
        toks = line.rstrip().split(',')
        pair = []
        for tok in toks:
            pair.append([int(x) for x in tok.split('-')])
        elves.append(pair)

contains_count = 0
overlap_count = 0
for elf in elves:
    if contains(elf):
        contains_count += 1
    if overlap(elf):
        overlap_count += 1

print('Part 1:', contains_count)
print('Part 2:', overlap_count)
