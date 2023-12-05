import os

input_file = os.path.join(os.path.dirname(__file__), "../../input/day_04.txt")

total = {x: 1 for x in range(196)}  # too lazy to refactor
with open(input_file, "r") as file:
    for idx, x in enumerate(file.readlines()):
        x = x[:-1]
        win_nums, own_nums = x.split(":")[1].split("|")
        win_nums = set(win_nums.split(" "))
        win_nums.remove("")

        match_count = 0
        for y in own_nums.split(" "):
            if y in win_nums:
                match_count += 1
        
        for i in range(idx + 1, idx + match_count + 1):
            total[i] += total[idx]

print(sum(total.values()))