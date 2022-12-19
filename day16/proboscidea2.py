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
closed = {name: True for name in valves.keys() if valves[name].rate > 0}
stack = [(1, 'AA', 'AA', 0, 0, set(), closed, [], [])]
while stack:
    time, name, ename, rate, score, old_state, old_closed, old_path, old_epath = stack.pop()
#    print(time, name, ename, rate, score, state, closed)
#    print(time, name, ename, rate, score, old_path, old_epath)
    state = copy(old_state)
    state.add((name, rate))
    state.add((ename, rate))
    path = copy(old_path)
    path.append(name[0])
    epath = copy(old_epath)
    epath.append(ename[0])
    closed = copy(old_closed)
#    if name == 'EE' and rate == 76:
#        pass
        
    if time <= 26 and sum(closed.values()) == 0:
        stack.append((27, name, ename, rate, score+(rate* (27-time)), state, closed, path + [name] * (26-len(path)), epath + [ename] * (26-len(epath))))
        continue

    if time > 26:
        if score > best_score:
            best_score = score
            print('new best score!', best_score)
#        else:
#            print('score =', score)
    else:
        stuck = True
        if name == ename: # don't open anything, same node (start)
            for i in range(len(valves[name].tunnels)):
                etunnel = valves[name].tunnels[i]
                for j in range(i+1, len(valves[name].tunnels)):
                    tunnel = valves[name].tunnels[j]
                    stack.append((time+1, tunnel, etunnel, rate, score+rate, state, closed, path, epath))
                    stuck = False
        else:            
            for tunnel in valves[name].tunnels: # don't open anything
                if (tunnel, rate) not in state:
                    for etunnel in valves[ename].tunnels:
                        if (etunnel, rate) not in state and etunnel != tunnel:
                            stack.append((time+1, tunnel, etunnel, rate, score+rate, state, closed, path, epath))
                            stuck = False
        if valves[name].rate > 0 and closed[name]: # only open my value
            new_closed = copy(closed)
            new_closed[name] = False
            for etunnel in valves[ename].tunnels:
                if etunnel != name:
                    stack.append((time+1, name, etunnel, rate + valves[name].rate, score+rate, state, new_closed, path, epath))
                    stuck = False
        if valves[ename].rate > 0 and closed[ename]: # only open elephant's value
            new_closed = copy(closed)
            new_closed[ename] = False
            for tunnel in valves[name].tunnels:
                if tunnel != ename:
                    stack.append((time+1, tunnel, ename, rate + valves[ename].rate, score+rate, state, new_closed, path, epath))
                    stuck = False
        if valves[name].rate > 0 and closed[name] and valves[ename].rate > 0 and closed[ename]: # open both valves
            new_closed = copy(closed)
            new_closed[name] = False
            new_closed[ename] = False
            stack.append((time+1, name, ename, rate + valves[name].rate + valves[ename].rate, score+rate, state, new_closed, path, epath))
            stuck = False
        if stuck:
            stack.append((27, name, ename, rate, score+(rate* (27-time)), state, closed, path + [name] * (26-len(path)), epath + [ename] * (26-len(epath))))
                
print('Part 1:', best_score)
