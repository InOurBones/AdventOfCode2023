import os

input_file = os.path.join(os.path.dirname(__file__), "../../input/day_03.txt")

symbol_dict = {}
SYMBOLS = {'#', '$', '%', '&', '*', '+', '-', '/', '=', '@'}
DIGITS = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

with open(input_file, "r") as file:
    lines = file.readlines()

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c in SYMBOLS:
            symbol_dict[(i, j)] = True

ADJECENT = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1)
]

def adjecent_number() -> int:
    for x, y in pos:
        for a, b in ADJECENT:
            if (x + a, y + b) in symbol_dict:
                return int(k)
    return 0

k = ""
pos = []
total = 0
for i, line in enumerate(lines):
    if k:
        total += adjecent_number()
        k = ""
        pos = []
    for j, c in enumerate(line):
        if c in SYMBOLS or c == ".":
            total += adjecent_number()
            k = ""
            pos = []
        if c in DIGITS:
            k += c
            pos.append((i, j))

print(total)