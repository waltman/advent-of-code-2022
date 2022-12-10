from sys import argv

# read in the program with a one-liner
with open(argv[1]) as f:
    cmds = [line.rstrip().split(' ') for line in f]

X = 1
cycle = 1
ip = 0
skip = True
strengths = 0
crt = [' '] * 240
while True:
    if cycle % 40 == 20:
        strengths += cycle * X
    if X-1 <= (cycle-1) % 40 <= X+1:
        crt[cycle-1] = '#'
    cmd = cmds[ip]
    if (cmd[0] == 'addx'):
        if skip:
            skip = False
            ip -= 1
        else:
            X += int(cmd[1])
            skip = True
    cycle += 1
    ip += 1
    if ip >= len(cmds):
        break

print('Part 1', strengths)
print('Part 2')
for i in range(0,240,40):
    print(''.join(crt[i:i+40]))
