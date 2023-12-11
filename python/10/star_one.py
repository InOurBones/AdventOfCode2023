import os
import re
from typing import Tuple

input_file = os.path.join(os.path.dirname(__file__), "../../input/day_10.txt")

with open(input_file, "r") as file:
    input = file.read()

SYMBOL_TO_CONNECTIONS = {
    "|": ["NS", "NS"],
    "-": ["EW", "EW"],
    "L": ["NE", "SW"],
    "J": ["NW", "ES"],
    "7": ["SW", "NE"],
    "F": ["ES", "NW"],
    "S": ["NESW", "NESW"],
    ".": ["", ""],
}

DIRECTION_TO_IDX = {
    "N": [0, -1],
    "E": [1, 0],
    "S": [0, 1],
    "W": [-1, 0],
}

def check_pos(MAPJE, pos: Tuple[int, int], last = None):
    x, y = pos
    backwards_dir = ["NS", "EW"]
    symbol = MAPJE[y][x]
    for dir in SYMBOL_TO_CONNECTIONS[symbol][0]:
        if dir != last:
            move_x, move_y = DIRECTION_TO_IDX[dir]
            if 0 <= (x + move_x) < (len(MAPJE[0])) or 0 <= (y + move_y) < (len(MAPJE)):
                if dir in SYMBOL_TO_CONNECTIONS[MAPJE[y + move_y][x + move_x]][1]:
                    last = backwards_dir[int(dir not in backwards_dir[0])].replace(dir, "")
                    return ((x + move_x), (y + move_y)), last
                
def check_inside_polygon(grouped_range, map_cleaned):
    # Uses the range of the loop pipe for each line to quickly find all pieces that are stuck inside the loop
    pattern = r'L-*7|\||F-*J'  # Regex pattern for finding a pipe that goes across
    total_inside = 0
    trapped_list = []  # Simply for creating a visual and is not required for logic
    for idx, line in enumerate(map_cleaned):
        prev_good = False  # prev_good and prev_ground allow you to avoid checking a . symbol if the previous was confirmed good
        prev_ground = False
        for i in range(*grouped_range[idx]):
            if line[i] == '.':
                if not prev_good:
                    if prev_ground:  # If the previous was a ground that was confirmed stuck, just add another stuck
                        total_inside += 1
                        trapped_list.append((i, idx))
                    else:  # Use the even-odd rule to determine if the point is within the loop
                        cross_lines = re.findall(pattern, ''.join(line[grouped_range[idx][0]:(i + 1)]))
                        if len(cross_lines) % 2 == 1:  # If there were an odd number of cross pipes, the point is within the loop
                            trapped_list.append((i, idx))
                            total_inside += 1
                            prev_good = False
                        else:  # If there was an even number of cross pipes, the point is outside of the loop
                            prev_good = True
                prev_ground = True
            else:  # Reset the switches whenever a pipe is hit
                prev_ground = False
                prev_good = False
    
    return total_inside, trapped_list

input = input.split("\n")
start = [(re.search('S', line).start(), idx) for idx, line in enumerate(input) if re.search('S', line)][0]
point_list = [start]
next_point, last = check_pos(input, start)  # Find the first pipe connected to S before the while loop
while next_point != start:  # Break when you get back to the start point
    point_list.append(next_point)
    next_point, last = check_pos(input, next_point, last)
print(len(point_list) // 2)