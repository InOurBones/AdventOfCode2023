import os

input_file = os.path.join(os.path.dirname(__file__), "../../input/day_15.txt")

with open(input_file, "r") as file:
    input = file.read()

total = 0
for x in input.split(","):
    sub_total = 0
    for char in x:
        sub_total = ((ord(char) + sub_total) * 17) % 256
    total += sub_total
print(total)