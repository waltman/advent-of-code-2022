from sys import argv
import re
from copy import copy

class Valve:
    def __init__(self, name, rate, tunnels):
        self.name = name
        self.rate = rate
        self.tunnels = tunnels
        self.closed = True

    def __repr__(self):
        return f'{self.name} rate:{self.rate} tunnels:{self.tunnels} closed:{self.closed}'

def make_graphviz(valves):
    gv = 'Graph G {\n'
    for name, valve in valves.items():
        for tunnel in valve.tunnels:
            if name < tunnel:
                gv += f'{name} -- {tunnel};\n';
    for name, valve in valves.items():
        if valve.rate > 0:
            gv += f'{name} [label="{name} {valve.rate}"];\n'
    gv += '}'
    return gv

def closed_dict2str(valves, closed):
    res = ''
    for k in sorted(valves.keys()):
        res += '1' if closed[k] else '0'
    return res

def closed_str2dict(valves, closed_str):
    closed = {}
    keys = sorted(valves.keys())
    for i in range(len(keys)):
        closed[keys[i]] = True if closed_str[i] == '1' else False
    return closed


# parse the input
valves = {}
with open(argv[1]) as f:
    for line in f:
        m = re.match('Valve (.*) has flow rate=(\d+); tunnels? leads? to valves? (.*)', line.rstrip())
        name = m.group(1)
        rate = int(m.group(2))
        tunnels = m.group(3).split(', ')
        valves[name] = Valve(name, rate, tunnels)

best_score = 0
closed = {name: True for name in valves.keys()}
stack = [(1, 'AA', 0, 0, set(), closed, [])]
while stack:
    time, name, rate, score, old_state, old_closed, old_path = stack.pop()
#    print(time, name, rate, score, state, closed)
#    print(time, name, rate, score, old_path)
    state = copy(old_state)
    state.add((name, rate))
    path = copy(old_path)
    path.append(name[0])
    closed = copy(old_closed)
    if name == 'EE' and rate == 76:
        pass
        
    if time > 30:
        if score > best_score:
            best_score = score
            print('new best score!', best_score)
#        else:
#            print('score =', score)
    else:
        stuck = True
        for tunnel in valves[name].tunnels:
            if (tunnel, rate) not in state:
#                print('pushing', (tunnel, rate))
                stack.append((time+1, tunnel, rate, score+rate, state, closed, path))
                stuck = False
        if closed[name] and valves[name].rate > 0:
            new_closed = copy(closed)
            new_closed[name] = False
#            print('open pushing', (name, rate + valves[name].rate))
            stack.append((time+1, name, rate + valves[name].rate, score+rate, state, new_closed, path))
            stuck = False
        if stuck:
            stack.append((31, name, rate, score+(rate* (31-time)), state, closed, path + [name] * (30-len(path))))
                
print('Part 1:', best_score)
