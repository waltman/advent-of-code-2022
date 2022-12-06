from sys import argv

def marker_pos(buf, patlen):
    for i in range(len(buf)-patlen):
        if len(set(buf[i:i+patlen])) == patlen:
            return i+patlen
    return -1

with open(argv[1]) as f:
    for line in f:
        print('Part 1:', marker_pos(line, 4))
        print('Part 2:', marker_pos(line, 14))
