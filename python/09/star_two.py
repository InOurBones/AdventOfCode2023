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
    
    history[-1] = [0] + history[-1]

    history = list(reversed(history))
    for idx, hist in enumerate(history[1:], 1):
        getal = hist[0] - history[idx - 1][0]
        history[idx] = [hist[0] - history[idx - 1][0]] + hist
    
    total += history[-1][0]
print(total)
