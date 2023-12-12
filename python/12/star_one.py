import itertools
import os

input_file = os.path.join(os.path.dirname(__file__), "../../input/day_12.txt")

with open(input_file, "r") as file:
    input = file.read()

# old school brute force
count = 0
for x in input.splitlines():
    rec, nums = x.split(" ")
    nums = [int(x) for x in nums.split(",")]

    known_rec = [idx for idx, r in enumerate(rec) if r == "#"]
    unknown_rec = [idx for idx, r in enumerate(rec) if r == "?"]
    remaining_count = sum(nums) - len(known_rec)

    combi_count = 0
    for combi in itertools.combinations(unknown_rec, remaining_count):
        ranges = []
        range_len = 0
        for idx, r in enumerate(rec):
            if r == "?":
                r = "#" if idx in combi else "."
            if range_len > 0:
                if r == "#":
                    range_len += 1
                else:
                    ranges.append(range_len)
                    range_len = 0
            elif r == "#":
                range_len += 1
        
        if range_len > 0:
            ranges.append(range_len)
        
        if ranges == nums:
            combi_count += 1
    count += combi_count
print(count)