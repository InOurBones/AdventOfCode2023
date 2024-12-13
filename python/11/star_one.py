import os

input_file = os.path.join(os.path.dirname(__file__), "../../input/day_11.txt")

with open(input_file, "r") as file:
    input = file.read()

# create map
input = [list(x) for x in input.splitlines()]

# find empty columns and rows
empty_rows = []
for idx, x in enumerate(input):
    if "#" not in x:
        empty_rows.append(idx)

empty_columns = []
for idx in range(len(input[0])):
    galaxy_found = False
    for x in input:
        if x[idx] == "#":
            galaxy_found = True
            break
    if not galaxy_found:
        empty_columns.append(idx)

# expand map
for x in input:
    for idx, col in enumerate(empty_columns):
        x.insert(col + idx, ".")
for idx, x in enumerate(empty_rows):
    input.insert(x + idx, ["."] * len(input[0]))

# list coords
coords = []
for y in range(len(input)):
    for x in range(len(input[0])):
        if input[y][x] == "#":
            coords.append((x, y))

# find distance between each coords
total = 0
for a in range(len(coords)):
    for b in range(a):
        total += abs((coords[a][1] - coords[b][1])) + abs((coords[a][0] - coords[b][0]))
        
print(total)
