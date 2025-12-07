with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

num_rows, num_cols = len(lines), len(lines[0])
rolls = {(r, c) for r in range(num_rows) for c in range(num_cols) if lines[r][c] == "@"}

num_inaccessible_rolls = 0
for r, c in rolls:
    if sum((r + dr, c + dc) in rolls for dr, dc in DIRECTIONS) < 4:
        num_inaccessible_rolls += 1
print(num_inaccessible_rolls)
