import math
import itertools
import re

input = open("input").read()

_input = """
"""

lines = input.strip().split("\n")
data = [[int(i) for i in re.findall("\d+", line)] for line in lines]
blueprints = []
for d in data:
    bp = (
        ((d[1], 0, 0), (1, 0, 0, 0)),
        ((d[2], 0, 0), (0, 1, 0, 0)),
        ((d[3], d[4], 0), (0, 0, 1, 0)),
        ((d[5], 0, d[6]), (0, 0, 0, 1))
    )
    blueprints.append(bp)
print(blueprints)

# ore clay obsidian geode

def buy_robots(state, details):
    newStates = []
    for i, detail in enumerate(details):
        new_resources = [r - c for c, r in zip(detail[0], state["resources"])]
        if all([r > 0 for r in new_resources]):
            newStates.append({
                "resources":new_resources,
                "robots":[r + 1 if i == j else r for j, r in enumerate(state[robots])]
            })

quality_levels = []
for bp in blueprints:
    states = [{
        "resources":(0, 0, 0, 0),
        "robots":(1, 0, 0, 0)
    }]
    for i in range(0, 24):
        for state in states:
            state["resources"] = [res + rob for res, rob in zip(state["resources"], state["robots"])]
    best = 0
    for s in states:
        best = max(best, s["resources"][3])
    quality_levels.append(best)



result = sum(quality_levels)
print(result)
