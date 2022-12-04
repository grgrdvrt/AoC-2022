import re

input = open("input").read()

ranges = [ [int(v) for v in re.findall("\d+", line)] for line in input.strip().split("\n") ]

total = sum((a <= c and b >= d) or (c <= a and d >= b) for a, b, c, d in ranges)
print(total)

total = sum(not(b < c or d < a) for a, b, c, d in ranges)
print(total)

# part 1: 3:18
# total: 5:05
