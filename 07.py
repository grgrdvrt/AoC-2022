import re
input = open("input_07").read()


# build tree
def makeDir(parent):
  return {
      "parent":parent,
      "size":0,
      "children":{}
  }

node = makeDir(None)
node["children"]["/"] = makeDir(node)
tree = node

lines = input.strip().split("\n")
for line in lines:
    r = line.split(" ")
    if r[0] == "$":
        if r[1] == "cd":
            # change dir
            if r[2] == "..":
                currSize = node["size"]
                node = node["parent"]
                node["size"] += currSize
            else:
                node = node["children"][r[2]]
    else :
        # read ls result
        child = node["children"].setdefault(r[1], makeDir(node))
        if r[0] != "dir":
            child["size"] = int(r[0])


# collect sizes, recursive
def collectSizes(node):
    for child in node["children"].values():
        node["size"] += collectSizes(child)
    return node["size"]

collectSizes(tree)


#part 1
# collect sizes, recursive
def collectSmallSizes(node):
    # we only consider directories
    if len(node["children"]) == 0:
        return 0
    # collect if size is small enough
    total = node["size"] if node["size"] < 100000 else 0

    # traverse children
    for child in node["children"].values():
        total += collectSmallSizes(child)
    return total

print("part1", collectSmallSizes(tree))


#part 2
totalAvailable = 70000000
requiredSpace = 30000000
totalSize = tree["size"]
currentUnused = totalAvailable - totalSize
minSizeToDelete = requiredSpace - currentUnused

def findSizeToDelete(node, best):
    if minSizeToDelete <= node["size"] < best:
        best = node["size"]
    # find best in children
    for child in node["children"].values():
        if len(child["children"]):
            best = findSizeToDelete(child, best)
    return best

print("part2", findSizeToDelete(tree, totalSize))
