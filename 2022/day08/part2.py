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


def scenic_score(x: int, y: int):
    height = data[(x, y)]

    # check values left
    hl = 0
    for i in range(x - 1, -1, -1):
        hl += 1
        if height <= data[i, y]:
            break

    # check values right
    hr = 0
    for i in range(x + 1, len_trees):
        hr += 1
        if height <= data[i, y]:
            break
    # check values top
    ht = 0
    for i in range(y - 1, -1, -1):
        ht += 1
        if height <= data[x, i]:
            break

    # check values bottom
    hb = 0
    for i in range(y + 1, len(input.splitlines())):
        hb += 1
        if height <= data[x, i]:
            break

    return hl * hr * ht * hb


data = {}
len_trees = len(input.splitlines()[0])
for y, line in enumerate(input.splitlines()):
    for x, char in enumerate(line):
        data[(x, y)] = int(char)

tree_scores = []
for tree in data:
    tree_scores.append(scenic_score(*tree))

print(max(tree_scores))
