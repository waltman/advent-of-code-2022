from sys import argv
from collections import deque

class Blizzard:
    def __init__(self, row, col):
        self.row = row-1
        self.col = col-1

    def __repr__(self):
        return f'row: {self.row}, col: {self.col}'

class LeftBlizzard(Blizzard):
    def pos_at(self, t, num_rows, num_cols):
        return 1 + self.row, 1 + (self.col - t) % num_cols

class RightBlizzard(Blizzard):
    def pos_at(self, t, num_rows, num_cols):
        return 1 + self.row, 1 + (self.col + t) % num_cols

class UpBlizzard(Blizzard):
    def pos_at(self, t, num_rows, num_cols):
        return 1 + (self.row - t) % num_rows, 1 + self.col

class DownBlizzard(Blizzard):
    def pos_at(self, t, num_rows, num_cols):
        return 1 + (self.row + t) % num_rows, 1 + self.col

def neighbors(row, col, num_rows, num_cols):
    if row == 0 and col == 1:
        yield 1,1
        return

    if row == num_rows+1 and col == num_cols:
        yield row-1, col
        return

    if row == num_rows and col == num_cols:
        yield row+1, col

    if row > 1:
        yield row-1, col
    if row < num_rows:
        yield row+1, col
    if col > 1:
        yield row, col-1
    if col < num_cols:
        yield row, col+1
    if row == 1 and col == 1:
        yield 0, 1

def gcd(a, b):
    if b > a:
        a,b = b,a

    return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
    return abs(a * b) // gcd(a,b)

entrance = (0,1)
blizzards = []
with open(argv[1]) as f:
    row = 0
    for line in f:
        if row > 0:
            if line[0:2] == '##': # last row
                num_rows = row + 1
                num_cols = len(line) - 2
                goal = (row, num_cols-1)
                break
            else:
                for col in range(1, len(line)-2):
                    match line[col]:
                        case '<':
                            blizzards.append(LeftBlizzard(row, col))
                        case '>':
                            blizzards.append(RightBlizzard(row, col))
                        case '^':
                            blizzards.append(UpBlizzard(row, col))
                        case 'v':
                            blizzards.append(DownBlizzard(row, col))
        row += 1

#print(num_rows, num_cols, goal)
#print(blizzards)

num_rows -= 2
num_cols -= 1
egress = num_rows+1, num_cols
queue = deque([(0, 0, 1, 0)])
time_mod = lcm(num_rows, num_cols)
seen = [set(), set(), set()]
part1_done = False
leg1_done = False
while queue:
    minute, row, col, leg = queue.popleft()
#    print('popped', minute, row, col, leg, len(queue))

    # have we already been in this state?
    seen_minute = minute % time_mod
    if ((seen_minute, row, col)) in seen[leg]:
        continue
    else:
        seen[leg].add((seen_minute, row, col))

    # did we find the exit?
    if row == egress[0] and col == egress[1]:
        if leg == 0 and not part1_done:
            print('Part 1:', minute)
            leg = 1
            part1_done = True
        elif leg == 2:
            print('Part 2:', minute)
            break

    # did we get back to the start?
    if row == 0 and col == 1 and leg == 1:
        if not leg1_done:
            print('Starting leg 2 at minute', minute)
            leg1_done = True
        leg = 2

    minute += 1
    blizzard_locs = {blizzard.pos_at(minute, num_rows, num_cols) for blizzard in blizzards}
    if (row, col) not in blizzard_locs:
        queue.append((minute, row, col, leg))

    for new_row, new_col in neighbors(row, col, num_rows, num_cols):
        if (new_row, new_col) not in blizzard_locs:
            queue.append((minute, new_row, new_col, leg))
