import math
import os

input_file = os.path.join(os.path.dirname(__file__), "../../input/day_08.txt")

with open(input_file, "r") as file:
    input = file.read()

directions = list(input.split("\n")[0])
input_lines = input.split("\n")[2:]

NODES = {}
for x in input_lines:
    key, value = x.split(" = ")
    left, right = value[1:-1].split(", ")
    NODES[key] = (left, right)

counts = []
for cur in [x for x in NODES.keys() if x.endswith("A")]:
    count = 0
    while not cur.endswith("Z"):
        for d in directions:
            count += 1
            cur = NODES[cur][int(d == "R")]
            if cur.endswith("Z"):
                break
    counts.append(count)

lcm = 1
for i in counts:
    lcm = lcm * i // math.gcd(lcm, i)

print(lcm)
