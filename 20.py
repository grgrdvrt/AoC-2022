import re
input = open("input").read()

_input ="""
1
2
-3
3
-2
0
4
"""

nums = [[int(re.findall("-?\d+", line)[0]), None, None] for i, line in enumerate(input.strip().split("\n"))]
zero = None
for i, num in enumerate(nums):
    num[1] = nums[(i - 1 + len(nums)) % len(nums)]
    num[2] = nums[(i + 1) % len(nums)]
    if num[0] == 0:
        zero = num

count = len(nums)
for num in nums:
    prev, next = num[1], num[2]
    prev[2] = next
    next[1] = prev
    newPrev = num[1]
    steps = ((num[0] % (count - 1)) + (count - 1)) % (count - 1)
    for i in range(steps):
        newPrev = newPrev[2]
    num[1] = newPrev
    num[2] = newPrev[2]
    num[1][2] = num
    num[2][1] = num

a = zero
for i in range(1000 % count): a = a[2]
b = a
for i in range(1000 % count): b = b[2]
c = b
for i in range(1000 % count): c = c[2]

print(a[0] + b[0] + c[0])

# too low 2473





nums = [[int(re.findall("-?\d+", line)[0]) * 811589153, None, None] for i, line in enumerate(input.strip().split("\n"))]
zero = None
for i, num in enumerate(nums):
    num[1] = nums[(i - 1 + len(nums)) % len(nums)]
    num[2] = nums[(i + 1) % len(nums)]
    if num[0] == 0:
        zero = num

count = len(nums)
for i in range(10):
    for num in nums:
        prev, next = num[1], num[2]
        prev[2] = next
        next[1] = prev
        newPrev = num[1]
        steps = ((num[0] % (count - 1)) + (count - 1)) % (count - 1)
        for i in range(steps):
            newPrev = newPrev[2]
        num[1] = newPrev
        num[2] = newPrev[2]
        num[1][2] = num
        num[2][1] = num

a = zero
for i in range(1000 % count): a = a[2]
b = a
for i in range(1000 % count): b = b[2]
c = b
for i in range(1000 % count): c = c[2]

print(a[0] + b[0] + c[0])

# too low 2473
