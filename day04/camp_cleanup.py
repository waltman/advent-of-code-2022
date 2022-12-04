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

with open(argv[1]) as f:
    elves = [[[int(x) for x in tok.split('-')] for tok in line.rstrip().split(',')] for line in f]

contains_count = 0
overlap_count = 0
for elf in elves:
    if contains(elf):
        contains_count += 1
    if overlap(elf):
        overlap_count += 1

print('Part 1:', contains_count)
print('Part 2:', overlap_count)
