import re
import os

input_file = os.path.join(os.path.dirname(__file__), "../../input/day_06.txt")

with open(input_file, "r") as file:
    input = file.read()

time, distance = [int(re.sub("\s+", "", x.split(":")[1])) for x in input.split("\n")]

top = None
bottom = None

# top to bot
time_held = time - 1
while time_held > 0:
    time_remaining = time - time_held
    distance_calc = time_remaining * time_held

    if distance_calc > distance:
        top = time_held
        break
    
    time_held -= 1

# bot to top
time_held = 1
while time_held < time - 1:
    time_remaining = time - time_held
    distance_calc = time_remaining * time_held

    if distance_calc > distance:
        bottom = time_held
        break

    time_held += 1

total = top - bottom + 1
print(total)