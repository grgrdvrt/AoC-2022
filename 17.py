import math
import itertools
import re

input = open("input_17").read()
print(len(input.strip()))

input = """
>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
"""

rocks = [
    [0, 1, 2, 3],
    [1 + 2j,
     1j, 1 + 1j, 2 + 1j,
     1],
    [2 + 2j,
     2 + 1j,
     0, 1, 2],
    [3j, 2j, 1j, 0],
    [1j, 1 + 1j,
     0, 1]
]


dirs = ["< >".index(char)-1 for char in input.strip()]

width = 7
highest = 0
dirIndex = 0
rockMap = set()

def showMap(rock):
    lines = []
    for j in range(1, highest + 7):
        line = []
        for i in range(width):
            pos = i + j * 1j 
            s = "."
            if pos in rockMap:
                s = "#"
            elif pos in rock:
                s = "@"
            line.append(s)
        lines.append("".join(line))
    lines.reverse()
    print("")
    print("\n".join(lines))

for i in range(2022):
    # print(i)
    start = 2 + (highest + 4) * 1j
    rock = [p + start for p in rocks[i % len(rocks)]]
    canFall = True
    step = 0
    while canFall:
        step += 1
        dir = dirs[dirIndex % len(dirs)]
        dirIndex+=1
        reals = [p.real for p in rock]
        canMoveLeft = (dir < 0 and min(reals) > 0)
        canMoveRight = (dir > 0 and max(reals) < width - 1)
        if (canMoveLeft or canMoveRight) and not(any([p + dir in rockMap for p in rock])):
            rock = [p + dir for p in rock]
        canFall = min([p.imag for p in rock]) > 1 and not(any(p - 1j in rockMap for p in rock))
        if canFall:
          rock = [p - 1j for p in rock]
    for p in rock:
        rockMap.add(p)
    highest = int(max(max([p.imag for p in rock]), highest))

# showMap([]);

# too high 3061

print(highest)

# tower shows the same pattern every 2572 lines
# tower grows by 2572 every 1710 pieces
towerCycle = 2572
rocksCycle = 1710

# test
towerCycle = 53
rocksCycle = 37

history = []
for i in range(1000000000000 % rocksCycle + rocksCycle):
# for i in range(1000000):
    # print(i)
    if (highest - towerCycle)in history:
      print(len(history) - history.index(highest - towerCycle))
    history.append(highest)
    start = 2 + (highest + 4) * 1j
    rock = [p + start for p in rocks[i % len(rocks)]]
    canFall = True
    step = 0
    while canFall:
        step += 1
        dir = dirs[dirIndex % len(dirs)]
        dirIndex+=1
        reals = [p.real for p in rock]
        canMoveLeft = (dir < 0 and min(reals) > 0)
        canMoveRight = (dir > 0 and max(reals) < width - 1)
        if (canMoveLeft or canMoveRight) and not(any([p + dir in rockMap for p in rock])):
            rock = [p + dir for p in rock]
        canFall = min([p.imag for p in rock]) > 1 and not(any(p - 1j in rockMap for p in rock))
        if canFall:
          rock = [p - 1j for p in rock]
    for p in rock:
        rockMap.add(p)
    highest = int(max(max([p.imag for p in rock]), highest))

# showMap([]);

# too high 3061

print(highest * (1000000000000 // rocksCycle))


84378378378378
1514285714288
