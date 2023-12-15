import os

input_file = os.path.join(os.path.dirname(__file__), "../../input/day_14.txt")

with open(input_file, "r") as file:
    input = file.read()

input = input.splitlines()

cycles = 1_000_000_000
seen = []

grid = ["".join([line[i] for line in input[::-1]]) for i in range(len(input[0]))]
for i in range(cycles):
    for _ in range(4):
        # tilt grid
        grid = ["#".join("".join(sorted(chunk)) for chunk in column.split("#")) for column in grid]
        # rotate grid
        grid = ["".join([line[i] for line in grid[::-1]]) for i in range(len(grid[0]))]
    grid_str = "\n".join(grid)
    if grid_str in seen:
        seen_idx = seen.index(grid_str)
        break
    seen.append(grid_str)

cycle_length = i - seen_idx
seen_idx = seen_idx + (cycles - seen_idx) % cycle_length - 1
total = sum((i + 1) for col in seen[seen_idx].splitlines() for i in range(len(col)) if col[i] == "O")
print(total)