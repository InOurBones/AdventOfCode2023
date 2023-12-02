import math
import os

input_file = os.path.join(os.path.dirname(__file__), "../../input/day_02.txt")

total = 0
with open(input_file, "r") as file:
    for x in file.readlines():
        inventory = {}

        x = x[:-1]  # remove \n
        _, input = x.split(": ")
        for s in input.replace(",", ";").split("; "):
            count_str, cube = s.split(" ")
            count = int(count_str)
            if (cube not in inventory) or (count > inventory[cube]):
                inventory[cube] = count
        total += math.prod(inventory.values())
print(total)