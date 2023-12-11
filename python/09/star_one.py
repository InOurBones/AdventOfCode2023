import os

input_file = os.path.join(os.path.dirname(__file__), "../../input/day_09.txt")

with open(input_file, "r") as file:
    input = file.read()

total = 0
for line in input.split("\n"):
    history = [[int(x) for x in line.split(" ")]]
    while not all(x == 0 for x in history[-1]):
        last_hist = history[-1]
        history.append([last_hist[idx] - last_hist[idx - 1] for idx in range(1, len(last_hist))])
    
    history[-1].append(0)
    history = list(reversed(history))
    for idx, hist in enumerate(history[1:], 1):
        hist.append(history[idx - 1][-1] + hist[-1])
    
    total += history[-1][-1]
print(total)
