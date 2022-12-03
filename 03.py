input = open("input_03").read()

total = 0
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for line in input.strip().split("\n"):
    a = line[:len(line)//2]
    b = line[len(line)//2:]
    pri = alpha.index(list(set(a).intersection(set(b)))[0]) + 1
    total += pri
print(total)


total = 0
data = input.strip().split("\n")
for i in range(0, len(data), 3):
    s1, s2, s3 = set(data[i]), set(data[i + 1]), set(data[i + 2]);
    s = (s1.intersection(s2, s3)).intersection(s3)
    pri = alpha.index(list(s)[0]) + 1
    total += pri
print(total)

# part1 10:40
# total:17:19
