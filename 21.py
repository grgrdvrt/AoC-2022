import re
input = open("input_21").read()

_input ="""
root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
"""


def evalNode(nodes, node):
    if node[0] != None:
        return node[0]

    n1, n2 = nodes[node[1][0]], nodes[node[1][1]]

    evalNode(nodes, n1)
    evalNode(nodes, n2)

    match node[2]:
        case "+":
          node[0] = n1[0] + n2[0]
        case "-":
          node[0] = n1[0] - n2[0]
        case "*":
          node[0] = n1[0] * n2[0]
        case "/":
          node[0] = n1[0] / n2[0]

    return node[0]

nodes = {}


"""
nodes:{
    name:{
        value:None | 0,
        dependencies:["a", "b"]
        op:add|sub|mul|div
    }
}
"""


for desc in input.strip().split("\n"):
    name, val = desc.split(": ")
    num = re.findall("-?\d+", val)
    node = [None, [], None]
    if num:
        node[0] = int(num[0])
    else:
        op = re.findall("[+\-*/]", val)[0]
        node[1] = val.split(str(" " + op + " "))
        node[2] = op
    nodes[name] = node

print(evalNode(nodes, nodes["root"]))

def resetNodes(nodes):
  for name in nodes:
      n = nodes[name]
      if n[2] != None:
          n[0] = None

def f(x):
  resetNodes(nodes)
  nodes["humn"][0] = x
  return evalNode(nodes, nodes[nodes["root"][1][0]])

def g(x):
  return evalNode(nodes, nodes[nodes["root"][1][1]])

# f is the composition of monotonic functions. We can bissect.
target = g(0)
a = 10000000000000
b = 0
fa = f(a)
fb = f(b)

while True:
    mid = (a + b)//2
    fmid = f(mid)
    if fmid == target:
        print(mid)
        break
    elif (fa <= target <= fmid) or (fa >= target >= fmid):
        b, fb = mid, fmid
    elif (fb <= target <= fmid) or (fb >= target >= fmid):
        a, fa = mid, fmid
