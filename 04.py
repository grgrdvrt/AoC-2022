input = open("input").read()

_input = """
"""
lines = input.strip().split("\n")
total = 0
for line in lines:
    a, b = line.split(",")
    ra = a.split("-")
    rb = b.split("-")
    ra = [int(ra[0]), int(ra[1])]
    rb = [int(rb[0]), int(rb[1])]
    if (ra[0] <= rb[0] and ra[1] >= rb[1]) or (rb[0] <= ra[0] and rb[1] >= ra[1]):
        total += 1
print(total)


_input = """
"""
lines = input.strip().split("\n")
total = 0
for line in lines:
    a, b = line.split(",")
    ra = a.split("-")
    rb = b.split("-")
    ra = [int(ra[0]), int(ra[1])]
    rb = [int(rb[0]), int(rb[1])]
    if (ra[0] <= rb[0] <= ra[1]) or (ra[0] <= rb[1] <= ra[1]) or (rb[0] <= ra[0] <= rb[1]) or (rb[0] <= ra[1] <= rb[1]):
        total += 1
print(total)

# part 1: 3:18
# total:5:05
