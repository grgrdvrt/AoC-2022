import math
import itertools
import re

input = open("input_23").read()

_input = """
....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..
"""

_input = """
..##.
..#..
.....
..##.
.....
"""

def bbox(elves):
    reals = [int(p.real) for p in elves]
    imags = [int(p.imag) for p in elves]
    return min(reals), max(reals), min(imags), max(imags)

def printElves(elves):
    xMin, xMax, yMin, yMax = bbox(elves)
    for j in range(yMin, yMax + 1):
        s = ""
        for i in range(xMin, xMax + 1):
            s += "#" if (i + j * 1j in elves) else "."
        print(s)


elves = set()
for j, line in enumerate(input.strip().split("\n")):
    for i, c in enumerate(line):
        if c == "#":
            elves.add(i + j * 1j)

# printElves(elves)

n, s, w, e = -1j, 1j, -1, 1
ne, nw, se, sw = n+e, n+w, s+e, s+w
checks = [
    ([n, ne, nw], n),
    ([s, se, sw], s),
    ([w, nw, sw], w),
    ([e, ne, se], e)
]
allDirs = [n, s, w, e, ne, nw, se, sw]
k = 0
while True:
    states = []
    propositions = {}
    for elf in elves:
        needMove = any([elf + d in elves for d in allDirs])
        next = elf
        if needMove:
            for c in checks:
                if not(any([elf + d in elves for d in c[0]])):
                    next = elf + c[1]
                    break
        states.append((elf, next))
        propositions.setdefault(next, 0)
        propositions[next]+=1
    checks = checks[1:] + checks[0:1]

    newElves = set()
    for prev, next in states:
        newElves.add(next if propositions[next] <= 1 else prev)

    k += 1
    if elves == newElves:
        print(k)
        break
    elves = newElves
    # print("\nround " + str(i + 1))
    # printElves(elves)



xMin, xMax, yMin, yMax = bbox(elves)
total = (xMax - xMin + 1) * (yMax - yMin + 1)
print(total - len(elves))


# 4044 too high

# part2
# 16308 too high
