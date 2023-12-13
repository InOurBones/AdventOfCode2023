import os
from typing import List

input_file = os.path.join(os.path.dirname(__file__), "../../input/day_13.txt")

with open(input_file, "r") as file:
    input = file.read()

def search_rows(rows: List[str]) -> int:
    possible_mirrors = []
    for i in range(0, len(rows) - 1):
        if rows[i] == rows[i + 1]:
            possible_mirrors.append((i, i + 1))

    for left, right in possible_mirrors:
        rows_to_check = min(left, len(rows) - right - 1)
        is_a_mirror = True
        for i in range(1, rows_to_check + 1):
            if rows[left - i] != rows[right + i]:
                is_a_mirror = False
                break

        if is_a_mirror:
            return right

def search_columns(rows: List[str]) -> int:
    new_rows = []
    for i in range(len(rows[0])):
        new_rows.append("".join(r[i] for r in rows))
    return search_rows(new_rows)

row_list = []
for map in input.split("\n\n"):
    rows = map.split("\n")

    idx = search_rows(rows)
    if idx is None:
        idx = search_columns(rows)
    else:
        idx *= 100
    row_list.append(idx)
print(sum(row_list))