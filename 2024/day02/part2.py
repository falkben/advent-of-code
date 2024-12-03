data = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

# with open("2024/day02/data.txt") as f:
#     data = f.read()


def diff(data: list[int]) -> list[int]:
    return [x - y for x, y in zip(data[:-1], data[1:])]


def is_safe(data: list[int]) -> bool:
    line_diff = diff(data)

    if max(line_diff) > 3:
        return False
    if min(line_diff) < -3:
        return False
    if all(d > 0 for d in line_diff) or all(d < 0 for d in line_diff):
        return True
    return False


safe = []
for line in data.splitlines():
    data_rem = False
    line_data = [int(x) for x in line.split(" ")]

    if is_safe(line_data):
        safe.append(True)
        continue

    for n in range(len(line_data)):
        is_safe2 = is_safe(line_data[:n] + line_data[n + 1 :])
        if is_safe2:
            safe.append(True)
            break

    safe.append(False)


print(sum(safe))
