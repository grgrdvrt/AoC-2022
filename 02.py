input = open("input_02").read()

_input = """
A Y
B X
C Z
"""
translation = {"X":"A", "Y":"B", "Z":"C"}
scores = {"A":1, "B":2, "C":3}
win = {"A":"C", "B":"A", "C":"B"}
lose = {"C":"A", "A":"B", "B":"C"}
total = 0
for line in input.strip().split("\n"):
    a, b = line[0], translation[line[2]]
    if a == b: score = 3
    elif win[a] == b: score = 0
    else: score = 6
    total += score + scores[b]
print(total)

total = 0
for line in input.strip().split("\n"):
    if line[2] == "X":
        total += scores[win[line[0]]]
    elif line[2] == "Y":
        total += 3 + scores[line[0]]
    elif line[2] == "Z":
        total += 6 + scores[lose[line[0]]]
print(total)
