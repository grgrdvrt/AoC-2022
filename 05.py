import re

input = open("input_05").read()

cols, moves = input.split("\n\n")


# manually typed based on input
cols = [
    "HRBDZFLS",
    "TBMZR",
    "ZLCHNS",
    "SCFJ",
    "PGHWRZB",
    "VJZGDNMT",
    "GLNWFSPQ",
    "MZR",
    "MCLGVRT"
]
cols = [list(s) for s in cols]

for line in moves.strip().split("\n"):
    a, b, c = [int(num) - 1 for num in re.findall("\d+", line)]
    slice = cols[b][-(a + 1):]
    # slice.reverse();
    cols[c] += slice
    cols[b] = cols[b][:-(a + 1)]

print("".join([col[-1] for col in cols]))
