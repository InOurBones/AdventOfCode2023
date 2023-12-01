import re
import os

input_file = os.path.join(os.path.dirname(__file__), "../../input/day_01.txt")
re_numbers = re.compile(r"[0-9]")

total = 0
with open(input_file, "r") as file:
    for x in file.readlines():
        nums = re_numbers.findall(x)
        total += int(nums[0] + nums[-1])
print(total)
