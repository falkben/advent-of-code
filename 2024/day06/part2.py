from collections import defaultdict

input = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

input = open("2024/day06/data.txt").read()

lab = defaultdict(lambda: "")
for y, row in enumerate(input.splitlines()):
    for x, pos in enumerate(row):
        lab[y, x] = pos
        if pos == "^":
            startyx = (y, x)

total = 0
for yy in range(len(input.splitlines())):
    for xx in range(len(row)):
        if lab[(yy, xx)] == "#":
            continue

        seen = set()
        y, x = startyx
        d = 0
        while True:
            if (y, x, d) in seen:
                total += 1
                break

            seen.add((y, x, d))

            dy, dx = [(-1, 0), (0, 1), (1, 0), (0, -1)][d]
            nexty = y + dy
            nextx = x + dx

            if lab[nexty, nextx] == "":
                break
            if lab[nexty, nextx] == "#" or nexty == yy and nextx == xx:
                d = (d + 1) % 4
            else:
                y = nexty
                x = nextx


print(total)


# for y, row in enumerate(input.splitlines()):
#     for x, pos in enumerate(row):
#         print(lab[y, x], end="")
#     print()
