from sys import argv

def marker_pos(buf):
    for i in range(len(buf)-4):
        if len(set(buf[i:i+4])) == 4:
            return i+4
    return -1

with open(argv[1]) as f:
    for line in f:
        print('Part 1:', marker_pos(line))
