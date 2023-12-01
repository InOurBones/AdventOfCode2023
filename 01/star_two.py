import re
import os

input_file = os.path.join(os.path.dirname(__file__), "./input.txt")
re_numbers = re.compile(r"[0-9]")

map_nums = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e"
}

total = 0
with open(input_file, "r") as file:
    for x in file.readlines():
        for key, value in map_nums.items():
            x = x.replace(key, value)
        nums = re_numbers.findall(x)
        total += int(nums[0] + nums[-1])
print(total)
