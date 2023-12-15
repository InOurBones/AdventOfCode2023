import os

input_file = os.path.join(os.path.dirname(__file__), "../../input/day_15.txt")

with open(input_file, "r") as file:
    input = file.read()

boxes = [[] for _ in range(256)]
for x in input.split(","):
    if "=" in x:
        chars = x[:-2]
        sign = "="
        idx = int(x[-1])
    else:
        chars = x[:-1]
        sign = "-"

    hash_value = 0
    for char in chars:
        hash_value = ((ord(char) + hash_value) * 17) % 256

    lens_idx = next((i for i, x in enumerate(boxes[hash_value]) if x[0] == chars), None)
    if sign == "=" and lens_idx is None:
        boxes[hash_value].append((chars, idx))
    elif sign == "=":
        boxes[hash_value][lens_idx] = (chars, idx)
    elif lens_idx is not None:
        boxes[hash_value].pop(lens_idx)

total = sum([sum(box_idx * lens_idx * lens[1] for lens_idx, lens in enumerate(box, 1)) for box_idx, box in enumerate(boxes, 1)])
print(total)