input = """\
30373
25512
65332
33549
35390
"""
# input = open("2022/day08/data.txt").read()


def is_visible(x: int, y: int):
    height = data[(x, y)]

    # check values left
    for i in range(x - 1, -1, -1):
        if height <= data[i, y]:
            break
    else:
        return True
    # check values right
    for i in range(x + 1, len_trees):
        if height <= data[i, y]:
            break
    else:
        return True
    # check values top
    for i in range(y - 1, -1, -1):
        if height <= data[x, i]:
            break
    else:
        return True
    # check values bottom
    for i in range(y + 1, len(input.splitlines())):
        if height <= data[x, i]:
            break
    else:
        return True

    return False


data = {}
len_trees = len(input.splitlines()[0])
for y, line in enumerate(input.splitlines()):
    for x, char in enumerate(line):
        data[(x, y)] = int(char)

vis_trees = 0
for tree in data:
    vis = is_visible(*tree)
    vis_trees += vis
    # print("x" if vis else ".", end="" if tree[0] != len_trees - 1 else "\n")

print(vis_trees)
