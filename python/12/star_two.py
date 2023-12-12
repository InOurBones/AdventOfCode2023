import os

input_file = os.path.join(os.path.dirname(__file__), "../../input/day_12.txt")

with open(input_file, "r") as file:
    input = file.read()

ways = {}

def find_ways(kw, dl, status, start):
    tt = (kw, tuple(dl), status)
    if tt in ways:
        return ways[tt]
    if len(dl) == 0:
        if kw != len(status):
            ways[tt] = 0
            return 0
        if any(c == "#" for c in status):
            ways[tt] = 0
            return 0
        else:
            ways[tt] = 1
            return 1

    w = 0
    for i, c in enumerate(status):
        if i == kw or c == "#":
            if i == 0 and not start:
                # must take at least one
                ways[tt] = 0
                return 0
            # working stops here
            w += find_ways_dam(kw - i, dl, status[i:])
            break
        if c == ".":
            # no choice
            continue
        if i > 0 or start:
            # "?", working might stop here
            w += find_ways_dam(kw - i, dl, status[i:])

    ways[tt] = w
    return w

def find_ways_dam(kw, dl, status):
    assert(len(dl) > 0)
    assert(dl[0] <= len(status))
    if any(c == "." for c in status[:dl[0]]):
        return 0
    return find_ways(kw, dl[1:], status[dl[0]:], False)

total = 0
for line_i, line in enumerate(input.splitlines()):
    line = line.strip()
    status, damaged_lengths = line.split(" ")
    status = "?".join([status] * 5)
    damaged_lengths = tuple(map(int, damaged_lengths.split(",")))
    damaged_lengths = damaged_lengths * 5

    num_working = len(status) - sum(damaged_lengths)
    assert(num_working >= 0)
    
    hw = find_ways(num_working, damaged_lengths, status, True)
    total += hw

print(total)
