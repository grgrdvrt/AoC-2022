import re

input = open("input").read()

_input = """
"""
lines = input.strip().split("\n")
total = 0
for line in lines:
    a, b, c, d = [int(v) for v in re.findall("\d+", line)];
    if (a <= c and b >= d) or (c <= a and d >= b):
        total += 1
print(total)

total = 0
for line in lines:
    a, b, c, d = [int(v) for v in re.findall("\d+", line)];
    if not(b < c or d < a): total += 1
print(total)

# part 1: 3:18
# total: 5:05
