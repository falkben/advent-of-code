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

# input = open("2024/day06/data.txt").read()

lab = defaultdict(lambda: "")
for y, row in enumerate(input.splitlines()):
    for x, pos in enumerate(row):
        lab[y, x] = pos
        if pos == "^":
            yx = (y, x)

total = 0
cur_dir = lab[yx]
while lab[yx] != "":
    y, x = yx
    prev_dir = cur_dir

    if prev_dir == "^":
        next_xy = (y - 1, x)
    elif prev_dir == ">":
        next_xy = (y, x + 1)
    elif prev_dir == "v":
        next_xy = (y + 1, x)
    elif prev_dir == "<":
        next_xy = (y, x - 1)

    if lab[next_xy] == "#":
        if prev_dir == "^":
            cur_dir = ">"
            next_xy = (y, x + 1)
        elif prev_dir == ">":
            cur_dir = "v"
            next_xy = (y + 1, x)
        elif prev_dir == "v":
            cur_dir = "<"
            next_xy = (y, x - 1)
        elif prev_dir == "<":
            cur_dir = "^"
            next_xy = (y - 1, x)
    else:
        cur_dir = prev_dir

    if lab[yx] != "X":
        lab[yx] = "X"
        total += 1
    yx = next_xy

print(total)


for y, row in enumerate(input.splitlines()):
    for x, pos in enumerate(row):
        print(lab[y, x], end="")
    print()
