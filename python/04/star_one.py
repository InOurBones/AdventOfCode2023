import os

input_file = os.path.join(os.path.dirname(__file__), "../../input/day_04.txt")

total = 0
with open(input_file, "r") as file:
    for x in file.readlines():
        x = x[:-1]
        win_nums, own_nums = x.split(":")[1].split("|")
        win_nums = set(win_nums.split(" "))
        win_nums.remove("")

        sub_count = 0.5
        for y in own_nums.split(" "):
            if y in win_nums:
                sub_count *= 2
        
        if sub_count != 0.5:
            total += int(sub_count)

print(total)