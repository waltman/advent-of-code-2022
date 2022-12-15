from sys import argv
import re

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

    def __repr__(self):
        return f'sensor:({self.srow},{self.scol}) beacon:({self.brow},{self.bcol}) dist:{self.dist()}'

infile = argv[1]
target = int(argv[2])
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



#for sensor in sensors:
#    print(sensor)

# print(sensors[6])
# for row in range(-3, 18):
#     if sensors[6].can_see(row):
#         print(row, sensors[6].range_on(row))
#     else:
#         print(row, [])

