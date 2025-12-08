with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

empty_line_i = lines.index("")
ranges = {tuple(map(int, l.split("-"))) for l in lines[:empty_line_i]}
ingredients = list(map(int, lines[empty_line_i + 1 :]))

num_fresh_ingredients = 0
for ingredient in ingredients:
    if any(a <= ingredient <= b for a, b in ranges):
        num_fresh_ingredients += 1
print(num_fresh_ingredients)
