import math
import itertools
import re

input = open("input_18").read()

_input = """
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
"""

cubes = [[int(v) for v in re.findall("\d+", line) ] for line in input.strip().split("\n")]
cubes = set([(x, y, z) for x, y, z in cubes])

total = 0
for x, y, z in cubes:
    neighbors = [
        (x - 1, y, z),
        (x + 1, y, z),

        (x, y - 1, z),
        (x, y + 1, z),

        (x, y, z - 1),
        (x, y, z + 1),
    ]
    count = 6
    for n in neighbors:
        if n in cubes:
            count-=1
    total += count
print(total)

airmap = set()

xMin = min([c[0] for c in cubes]) - 1
xMax = max([c[0] for c in cubes]) + 1
yMin = min([c[1] for c in cubes]) - 1
yMax = max([c[1] for c in cubes]) + 1
zMin = min([c[2] for c in cubes]) - 1
zMax = max([c[2] for c in cubes]) + 1

stack = [(xMin, yMin, zMin)]

def inCube(n):
    x, y, z = n
    return (x >= xMin and x <= xMax) and (y >= yMin and y <= yMax) and (z >= zMin and z <= zMax)

while stack:
    pos = stack.pop()
    airmap.add(pos)
    x, y, z = pos
    neighbors = [
        (x - 1, y, z),
        (x + 1, y, z),

        (x, y - 1, z),
        (x, y + 1, z),

        (x, y, z - 1),
        (x, y, z + 1),
    ]
    for n in neighbors:
        if not(n in stack) and not(n in airmap) and not(n in cubes) and inCube(n):
            stack.append(n)


total = 0
for x, y, z in cubes:
    neighbors = [
        (x - 1, y, z),
        (x + 1, y, z),

        (x, y - 1, z),
        (x, y + 1, z),

        (x, y, z - 1),
        (x, y, z + 1),
    ]
    for n in neighbors:
        if n in airmap:
            total+=1
print(total)
