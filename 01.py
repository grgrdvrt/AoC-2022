input = open("input").read().strip().split("\n\n")
sums = [sum([int(num) for num in nums]) for nums in [vals.split("\n") for vals in input]]
print(max(sums));
print(sum(sorted(sums)[-3:]))

# part1 3:30
# total: 9:14
