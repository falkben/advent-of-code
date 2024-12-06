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


def find_xmax(data):
    count = 0
    for line in data.splitlines():
        for i in range(len(line)):
            substr = line[i : min(i + 4, len(line))]
            count += substr in ("XMAS", "SAMX")
    return count


total = 0
total += find_xmax(input)

cols = "\n".join("".join(chars) for chars in zip(*input.splitlines()))
total += find_xmax(cols)


rows = len(input.splitlines())
cols = len(cols.splitlines())

data = "".join(input.splitlines())
mat = {}
n = 0
for y in range(rows):
    for x in range(cols):
        mat[x, y] = data[y * cols + x]
        n += 1


# creating diag
diagxy = ""

# 9,0;\n
# 8,0;9,1\n
# 7,0;8,1;9,2\n
# ...
# 0,0;1,1;2,2...9,9\n
# ...
# 0,9;\n

for x in range(cols, 0, -1):
    for xy in range(rows - x):
        # print(x + xy, xy)
        diagxy += mat[x + xy, xy]
    diagxy += "\n"
    # print()

for y in range(rows):
    for xy in range(rows - y):
        # print(xy, xy + y)
        diagxy += mat[xy, xy + y]
    diagxy += "\n"
    # print()


total += find_xmax(diagxy)

# 0,0;\n
# 0,1;1,0\n
# 0,2;1,1;2,0\n
# ...
# 0,9;1,8;2,7...9,0\n
# 1,9;2,8;3,7...9,1\n
# ...
# 9,9;\n

diagrev = ""
for x in range(cols):
    for y in range(x, -1, -1):
        diagrev += mat[abs(x - y), y]
        # print(abs(x - y), y)
    # print()
    diagrev += "\n"


for x in range(1, cols):
    for i, y in enumerate(range(rows - 1, x - 1, -1)):
        # print(x + i, y)
        diagrev += mat[x + i, y]
    diagrev += "\n"
    # print()

total += find_xmax(diagrev)
print(total)

# return_data = ...
# print(return_data)
