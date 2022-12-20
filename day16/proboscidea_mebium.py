# This is based on the code at https://github.com/mebeim/aoc/blob/master/2022/README.md#day-16---proboscidea-volcanium
# I learned a bunch from that description, and I also had to fix a few
# bugs to get it to work on my input, so I'm going to count this as a win.

from sys import argv
import re
import networkx as nx
from collections import defaultdict
from itertools import combinations

class Valve:
    def __init__(self, name, rate, tunnels):
        self.name = name
        self.rate = rate
        self.tunnels = tunnels
        self.closed = True

    def __repr__(self):
        return f'{self.name} rate:{self.rate} tunnels:{self.tunnels} closed:{self.closed}'

def score(valves, chosen_valves):
    return sum(map(lambda x: valves[x[0]].rate * x[1], chosen_valves.items()))

def solutions(distance, valves, time=30, cur='AA', chosen={}):
    for nxt in valves:
        new_time   = time - (distance[cur][nxt] + 1)
        if new_time < 1:
            continue

        new_chosen = chosen | {nxt: new_time}
        new_valves = valves - {nxt}
        yield from solutions(distance, new_valves, new_time, nxt, new_chosen)

    yield chosen

# parse the input
valves = {}
with open(argv[1]) as f:
    for line in f:
        m = re.match('Valve (.*) has flow rate=(\d+); tunnels? leads? to valves? (.*)', line.rstrip())
        name = m.group(1)
        rate = int(m.group(2))
        tunnels = m.group(3).split(', ')
        valves[name] = Valve(name, rate, tunnels)

G = nx.Graph()
for name, valve in valves.items():
    for tunnel in valve.tunnels:
        G.add_edge(name, tunnel)

dist = dict(nx.all_pairs_shortest_path_length(G))
good = {valve.name for valve in valves.values() if valve.rate > 0}
best = max(score(valves, s) for s in solutions(dist, good))
print('Part 1:', best)

# part 2
maxscore = defaultdict(int)

for solution in solutions(dist, good, 26):
    k = frozenset(solution)
    s = score(valves, solution)

    if s > maxscore[k]:
        maxscore[k] = s

best = 0

for (s1, score1), (s2, score2) in combinations(maxscore.items(), 2):
    if len(s1 & s2) > 0:
        continue

    if (cur := score1 + score2) > best:
        best = cur

print('Part 2:', best)
