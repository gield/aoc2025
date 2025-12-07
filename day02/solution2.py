with open("input.txt", "r") as f:
    line = f.read().strip()


def is_invalid(num: int) -> bool:
    s = str(num)
    mid = len(s) // 2
    return any(s[:l] * (len(s) // l) == s for l in range(1, mid + 1))


total_sum = 0
for r in line.split(","):
    start, end = map(int, r.split("-"))
    total_sum += sum(num for num in range(start, end + 1) if is_invalid(num))
print(total_sum)
