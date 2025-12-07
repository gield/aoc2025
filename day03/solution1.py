with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

s = 0
for l in lines:
    bank = list(map(int, l))
    left, right = -1, -1
    for battery in reversed(bank):
        if battery >= left:
            right = left
            left = battery
    s += left * 10 + right
print(s)
