with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

dial = 50
counter = 0
for rotation in lines:
    direction = rotation[0]
    distance = int(rotation[1:])
    if direction == "R":
        dial = (dial + distance) % 100
    else:
        dial = (dial - distance) % 100
    if dial == 0:
        counter += 1
print(counter)
