from collections import defaultdict

input = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

# input = open("2024/day04/data.txt").read()


cols = "\n".join("".join(chars) for chars in zip(*input.splitlines()))

rows = len(input.splitlines())
cols = len(cols.splitlines())

data = "".join(input.splitlines())
mat = defaultdict(lambda: "")
n = 0
for y in range(rows):
    for x in range(cols):
        mat[x, y] = data[y * cols + x]
        n += 1

total = 0
for y in range(rows):
    for x in range(cols):
        s1 = mat[x - 1, y - 1] + mat[x, y] + mat[x + 1, y + 1]
        s2 = mat[x - 1, y + 1] + mat[x, y] + mat[x + 1, y - 1]
        if s1 in ("SAM", "MAS") and s2 in ("SAM", "MAS"):
            total += 1

print(total)
