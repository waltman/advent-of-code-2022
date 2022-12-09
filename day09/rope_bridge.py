from sys import argv

def tail_move(dr, dc):
    move = {
        (0,+2): (0,+1),
        (0,-2): (0,-1),
        (+2,0): (+1,0),
        (-2,0): (-1,0),

        (+1,+2): (+1,+1),
        (+2,+1): (+1,+1),
        (+2,+2): (+1,+1),

        (+1,-2): (+1,-1),
        (+2,-1): (+1,-1),
        (+2,-2): (+1,-1),

        (-1,-2): (-1,-1),
        (-2,-1): (-1,-1),
        (-2,-2): (-1,-1),

        (-2,+1): (-1,+1),
        (-1,+2): (-1,+1),
        (-2,+2): (-1,+1),
    }

    if abs(dr) < 2 and abs(dc) < 2:
        return (0,0)
    elif (dr,dc) in move:
        return move[(dr,dc)]
    else:
        print("Can't find", dr, dc)
        return (0,0)

def run_sim(lines, num_knots):
    head_move = {
        'R': (0,+1),
        'L': (0,-1),
        'U': (+1,0),
        'D': (-1,0),
        }

    knots = [[0,0] for _ in range(num_knots)]
    hpos = [0,0]
    tpos = [0,0]
    seen = set()
    for line in lines:
        direct, cnt = line.split(' ')
        cnt = int(cnt)
        for i in range(cnt):
            dr, dc = head_move[direct]
            knots[0][0] += dr
            knots[0][1] += dc
            for j in range(1, num_knots):
                dr, dc = tail_move(knots[j-1][0] - knots[j][0], knots[j-1][1] - knots[j][1])
                knots[j][0] += dr
                knots[j][1] += dc
            seen.add(tuple(knots[-1]))

    return len(seen)

with open(argv[1]) as f:
    lines = [line.rstrip() for line in f]
    
print('Part 1:', run_sim(lines, 2))
print('Part 2:', run_sim(lines, 10))

            
