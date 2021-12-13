from collections import defaultdict

from rich import print

input = """\
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""

# input = """\
# 11111
# 19991
# 19191
# 19991
# 11111"""


input = """\
8826876714
3127787238
8182852861
4655371483
3864551365
1878253581
8317422437
1517254266
2621124761
3473331514"""


def get_adjacent(data, i, j):

    yield (i - 1, j), data[(i - 1, j)]
    yield (i + 1, j), data[(i + 1, j)]
    yield (i, j - 1), data[(i, j - 1)]
    yield (i, j + 1), data[(i, j + 1)]
    yield (i + 1, j + 1), data[(i + 1, j + 1)]
    yield (i - 1, j - 1), data[(i - 1, j - 1)]
    yield (i + 1, j - 1), data[(i + 1, j - 1)]
    yield (i - 1, j + 1), data[(i - 1, j + 1)]


def print_data(data):
    cols = {0: "white"}
    for i in range(num_lines):
        line_str = []
        for j in range(num_cols):
            line_str.append(data[(i, j)])
        print(
            "".join(
                [
                    f"[{cols.get(char, 'grey37')}]{char}[/{cols.get(char, 'grey37')}]"
                    for char in line_str
                ]
            )
        )
    print()


num_lines = len(input.splitlines())
num_cols = len(input.splitlines()[0])

data = defaultdict(lambda: -1)
for i, line in enumerate(input.splitlines()):
    for j, val in enumerate(line):
        data[(i, j)] = int(val)

# print("Before any steps:")
# print_data(data)

flashes = 0
for step in range(1000):

    for i in range(num_lines):
        for j in range(num_cols):
            data[(i, j)] += 1

    for i in range(num_lines):
        for j in range(num_cols):
            val = data[(i, j)]

            stack = []
            # any val > 9 flashes:
            # values adjacent (incl. diag.) flash if > 9
            # values can only flash once per step
            if val > 9:

                stack.append((i, j))
                while len(stack) > 0:

                    # pop item off stack
                    ii, jj = stack.pop()

                    # skip if we already hit this
                    if data[(ii, jj)] == -1:
                        continue

                    flashes += 1

                    # set value to signal (-1)
                    data[(ii, jj)] = -1

                    # check adjacent values of stack item
                    for (i_adj, j_adj), adj_val in get_adjacent(data, ii, jj):
                        if adj_val == -1:
                            continue

                        data[(i_adj, j_adj)] += 1
                        if data[(i_adj, j_adj)] > 9:
                            stack.append((i_adj, j_adj))

    # finally, any that flash have energy set to 0
    for i in range(num_lines):
        for j in range(num_cols):
            if data[(i, j)] == -1:
                data[(i, j)] = 0

    items = []
    for i in range(num_lines):
        for j in range(num_cols):
            items.append(data[(i, j)])
    if all(i == 0 for i in items):
        break

    # printing
    # print(f"After step {step+1}:")
    # print_data(data)

print(step + 1)
