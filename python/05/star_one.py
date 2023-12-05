import os

input_file = os.path.join(os.path.dirname(__file__), "../../input/day_05.txt")

with open(input_file, "r") as file:
    input = file.read()

seeds, *maps = input.split("\n\n")
seeds_arr = [int(x) for x in seeds.split(": ")[1].split(" ")]

seeds_dct = {x: x for x in seeds_arr}
for x in maps:
    for y in x.split("\n")[1:]:
        dst_start, src_start, rng = [int(z) for z in y.split(" ")]

        for seed in seeds_dct.keys():
            if seed >= src_start and seed <= src_start + rng - 1:
                seeds_dct[seed] = dst_start + (seed - src_start)

    seeds_dct = {x: x for x in seeds_dct.values()}
print(min(seeds_dct.values()))