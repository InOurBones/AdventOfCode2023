import os
from typing import List, Tuple

input_file = os.path.join(os.path.dirname(__file__), "../../input/day_05.txt")

with open(input_file, "r") as file:
    input = file.read()

def find_intersect(l1: List[int], l2: List[int]) -> Tuple:
    min_intersect = max(l1[0],l2[0])
    max_intersect = min(l1[1],l2[1])
    if min_intersect>max_intersect:
        return tuple()
    return (min_intersect,max_intersect)

def create_seed_ranges(iterable):
    l = []
    for x in range(0,len(iterable),2):
        l.append((iterable[x],iterable[x]+iterable[x+1]-2))
    return l

def convert_map(map_item):
    return [convert_map_line(line) for line in map_item]

def convert_map_line(line):
    dst, src, l = [int(x) for x in line.split()]
    linerange = (src, src+l-1)
    return [linerange, dst]

def map_intersect(mapping, intersect):
    mapping_range = mapping[0]
    diff_lower = intersect[0]-mapping_range[0]
    intersect_len = intersect[1]-intersect[0]
    retval = (mapping[1]+diff_lower,mapping[1]+diff_lower+intersect_len)
    return retval

def process_map_seeds(map,seeds):
    ranges = []
    while len(seeds)>0:
        item = seeds.pop(0)
        len_before = len(ranges)
        for mapping in map:
            intersect = find_intersect(item, mapping[0])
            if intersect==tuple():
                continue
            ranges.append(map_intersect(mapping,intersect))
            if intersect[0]==item[0] and intersect[1] == item[1]:
                break
            
        if len_before == len(ranges):
            ranges.append(item)
    return ranges

maps = input.split("\n\n")
seeds = create_seed_ranges([int(x) for x in maps.pop(0).split(": ")[1].split(" ")])
maps = [x.split("\n")[1:] for x in maps]

for map_item in maps:
    seedlist = process_map_seeds(convert_map(map_item), seedlist)
print(min([item[0] for item in seedlist]))
