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

safe = 0
for line in data.splitlines():
    line_data = [int(x) for x in line.split(" ")]
    line_diff = [x - y for x, y in zip(line_data[:-1], line_data[1:])]

    if max(line_diff) > 3:
        continue
    if min(line_diff) < -3:
        continue
    if all(d > 0 for d in line_diff) or all(d < 0 for d in line_diff):
        safe += 1

return_value = safe
print(return_value)
