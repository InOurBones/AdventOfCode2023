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

# list coords
coords = []
for y in range(len(input)):
    for x in range(len(input[0])):
        if input[y][x] == "#":
            coords.append((x, y))

# expand coords
expand_by = 1_000_000 - 1
for idx, coord in enumerate(coords):
    x, y = coord
    for row_idx, row in enumerate(empty_rows, 1):
        if y < row:
            row_idx -= 1
            break
    if row_idx != 0:
        y += (expand_by * row_idx)

    for col_idx, col in enumerate(empty_columns, 1):
        if x < col:
            col_idx -= 1
            break
    if col_idx != 0:
        x += (expand_by * col_idx)
    coords[idx] = (x, y)

# find distance between each coords
total = 0
for a in range(len(coords)):
    for b in range(a):
        total += abs((coords[a][1] - coords[b][1])) + abs((coords[a][0] - coords[b][0]))
        
print(total)
