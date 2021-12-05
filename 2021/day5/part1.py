from collections import defaultdict

input = """\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

with open("2021/day5/data.txt") as fh:
    input = fh.read()

counter = defaultdict(int)

for line in input.splitlines():
    p1, p2 = line.split(" -> ")
    x1, y1 = map(int, p1.split(","))
    x2, y2 = map(int, p2.split(","))

    if x1 == x2:
        # vertical
        for yy in range(min(y1, y2), max(y1, y2) + 1):
            counter[(x1, yy)] += 1
    elif y1 == y2:
        # horizontal
        for xx in range(min(x1, x2), max(x1, x2) + 1):
            counter[(xx, y1)] += 1

intersect_pts = 0
for item in counter.values():
    if item >= 2:
        intersect_pts += 1

print(intersect_pts)
