input = """\
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


# with open("2021/day13/data.txt") as fh:
#     input = fh.read()

dot_input, fold_input = input.split("\n\n")
pair_data = set()
for line in dot_input.splitlines():
    x, y = line.split(",")
    pair_data.add((int(x), int(y)))
# print(pair_data)

folds = []
for fold_line in fold_input.splitlines():
    _, fold_val_str = fold_line.split("fold along ")
    axis, fold_val = fold_val_str.split("=")
    folds.append((0 if axis == "x" else 1, int(fold_val)))
# print(folds)

# part1 only the first fold
for axis, fold_val in folds:
    folded_pair_data = pair_data.copy()
    for pair in pair_data:
        point_val = pair[axis]
        if point_val > fold_val:
            folded_pair = list(pair)
            folded_pair[axis] = 2 * fold_val - folded_pair[axis]
            folded_pair_data.remove(pair)
            folded_pair_data.add(tuple(folded_pair))
    pair_data = folded_pair_data


max_x = max([x for x, _ in pair_data])
max_y = max([y for _, y in pair_data])


for yy in range(max_y + 1):
    for xx in range(max_x + 1):
        if (xx, yy) in pair_data:
            print("#", end="")
        else:
            print(".", end="")
    print()


"""
0   0
1   1
2   2
3   3
4----
5   3   4 - (5-4) = n + -v +n = 2n-v
6   2   4 - (6-4)
7   1   4 - (7-4)
8   0   4 - (8-4)
"""
