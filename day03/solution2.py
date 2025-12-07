with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

s = 0
for l in lines:
    bank = list(map(int, l))
    selected_batteries = []
    min_i = 0
    for b in range(1, 12 + 1):
        max_i = len(bank) - 12 + b
        window = bank[min_i:max_i]
        best = max(window)
        best_i = window.index(best)
        selected_batteries.append(best)
        min_i += window.index(best) + 1
    s += int("".join(map(str, selected_batteries)))
print(s)
