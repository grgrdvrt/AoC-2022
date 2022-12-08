input = open("input").read()

_input = """
30373
25512
65332
33549
35390
"""

lines = input.strip().split("\n")


width = len(lines[0])
height = len(lines)
visibilities = {}
for j in range(height):
    for i in range(width):
        visibilities[(i, j)] = False

for j in range(height):
    val = -1
    for i in range(width):
        vis = int(lines[j][i]) > val
        if vis: val = int(lines[j][i])
        visibilities[(i, j)] = vis or visibilities[(i, j)]

    val = -1
    for i in range(width - 1, -1, -1):
        vis = int(lines[j][i]) > val
        if vis: val = int(lines[j][i])
        visibilities[(i, j)] = vis or visibilities[(i, j)]


for i in range(width):
    val = -1
    for j in range(height):
        vis = int(lines[j][i]) > val
        if vis: val = int(lines[j][i])
        visibilities[(i, j)] = vis or visibilities[(i, j)]

    val = -1
    for j in range(height - 1, -1, -1):
        vis = int(lines[j][i]) > val
        if vis: val = int(lines[j][i])
        visibilities[(i, j)] = vis or visibilities[(i, j)]


print(sum(visibilities.values()))


maxVal = max([max([int(c) for c in line]) for line in lines])

result = 0
for j in range(height):
    for i in range(width):
        v = int(lines[j][i])
        t = 1
        #up
        c = 0
        for a in range(j - 1, -1, -1):
            c += 1
            if int(lines[a][i]) >= v: break
        t *= c
        #left
        c = 0
        for a in range(i - 1, -1, -1):
            c += 1
            if int(lines[j][a]) >= v: break
        t *= c
        #right
        c = 0
        for a in range(i + 1, width):
            c += 1
            if int(lines[j][a]) >= v: break
        t *= c
        #down
        c = 0
        for a in range(j + 1, height):
            c += 1
            if int(lines[a][i]) >= v: break
        t *= c
        if t > result:
            result = t
print(result)
