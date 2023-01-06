import re

input = open("input_14").read()

lines = input.strip().split("\n")

paths = [[int(v) for v in re.findall("\d+", line)] for line in lines]
sandStart = (500, 0)

rockMap = set()
for path in paths:
    for i in range(0, len(path) - 2, 2):
        x1, y1, x2, y2 = path[i:i+4]
        for y in range(min(y1, y2), max(y1, y2) + 1):
            for x in range(min(x1, x2), max(x1, x2) + 1):
                rockMap.add((x, y))
bottom = max([y for (x, y) in rockMap])
canRest = True
units = 0
while canRest:
    units += 1
    isRested = False
    pos = sandStart
    while not(isRested) and canRest:
        d = (pos[0], pos[1] + 1)
        dl = (pos[0] - 1, pos[1] + 1)
        dr = (pos[0] + 1, pos[1] + 1)
        if not(d in rockMap):
            pos = d
            if pos[1] >= bottom:
                canRest = False;
        elif not(dl in rockMap):
            pos = dl
        elif not(dr in rockMap):
            pos = dr
        else:
            rockMap.add(pos)
            isRested = True
print(units - 1)

# 902 too high



rockMap = set()
for path in paths:
    for i in range(0, len(path) - 2, 2):
        x1, y1, x2, y2 = path[i:i+4]
        for y in range(min(y1, y2), max(y1, y2) + 1):
            for x in range(min(x1, x2), max(x1, x2) + 1):
                rockMap.add((x, y))
bottom = max([y for (x, y) in rockMap])
canRest = True
units = 0
while canRest:
    units += 1
    isRested = False
    pos = sandStart
    if pos in rockMap:
        break
    while not(isRested) and canRest:
        d = (pos[0], pos[1] + 1)
        dl = (pos[0] - 1, pos[1] + 1)
        dr = (pos[0] + 1, pos[1] + 1)
        if not(d[1] == bottom + 2):
            if not(d in rockMap):
                pos = d
            elif not(dl in rockMap):
                pos = dl
            elif not(dr in rockMap):
                pos = dr
            else:
                rockMap.add(pos)
                isRested = True
        else:
            # this MUST be wrong. result is correct though
            rockMap.add(pos)
            isRested = True

print(units - 1)

# part1 23:58
# total 29:32
