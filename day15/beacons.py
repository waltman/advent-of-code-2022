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

    def __repr__(self):
        return f'sensor:({self.srow},{self.scol}) beacon:({self.brow},{self.bcol}) dist:{self.dist()}'

sensors = []
with open(argv[1]) as f:
    for line in f:
        m = re.search('=([\d-]*).*=([\d-]*).*=([\d-]*).*=([\d-]*)', line)
        sensors.append(Sensor(m.group(1), m.group(2), m.group(3), m.group(4)))
for sensor in sensors:
    print(sensor)

