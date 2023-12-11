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

count = 0
cur = "AAA"
while cur != "ZZZ":
    for d in directions:
        count += 1
        cur = NODES[cur][int(d == "R")]
        if cur == "ZZZ":
            break
            
print(count)