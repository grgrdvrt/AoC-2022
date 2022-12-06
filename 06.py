input = open("input_06").read()

input = input.strip()
for i in range(0, len(input) - 3):
    if len(set(input[i:i+4])) == 4:
        print(i + 4)
        break;


input = input.strip()
n = 14
for i in range(0, len(input) - n + 1):
    if len(set(input[i:i+n])) == n:
        print(i + n)
        break;

# part 1: 6:01
# total: 8:01
