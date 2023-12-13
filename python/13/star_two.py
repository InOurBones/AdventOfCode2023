import os
from typing import List

input_file = os.path.join(os.path.dirname(__file__), "../../input/day_13.txt")

with open(input_file, "r") as file:
    input = file.read()

def find_reflections(grid, p2=False):

    R = len(grid)
    C = len(grid[0])

    # Columns
    for c in range(1, C):
        l = min(c, C-c)

        errors = 0
        for r in range(R):
            for i in range(l):
                cl = c-1-i
                cr = c+i
                if not grid[r][cl] == grid[r][cr]:
                    errors += 1

        if errors == (1 if p2 else 0):
            return c

    # Row
    for r in range(1, R):
        l = min(r, R-r)

        errors = 0
        for c in range(C):
            for i in range(l):
                rl = r-1-i
                rr = r+i
                if not grid[rl][c] == grid[rr][c]:
                    errors += 1

        if errors == (1 if p2 else 0):
            return r * 100

    return 0


blocks = [block for block in input.split("\n\n")]

# Reflected columns and rows counter
T = 0
for block in blocks:
    grid = [[char for char in line] for line in block.splitlines()]

    # Find reflected columns
    T += find_reflections(grid, True)
print(T)