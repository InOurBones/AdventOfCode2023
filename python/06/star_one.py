import re
import math
import os

input_file = os.path.join(os.path.dirname(__file__), "../../input/day_06.txt")

with open(input_file, "r") as file:
    input = file.read()

time_arr, distance_arr = [re.sub("\s+", " ", x.split(":")[1]).strip().split(" ") for x in input.split("\n")]
time_arr = [int(x) for x in time_arr]
distance_arr = [int(x) for x in distance_arr]

bottom_arr = []
top_arr = []
for time, distance in zip(time_arr, distance_arr):

    # top to bot
    time_held = time - 1
    while time_held > 0:
        time_remaining = time - time_held
        distance_calc = time_remaining * time_held

        if distance_calc > distance:
            top_arr.append(time_held)
            break
        
        time_held -= 1

    # bot to top
    time_held = 1
    while time_held < time - 1:
        time_remaining = time - time_held
        distance_calc = time_remaining * time_held

        if distance_calc > distance:
            bottom_arr.append(time_held)
            break

        time_held += 1

total = math.prod([top - bottom + 1 for top, bottom in zip(top_arr, bottom_arr)])
print(total)