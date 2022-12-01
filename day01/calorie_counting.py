from sys import argv

calories = []
with open(argv[1]) as f:
    elf = 0
    for line in f:
        if line := line.rstrip():
            elf += int(line)
        else:
            calories.append(elf)
            elf = 0

calories.append(elf)
print('Part 1:', max(calories))
print('Part 2:', sum(sorted(calories)[-3:]))
