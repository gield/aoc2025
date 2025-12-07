with open("input.txt", "r") as f:
    line = f.read().strip()


def is_invalid(num: int) -> bool:
    s = str(num)
    if len(s) % 2 != 0:
        return False
    mid = len(s) // 2
    return s[:mid] == s[mid:]


total_sum = 0
for r in line.split(","):
    start, end = map(int, r.split("-"))
    total_sum += sum(num for num in range(start, end + 1) if is_invalid(num))
print(total_sum)
