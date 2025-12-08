with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

empty_line_i = lines.index("")
ranges = {tuple(map(int, l.split("-"))) for l in lines[:empty_line_i]}

total = 0
pointer = -1
for a, b in sorted(ranges):
    if a > pointer:  # new range
        total += b - a + 1  # add full
    elif b > pointer:  # in already seen range
        total += b - pointer  # only add new numbers
    pointer = max(pointer, b)
print(total)
