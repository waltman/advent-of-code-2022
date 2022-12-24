from sys import argv
import re

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

#blueprints = []
with open(argv[1]) as f:
    blueprints = [Blueprint(*map(int, re.findall(r'\d+', line))) for line in f]

for bp in blueprints:
    print(bp)
