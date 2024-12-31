input = """\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

# input = open("2024/day10/data.txt").read()

rows = len(input.splitlines())
cols = len(input.splitlines()[0])

data = {}
starts = []
ends = []
for y, row in enumerate(input.splitlines()):
    for x, pos in enumerate(row):
        data[(y, x)] = int(pos)
        if pos == "0":
            starts.append((y, x))
        if pos == "9":
            ends.append((y, x))


def find_trails(y, x, prev_val, trail):
    global trails

    if not (0 <= y < rows and 0 <= x < cols):
        return

    val = data[(y, x)]
    trail.add((y, x))

    if val != prev_val + 1:
        return

    if val == 9:
        trails += 1
        return

    find_trails(y, x + 1, val, trail)
    find_trails(y + 1, x, val, trail)
    find_trails(y, x - 1, val, trail)
    find_trails(y - 1, x, val, trail)


score = 0
for y, x in starts:
    trails = 0
    find_trails(y, x, -1, set())
    score += trails

print(score)
