import re
input = open("input").read()

_input ="""
"""

boardMapInput, pathInput = input.strip().split("\n\n")
lines = boardMapInput.strip().split("\n")

boardMap = set()
rowsRanges = []
for j, line in enumerate(boardMapInput.strip().split("\n")):
    begin = 0
    end = len(line)
    for i, c in enumerate(line):
        if c == " ":
            begin += 1
        if c == "#":
            boardMap.add(i + j * 1j);
    rowsRanges.append((begin, end))


distances = [int(v) for v in re.split("R|L", pathInput.strip())]
turns = [1j if t == "L" else -1j  for t in re.split("\d+", pathInput.strip()) if t]
print(len(distances), len(turns))



dir = 1
pos = 0

for i, d in enumerate(distances):
    for j in range(d):
        nextPos = pos + dir
        begin, end = rowsRanges[int(nextPos.imag)]
        if nextPos.real > end: pos = begin + pos.imag * 1j
        elif nextPos.real < begin: pos = end + pos.imag * 1j
        if nextPos.imag < 0: pos = pos.real + len(rowsRanges) - 1
        elif nextPos.imag > len(rowsRanges) - 1: pos = pos.real
        if (next + dir) in boardMap: break
        else: nextPos = nextPos
    if i < len(turns):
        dir *= turns[i]

row = int(pos.real) + 1
col = int(pos.imag) + 1
facing = 0
match dir:
    case 1:facing = 0
    case 1j:facing = 1
    case -1:facing = 2
    case -1j:facing = 3

password = 1000 * row + 4 * col + facing
print(password)
