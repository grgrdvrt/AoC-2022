input = open("input_24").read()

left, right, up, down, stay = dirs = [-1, 1, -1j, 1j, 0]
dirsMap = {"<":left, ">":right, "^":up, "v":down}
blizzards = []
lines = input.strip().split("\n")
xMin, xMax = 1, len(lines[0].strip()) - 2
yMin, yMax = 1, len(lines) - 2

for j, line in enumerate(lines):
    for i, c in enumerate(line.strip()):
        if c in dirsMap:
            blizzards.append((i + j * 1j, dirsMap[c], c))

def find(blizzards, initialPosition, finalPosition):
    paths = set()
    paths.add(initialPosition)
    steps = 0
    while True:
        steps += 1

        #update blizzards
        newBlizzards = []
        for b in blizzards:
            pos = b[0] + b[1]
            if pos.real > xMax: pos = xMin + pos.imag * 1j
            elif pos.real < xMin: pos = xMax + pos.imag * 1j
            if pos.imag > yMax: pos = pos.real + yMin * 1j
            elif pos.imag < xMin: pos = pos.real + yMax * 1j
            newBlizzards.append((pos, b[1], b[2]))
        blizzards = newBlizzards

        occupied = set()
        for b in blizzards:
            occupied.add(b[0])


        #find new positions
        newPaths = set()
        for pos in paths:
            for d in dirs:
                nextPos = pos + d
                if nextPos == finalPosition:
                    return steps, blizzards
                elif not(nextPos in occupied) and xMin <= nextPos.real <= xMax and yMin <= nextPos.imag <= yMax:
                    newPaths.add(nextPos)
                elif nextPos == initialPosition:
                    newPaths.add(nextPos)
        paths = newPaths


initialPosition = xMin + (yMin - 1) * 1j
finalPosition = xMax + (yMax + 1) * 1j

t1, b1 = find(blizzards, initialPosition, finalPosition)
print("part1", t1)
t2, b2 = find(b1, finalPosition, initialPosition)
t3, b3 = find(b2, initialPosition, finalPosition)
print("part2", t1 + t2 + t3)
