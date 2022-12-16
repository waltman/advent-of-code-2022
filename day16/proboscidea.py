from sys import argv
import re

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

# for name in valves.keys():
#     print(valves[name])

#print(make_graphviz(valves))

best_score = 0
closed = {name: True for name in valves.keys()}
stack = [(1, 'AA', 0, 0, set(), closed)]
while stack:
    time, name, rate, score, state, closed = stack.pop()
#    print(time, name, rate, score, state, closed)
    print(time, name, rate, score)
    state.add((name, rate))
        
    if time > 30:
        if score > best_score:
            best_score = score
            print('new best score!', best_score)
    else:
        stuck = True
        for tunnel in valves[name].tunnels:
            if (tunnel, rate) not in state:
                stack.append((time+1, tunnel, rate, score+rate, state, closed))
                stuck = False
        if closed[name] and valves[name].rate > 0:
            closed[name] = False
            stack.append((time+1, name, rate + valves[name].rate, score+rate, state, closed))
            stuck = False
        if stuck:
            stack.append((time+1, name, rate, score+rate, state, closed))
                
print('Part 1:', best_score)
    

# best_score = 0
# stack = [('AA', 0, set(), 0, 0)]
# while (stack):
#     name, time, visited, rate, score = stack.pop()
#     print(name, time, visited, rate, score, len(stack))
#     if time > 30:
#         if score > best_score:
#             best_score = score
#             print('new best score!')
#     elif len(visited) == len(valves):
#         score += rate * (31 - time)
#         if score > best_score:
#             best_score = score
#             print('new best score!')
#     else:
#         score += rate
#         valve = valves[name]
#         if valve.closed and valve.rate > 0:
#             time += 1
#             if time <= 30:
#                 rate += valve.rate
#                 for tunnel in valve.tunnels:
#                     if tunnel not in visited:
#                         tmp = set()
#                         tmp.add(tunnel)
#                         stack.append((tunnel, time+1, visited | tmp, rate, score))
#         else:
#             for tunnel in valve.tunnels:
#                 if tunnel not in visited:
#                     tmp = set()
#                     tmp.add(tunnel)
#                     stack.append((tunnel, time+1, visited | tmp, rate, score))

# print('Part 1:', best_score)
