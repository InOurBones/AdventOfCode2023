import os

input_file = os.path.join(os.path.dirname(__file__), "../../input/day_03.txt")

DIGITS = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

with open(input_file, "r") as file:
    lines = file.readlines()

gears = []
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c in "*":
            gears.append((i, j))

ADJECENT = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1)
]

def adjecent_number(xg, yg) -> int:
    tmp = []
    for number, positions in numbers:
        for a, b in ADJECENT:
            if (xg + a, yg + b) in positions:
                tmp.append(int(number))
                break
    return tmp

k = ""
pos = []
numbers = []
for i, line in enumerate(lines):
    if k:
        numbers.append((k, list(pos)))
        k = ""
        pos = []
    for j, c in enumerate(line):
        if k and c not in DIGITS:
            numbers.append((k, list(pos)))
            k = ""
            pos = []
        if c in DIGITS:
            k += c
            pos.append((i, j))

total = 0
for gear in gears:
    x = adjecent_number(*gear)
    if len(x) == 2:
        total += (x[0] * x[1])
print(total)