import math
import itertools
import re

input = open("input_16").read()

_input = """
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
"""

start = "AA"
lines = input.strip().split("\n")
for line in lines:
    p = re.findall(r"[A-Z]{2}", line)
    rate = int(re.findall(r"\d+", line)[0])
print(t)

# récupérer les chemins entre chaque paire de valve qui ont un rate > 0
# chaque arete est un couple (time, rate)
# collecter les combinaisons possibles
