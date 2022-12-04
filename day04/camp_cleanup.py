from sys import argv

elves = []
with open(argv[1]) as f:
    for line in f:
        toks = line.rstrip().split(',')
        pair = []
        for tok in toks:
            pair.append([int(x) for x in tok.split('-')])
        elves.append(pair)

contains_count = 0
for elf in elves:
    if (elf[0][0] >= elf[1][0] and elf[0][1] <= elf[1][1]) or \
       (elf[1][0] >= elf[0][0] and elf[1][1] <= elf[0][1]):
        contains_count += 1

print('Part 1:', contains_count)
