import re
input = open("input_11").read()


monkeys = [monkey.strip().split("\n") for monkey in input.strip().split("\n\n")]

values = [[[int(v) for v in re.findall("\d+", line)] for line in monkey] for monkey in monkeys]
ops =[lines[2][23] for lines in monkeys]

inspected = [0 for m in monkeys]

for i in range(20):
    for i, nums in enumerate(values):
        op = ops[i]
        for item in nums[1]:
            val2 = nums[2][0] if len(nums[2]) else item
            if op == "+":
                val = item + val2
            elif op == "*":
                val = item * val2
            val = val // 3
            inspected[i] += 1
            if val % nums[3][0] == 0:
                values[nums[4][0]][1].append(val)
            else:
                values[nums[5][0]][1].append(val)
        values[i][1] = []

inspected.sort(reverse=True)
print(inspected[0] * inspected[1])



values = [[[int(v) for v in re.findall("\d+", line)] for line in monkey] for monkey in monkeys]
ops =[lines[2][23] for lines in monkeys]

inspected = [0 for m in monkeys]
prod = 1
for v in [nums[3][0] for nums in values]:
    prod *= v

for i in range(10000):
    for i, nums in enumerate(values):
        op = ops[i]
        for item in nums[1]:
            val2 = nums[2][0] if len(nums[2]) else item
            if op == "+":
                val = item + val2
            elif op == "*":
                val = item * val2
            val = val % prod
            inspected[i] += 1
            if val % nums[3][0] == 0:
                values[nums[4][0]][1].append(val)
            else:
                values[nums[5][0]][1].append(val)
        values[i][1] = []

inspected.sort(reverse=True)
print(inspected[0] * inspected[1])

# 20733984048 too high
# 14399879998 too low
# 14561971968


# part1: 27:15
# total: 35:45
