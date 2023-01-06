import math
import itertools
import re

input = open("input_15").read()

_input = """
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""

lines = input.strip().split("\n")

def man(v):
    return abs(v.real) + abs(v.imag)

def comp(a, b):
    return complex(int(a), int(b))

# vals = [[(comp(a, b), comp(c, d)) for a, b, c, d in re.findall("\d+", line)] for line in lines]
vals = [re.findall("-?\d+", line) for line in lines]
vals = [(comp(a, b), comp(c, d)) for a, b, c, d in vals]
data = [(a, b, man(a - b)) for a, b in vals]

testRow = 2000000 * 1j
# testRow = 10 * 1j



minX = int(min([a.real - d for a, b, d in data]))
minY = int(min([a.imag - d for a, b, d in data]))
maxX = int(max([a.real + d for a, b, d in data]))
maxY = int(max([a.imag + d for a, b, d in data]))

def toS(num):
    return ("0" if 0 <= num < 10 else "") + str(num)

def vis():
    stringMap = []
    for j in range(minY, maxY + 1):
        row = []
        stringMap.append(row)
        for i in range(minX, maxX + 1):
            minDist = math.inf
            char = ""
            pos = i + j * 1j
            for k, (s, b, d) in enumerate(data):
                dist = man(s - pos)
                if pos == s:
                    char = " S"
                    break
                elif pos == b:
                    char = " B"
                    break
                elif dist < minDist and dist <= d:
                    char = toS(k)
                    minDist = dist
                    break
                else: char = " ."
            row.append(char)
    s = []
    for i in range(minX, maxX + 1):
        s.append(str(toS(i - 1)))
    print(" ".join(s))

    for i, j in enumerate(range(minY, maxY + 1)):
        line = stringMap[i];
        l = [toS(j)] + line
        print(" ".join(l))

# vis()

# count = 0
# for i in range(minX, maxX + 1):
#     pos = i + testRow
#     empty = False
#     for s, b, d in data:
#         if pos == s or (pos != b and man(s - pos) <= d):
#             count += 1
#             break
# print(count)

maxCoord = 4000000
_maxCoord = 20

for j in range(0, maxCoord):
    # print(100 * j / maxCoord)
    i = 0
    finished = False
    while i < maxCoord:
      skip = 1
      pos = i + j * 1j
      found = False
      for s, b, d in data:
          diff = s - pos
          if man(diff) <= d:
              thisSkip = abs(d - abs(diff.imag)) + diff.real + 1
              skip = max(thisSkip, skip)
              found = True
      if not(found):
          print(pos.real, pos.imag)
          print(int(pos.real * 4000000 + pos.imag))
          finished = True
          i = maxCoord
          break
      i += skip
    if finished:break

