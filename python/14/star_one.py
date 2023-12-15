import os
from typing import List, Union

input_file = os.path.join(os.path.dirname(__file__), "../../input/day_14.txt")

with open(input_file, "r") as file:
    input = file.read()

input = input.splitlines()

def get_clean_map(input: List[str]) -> List[Union[List[str], str]]:
    clean_map = []
    for x in range(len(input[0])):
        tmp_row = []
        tmp = []
        for y in range(len(input)):
            char = input[y][x]

            if char == "O":
                tmp.append(int(y))
            if char == "#":
                if tmp != []:
                    tmp_row.append(tmp)
                    tmp = []
                tmp_row.append(int(y))
        if tmp != []:
            tmp_row.append(tmp)
        clean_map.append(tmp_row)
    return clean_map

total = 0
input_length = len(input)
for row in get_clean_map(input):
    stationary_block = 0
    for entry in row:
        if type(entry) == int:
            stationary_block = entry + 1
        else:
            total += sum( (input_length - i - stationary_block) for i in range(len(entry)))
print(total)