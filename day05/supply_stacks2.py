from sys import argv
import re

state = 'parse'
with open(argv[1]) as f:
    lines = []
    for line in f:
        if state == 'parse':
            if line[1] == '1':
                # create stacks
                num_stacks = int(line[-3])
                stacks = []
                for i in range(num_stacks):
                    stacks.append([])
                for i in range(len(lines)-1, -1, -1):
                    for j in range(num_stacks):
                        idx = 4 * j + 1
                        if lines[i][idx] != ' ':
                            stacks[j].append(lines[i][idx])
                state = 'move'
            else:
                lines.append(line)
        else:
            if m := re.match('move (\d+) from (\d+) to (\d+)', line):
                move_cnt = int(m.group(1))
                move_from = int(m.group(2)) - 1
                move_to = int(m.group(3)) - 1
                cache = ''
                for i in range(move_cnt):
                    cache += stacks[move_from].pop()
                for i in range(len(cache)-1, -1, -1):
                    stacks[move_to].append(cache[i])

print('Part 2:', end='')
for i in range(num_stacks):
    print(stacks[i][-1], end='')
print()
