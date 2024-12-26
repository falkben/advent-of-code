import itertools
from collections import defaultdict

input = """\
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""


# input = open("2024/day08/data.txt").read()

ants = defaultdict(list)
roof = {}

rows = len(input.splitlines())
cols = len(input.splitlines()[0])

for y, row in enumerate(input.splitlines()):
    for x, pos in enumerate(row):
        roof[(y, x)] = pos
        if pos != ".":
            ants[pos].append((y, x))


# for y, row in enumerate(input.splitlines()):
#     for x, pos in enumerate(row):
#         print(roof[(y, x)], end="")
#     print()


nn = set()
for ant, positions in ants.items():
    pairs = list(itertools.combinations(positions, r=2))
    for p1, p2 in pairs:
        y1, x1 = p1
        y2, x2 = p2

        # y = mx + b
        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1

        for y, row in enumerate(input.splitlines()):
            xfloat = (y - b) / m
            x = round(xfloat)
            if abs(x - xfloat) < 0.01:
                nn.add((y, x))

        for x, pos in enumerate(row):
            yfloat = m * x + b
            y = round(yfloat)
            if abs(y - yfloat) < 0.01:
                nn.add((y, x))

    # if slope < 0:
    #     p1 = (y1 - abs(y1 - y2), x1 + abs(x1 - x2))
    #     p2 = (y2 + abs(y2 - y1), x2 - abs(x2 - x1))
    # else:
    #     p1 = (y1 - abs(y1 - y2), x1 - abs(x1 - x2))
    #     p2 = (y2 + abs(y2 - y1), x2 + abs(x2 - x1))

    # nn.add(p1)
    # nn.add(p2)


an = 0
for y, row in enumerate(input.splitlines()):
    for x, pos in enumerate(row):
        if (y, x) in nn:
            print("#", end="")
            an += 1
        else:
            print(roof[(y, x)], end="")
    print()

print(an)
