input = open("input_03").read()

total = 0
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for line in input.strip().split("\n"):
    s = set(line[:len(line)//2]) & set(line[len(line)//2:])
    total += alpha.index(list(s)[0]) + 1
print(total)


total = 0
data = input.strip().split("\n")
for i in range(0, len(data), 3):
    s = set(data[i]) & set(data[i + 1]) & set(data[i + 2])
    total += alpha.index(list(s)[0]) + 1
print(total)

# part1 10:40
# total:17:19
