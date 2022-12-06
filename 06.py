input = open("input_06").read().strip()

def findFirst(n):
    return [i for i in range(0, len(input) - n + 1) if len(set(input[i:i+n])) == n][0] + n

print(findFirst(4))
print(findFirst(14))

# part 1: 6:01
# total: 8:01
