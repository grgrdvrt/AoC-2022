input = open("input_10").read()


lines = input.strip().split("\n")
X = 1
cycle = 0
total = 0
for line in lines:

    #read input
    if line == "noop":
        cycles = 1
        val = 0
    else:
        cycles = 2
        val = int(line.split(" ")[1])

    for i in range(cycles):
        cycle += 1
        if (cycle + 20) % 40 == 0:
            total += cycle * X
    X += val
print(total)


lines = input.strip().split("\n")
X = 1
cycle = 0
screen = []
for j in range(6):
    screen.append([])
    for i in range(40):
        screen[j].append(".")
for line in lines:
    #read input
    if line == "noop":
        cycles = 1
        val = 0
    else:
        cycles = 2
        val = int(line.split(" ")[1])

    for i in range(cycles):
        col = cycle % 40
        row = cycle // 40
        cycle += 1
        if X - 1 <= col <= X + 1:
            screen[row][col] = "#"
    X += val
print("\n".join(["".join(line) for line in screen]))
