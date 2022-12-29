input = open("input_23").read()

def bbox(elves):
    reals = [int(p.real) for p in elves]
    imags = [int(p.imag) for p in elves]
    return min(reals), max(reals), min(imags), max(imags)


elves = set()
for j, line in enumerate(input.strip().split("\n")):
    for i, c in enumerate(line):
        if c == "#":
            elves.add(i + j * 1j)


n, s, w, e = -1j, 1j, -1, 1
ne, nw, se, sw = n+e, n+w, s+e, s+w
checks = [
    ([n, ne, nw], n),
    ([s, se, sw], s),
    ([w, nw, sw], w),
    ([e, ne, se], e)
]
allDirs = [n, s, w, e, ne, nw, se, sw]
k = 0
while True:
    states = []
    propositions = {}
    for elf in elves:
        needMove = any([elf + d in elves for d in allDirs])
        next = elf
        if needMove:
            for c in checks:
                if not(any([elf + d in elves for d in c[0]])):
                    next = elf + c[1]
                    break
        states.append((elf, next))
        propositions.setdefault(next, 0)
        propositions[next]+=1
    checks = checks[1:] + checks[0:1]

    newElves = set()
    for prev, next in states:
        newElves.add(next if propositions[next] <= 1 else prev)

    k += 1
    if k == 11:
        xMin, xMax, yMin, yMax = bbox(elves)
        total = (xMax - xMin + 1) * (yMax - yMin + 1)
        print("part 1", total - len(elves))

    if elves == newElves:
        print("part 2", k)
        break
    elves = newElves



