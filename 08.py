input = open("input_08").read()

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

trees = [[int(c) for c in line] for line in lines]

result = 0
for j in range(height):
    for i in range(width):
        val = trees[j][i]
        left = max(trees[j][0:i], default=-1)
        right = max(trees[j][i+1:], default=-1)
        top = max([line[i] for line in trees[:j]], default=-1)
        bottom = max([line[i] for line in trees[j+1:]], default=-1)
        result += min(left, right, top, bottom) < val

print(result)



result = 0
for j in range(height):
    for i in range(width):
        v = trees[j][i]
        up = 0
        for a in range(j - 1, -1, -1):
            up += 1
            if trees[a][i] >= v: break
        left = 0
        for a in range(i - 1, -1, -1):
            left += 1
            if trees[j][a] >= v: break
        right = 0
        for a in range(i + 1, width):
            right += 1
            if trees[j][a] >= v: break
        down = 0
        for a in range(j + 1, height):
            down += 1
            if trees[a][i] >= v: break
        t = up * left * right * down
        if t > result:
            result = t
print(result)
