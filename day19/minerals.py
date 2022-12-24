from sys import argv
import re

# inspired by https://github.com/mebeim/aoc/tree/master/2022#day-19---not-enough-minerals

class Blueprint:
    def __init__(self, idx, ore_cost, clay_cost, obs_cost_ore, obs_cost_clay, geo_cost_ore, geo_cost_obs):
        self.idx = idx
        self.ore_cost = ore_cost
        self.clay_cost = clay_cost
        self.obs_cost_ore = obs_cost_ore
        self.obs_cost_clay = obs_cost_clay
        self.geo_cost_ore = geo_cost_ore
        self.geo_cost_obs = geo_cost_obs

    def __repr__(self):
        return f'{self.idx}: {self.ore_cost}, {self.clay_cost}, {self.obs_cost_ore} + {self.obs_cost_clay}, {self.geo_cost_ore} + {self.geo_cost_obs}'

def best_case_scenario(initial_amount, robots, t):
    return initial_amount + robots * (t + 1) + t * (t + 1) // 2

def search(bp):
    time    = 24
    best    = 0     # Best number of geodes we are able to collect.
    visited = set() # Visited states.

    # The "frontier" of our search, containing states to explore next.
    # In the initial state we only have 1 ore-mining robot.
    stack = [(time, 0, 0, 0, 0, 1, 0, 0, 0)]

    max_ore_needed  = max(bp.ore_cost, bp.clay_cost, bp.obs_cost_ore, bp.geo_cost_ore)
    max_clay_needed = bp.obs_cost_clay
    max_obs_needed  = bp.geo_cost_obs

    while stack:
        time, ore, clay, obs, geo, rore, rclay, robs, rgeo = state = stack.pop()
        if state in visited:
            continue

        visited.add(state)

        # Each robot we have mines 1 resource of its type, taking 1 minute.
        newore  = ore  + rore
        newclay = clay + rclay
        newobs  = obs  + robs
        newgeo  = geo  + rgeo
        time -= 1

        # If we run out of time, we reached a "goal" state. Update the best
        # number of geodes we were able to mine.
        if time == 0:
            best = max(best, newgeo)
            continue

        # If we can't mine more geodes in the best-case scenario, bail out.
        if best_case_scenario(newgeo, rgeo, time) < best:
            continue

        # If we can't mine enough obsidian to build new geode robots even in the
        # best-case scenario, we already know how many geodes we'll be able to get.
        if best_case_scenario(newobs, robs, time) < bp.geo_cost_obs:
            best = max(best, newgeo + rgeo * time)
            continue

        # Likewise for ore.
        if best_case_scenario(newore, rore, time) < bp.geo_cost_ore:
            best = max(best, newgeo + rgeo * time)
            continue

        # Following are the possible actions (transitions) to take...

        # Does it make sense to wait for a resource? I.E. do I have less than
        # the max needed and do I also have robots to produce it?
        if (robs and obs < max_obs_needed) or (rclay and clay < max_clay_needed) or ore < max_ore_needed:
            # If so, we can also try just spending one minute only mining without building any robot.
            stack.append((time, newore, newclay, newobs, newgeo, rore, rclay, robs, rgeo))

        # If we have enough materials for a geode-mining robot, we could also build that.
        if obs >= bp.geo_cost_obs and ore >= bp.geo_cost_ore:
            stack.append((
                time,
                newore - bp.geo_cost_ore,
                newclay,
                newobs - bp.geo_cost_obs,
                newgeo,
                rore, rclay, robs, rgeo + 1
            ))

        # If we have enough materials for an obsidian-mining robot, we could also build that.
        if obs < max_obs_needed and clay >= bp.obs_cost_clay and ore >= bp.obs_cost_ore:
            stack.append((
                time,
                newore - bp.obs_cost_ore,
                newclay - bp.obs_cost_clay,
                newobs,
                newgeo,
                rore, rclay, robs + 1, rgeo
            ))

        # If we have enough materials for a clay-mining robot, we could also build that.
        if rclay < max_clay_needed and ore >= bp.clay_cost:
            stack.append((
                time,
                newore - bp.clay_cost,
                newclay,
                newobs,
                newgeo,
                rore, rclay + 1, robs, rgeo
            ))

        # If we have enough materials for an ore-mining robot, we could also build that.
        if rore < max_ore_needed and ore >= bp.ore_cost:
            stack.append((
                time,
                newore - bp.ore_cost,
                newclay,
                newobs,
                newgeo,
                rore + 1, rclay, robs, rgeo
            ))

    return best

with open(argv[1]) as f:
    blueprints = [Blueprint(*map(int, re.findall(r'\d+', line))) for line in f]

print('Part 1:', sum(bp.idx * search(bp) for bp in blueprints))
