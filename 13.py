import functools
import re
input = open("input_13").read()

_input = """"""

def compare(a, b):
    comp = 0
    if not(isinstance(a, list)) and not(isinstance(b, list)):
        comp = a - b
    elif not(isinstance(a, list)) and isinstance(b, list):
        comp = compare([a], b)
    elif not(isinstance(b, list)) and isinstance(a, list):
        comp = compare(a, [b])
    else:
        comp = 0
        for c, d in zip(a, b):
            comp = compare(c, d)
            if comp != 0:
                break;
        if comp == 0:
            comp = len(a) - len(b)

    return max(-1, min(1, comp))

pairs = [[eval(p) for p in pair.strip().split("\n")] for pair in input.strip().split("\n\n")]
count = 0
for i, (a, b) in enumerate(pairs):
    if compare(a, b) < 0:
        count += i + 1
print(count)




packets = [eval(packet) for packet in re.split("\n+", input.strip())]
packets.append([[2]])
packets.append([[6]])
cmp = functools.cmp_to_key(compare)
packets.sort(key=cmp)

print((1 + packets.index([[2]])) * (1 + packets.index([[6]])))

#part1: 19:28
#total: 28:18
