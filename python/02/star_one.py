import os

INVENTORY = {
    "red": 12,
    "green": 13,
    "blue": 14
}

input_file = os.path.join(os.path.dirname(__file__), "../../input/day_02.txt")

def game_is_possible(input: str) -> bool:
    for s in input.replace(",", ";").split("; "):
        count_str, cube = s.split(" ")
        if int(count_str) > INVENTORY[cube]:
            return False
    return True

total = 0
with open(input_file, "r") as file:
    for x in file.readlines():
        x = x[:-1]  # remove \n
        game_str, input = x.split(": ")
        if game_is_possible(input):
            total += int(game_str[5:])  # remove 'Game '
print(total)