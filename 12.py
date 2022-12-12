input = open("input_12").read()

_input = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""

lines = input.strip().split("\n")

start = (0, 0)
end = (0, 0)
for j, line in enumerate(lines):
    for i, c in enumerate(line):
        if c == "S":
            start = (i, j)
        if c == "E":
            end = (i, j)

alpha = "abcdefghijklmnopqrstuvwxyz"
m = {}
for j, line in enumerate(lines):
    for i, c in enumerate(line):
        if c == "S": c = "a"
        elif c == "E": c = "z"
        m[(i, j)] = alpha.index(c)

neighbours = {}
for x, y in m:
    ns = [
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1),
    ]
    for n in ns:
        if n in m and m[n] - m[(x, y)] <= 1:
            neighbours.setdefault((x, y), [])
            neighbours[(x, y)].append(n)

scores = {}
stack = [start]
scores[start] = 0
parents = {}
while stack:
    pos = stack.pop()
    val = m[pos]
    score = scores[pos]
    for n in neighbours[pos]:
        scores.setdefault(n, 100000000)
        if scores[n] > score + 1:
            stack.append(n)
            scores[n] = score + 1
            parents[n] = pos

count = 0
n = end
while n != start:
    count += 1
    n = parents[n]
print(count)



starts = []
end = (0, 0)
for j, line in enumerate(lines):
    for i, c in enumerate(line):
        if c == "S" or c == "a":
            starts.append((i, j))
        if c == "E":
            end = (i, j)

results = []

for k, start in enumerate(starts):
  scores = {}
  stack = [start]
  scores[start] = 0
  parents = {}
  endVisited = False
  while stack:
      pos = stack.pop()
      val = m[pos]
      score = scores[pos]
      for n in neighbours[pos]:
          scores.setdefault(n, 100000000)
          if scores[n] > score + 1:
              if n == end:
                  endVisited = True
              stack.append(n)
              scores[n] = score + 1
              parents[n] = pos
  print("step", k, len(starts))
  if endVisited:
    count = 0
    n = end
    while n != start:
        count += 1
        n = parents[n]
    results.append(count)
print(min(results))
