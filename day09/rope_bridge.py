from sys import argv

def tail_move(dr, dc):
    move = {
        (0,+2): (0,+1),
        (0,-2): (0,-1),
        (+2,0): (+1,0),
        (-2,0): (-1,0),

        (+1,+2): (+1,+1),
        (+2,+1): (+1,+1),

        (+1,-2): (+1,-1),
        (+2,-1): (+1,-1),

        (-1,-2): (-1,-1),
        (-2,-1): (-1,-1),

        (-2,+1): (-1,+1),
        (-1,+2): (-1,+1),
    }

    if abs(dr) < 2 and abs(dc) < 2:
        return (0,0)
    elif (dr,dc) in move:
        return move[(dr,dc)]
    else:
        print("Can't find", dr, dc)
        return (0,0)

head_move = {
    'R': (0,+1),
    'L': (0,-1),
    'U': (+1,0),
    'D': (-1,0),
    }

hpos = [0,0]
tpos = [0,0]
seen = set()
seen.add(tuple(tpos))

with open(argv[1]) as f:
    for line in f:
        direct, cnt = line.rstrip().split(' ')
        cnt = int(cnt)
        for i in range(cnt):
            hdr, hdc = head_move[direct]
            hpos[0] += hdr
            hpos[1] += hdc
            tdr, tdc = tail_move(hpos[0] - tpos[0], hpos[1] - tpos[1])
            tpos[0] += tdr
            tpos[1] += tdc
            seen.add(tuple(tpos))

print('Part 1:', len(seen))

            
