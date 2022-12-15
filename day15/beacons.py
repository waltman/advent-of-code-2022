from sys import argv
import re
from sympy import Interval, Union

class Sensor:
    def __init__(self, srow, scol, brow, bcol):
        self.srow = int(srow)
        self.scol = int(scol)
        self.brow = int(brow)
        self.bcol = int(bcol)

    def dist(self):
        return abs(self.srow - self.brow) + abs(self.scol - self.bcol)

    def can_see(self, row):
        return abs(row - self.srow) <= self.dist()

    def range_on(self, row):
        view_len = self.dist() - abs(row - self.srow)
        return range(self.scol-view_len, self.scol+view_len+1)

    def start_end_on(self, row):
        view_len = self.dist() - abs(row - self.srow)
        return self.scol-view_len, self.scol+view_len

    def __repr__(self):
        return f'sensor:({self.srow},{self.scol}) beacon:({self.brow},{self.bcol}) dist:{self.dist()}'

def union(data):
    """ Union of a list of intervals e.g. [(1,2),(3,4)] """
    intervals = [Interval(begin, end) for (begin, end) in data]
    u = Union(*intervals)
    return u.args[:2] if isinstance(u, Interval) \
       else u.args

def union2(data):
    union = []
    for begin,end in sorted(data):
        if union and union[-1][1] >= begin - 1:
            union[-1][1] = max(union[-1][1], end)
        else:
            union.append([begin, end])
    return union
    


infile = argv[1]
target = int(argv[2])
range_max = int(argv[3]) + 1
sensors = []
with open(infile) as f:
    for line in f:
        m = re.search('=([\d-]*).*=([\d-]*).*=([\d-]*).*=([\d-]*)', line)
        sensors.append(Sensor(m.group(2), m.group(1), m.group(4), m.group(3)))

free_cols = set()
# find all the cols that all the sensors can see
for sensor in sensors:
    if sensor.can_see(target):
        free_cols |= set(sensor.range_on(target))

# remove and cols that actually contain a beacon
for sensor in sensors:
    if sensor.brow == target and sensor.bcol in free_cols:
#        print('removing', sensor, 'free_cols', free_cols)
        free_cols.remove(sensor.bcol)

#print(free_cols, len(free_cols))
print('Part 1:', len(free_cols))

# for sensor in sensors:
#     print(sensor)

for row in range(range_max):
    ranges = []
    for sensor in sensors:
        if sensor.can_see(row):
            ranges.append(sensor.start_end_on(row))

    merged = union2(ranges)
#    print(row, merged)
    if len(merged) > 1:
        print('Part 2', (merged[0][1]+1) * 4000000 + row)
        break
    # if type(merged[0]) == Interval:
    #     print('Part 2', merged[0].end * 4000000 + row)
    #     break
    # if free_cols:
    #     print(row, free_cols)
    #     print('Part 2', list(free_cols)[0] * 4000000 + row)
    #     break

#for sensor in sensors:
#    print(sensor)

# print(sensors[6])
# for row in range(-3, 18):
#     if sensors[6].can_see(row):
#         print(row, sensors[6].range_on(row))
#     else:
#         print(row, [])

