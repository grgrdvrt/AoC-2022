input = open("input_09").read()

_input = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""


dirs = {
    "U":(0, -1),
    "L":(-1, 0),
    "R":(1, 0),
    "D":(0, 1),
}

lines = input.strip().split("\n")
visited = set()
head = (0, 0)
tail = (0, 0)

visited.add(tail)
for line in lines:
    dir = dirs[line[0]]
    for i in range(int(line[2:])):
        # print(dir)
        head = (head[0] + dir[0], head[1] + dir[1])
        diff = (head[0] - tail[0], head[1] - tail[1])
        dist = max(abs(diff[0]), abs(diff[1]))
        if dist > 1:
            a, b = diff
            a = max(-1, min(a, 1))
            b = max(-1, min(b, 1))
            tail = (tail[0] + a, tail[1] + b)
        visited.add(tail)
    visited.add(tail)
# print(visited)

# xMin = min([p[0] for p in visited])
# yMin = min([p[1] for p in visited])
# xMax = max([p[0] for p in visited])
# yMax = max([p[1] for p in visited])
# for j in range(yMin, yMax + 1):
#     str = ""
#     for i in range(xMin, xMax + 1):
#         str += "#" if (i, j) in visited else "."
#     print(str)

# print(len(visited))

# 3000 to low


_input = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""


lines = input.strip().split("\n")
visited = set()
head = (0, 0)
knots = [(0, 0)]*9

visited.add(tail)
for line in lines:
    dir = dirs[line[0]]
    for i in range(int(line[2:])):
        # print(dir)
        head = (head[0] + dir[0], head[1] + dir[1])
        prev = head
        for k in range(9):
            knot = knots[k]
            diff = (prev[0] - knot[0], prev[1] - knot[1])
            dist = max(abs(diff[0]), abs(diff[1]))
            if dist > 1:
                a, b = diff
                a = max(-1, min(a, 1))
                b = max(-1, min(b, 1))
                knots[k] = (knot[0] + a, knot[1] + b)
            prev = knots[k]
        visited.add(knots[8])
# print(visited)

xMin = min([p[0] for p in visited])
yMin = min([p[1] for p in visited])
xMax = max([p[0] for p in visited])
yMax = max([p[1] for p in visited])
for j in range(yMin, yMax + 1):
    str = ""
    for i in range(xMin, xMax + 1):
        str += "#" if (i, j) in visited else "."
    print(str)

print(len(visited))

# part 1: 20:20
# total: 30:52
