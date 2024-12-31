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


def find_trails(y, x, prev_val):
    global visited_peaks

    if not (0 <= y < rows and 0 <= x < cols):
        return

    val = data[(y, x)]

    if val != prev_val + 1:
        return

    if val == 9:
        visited_peaks.add((y, x))
        return

    find_trails(y, x + 1, val)
    find_trails(y + 1, x, val)
    find_trails(y, x - 1, val)
    find_trails(y - 1, x, val)


score = 0
for y, x in starts:
    visited_peaks = set()
    find_trails(y, x, -1)
    score += len(visited_peaks)

print(score)
