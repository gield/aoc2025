with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

dial = 50
counter = 0
for rotation in lines:
    direction = rotation[0]
    distance = int(rotation[1:])
    full_rotations, distance = divmod(distance, 100)
    counter += full_rotations
    if direction == "R":
        if dial != 0 and dial + distance >= 100:
            counter += 1
        dial = (dial + distance) % 100
    else:
        if dial != 0 and dial - distance <= 0:
            counter += 1
        dial = (dial - distance) % 100
print(counter)
