import numpy as np

input = """\
2199943210
3987894921
9856789892
8767896789
9899965678"""

with open("2021/day09/data.txt") as fh:
    input = fh.read()

linelen = len(input.splitlines()[0])
rowlen = len(input.splitlines())

hmap = np.genfromtxt(
    input.splitlines(), dtype=np.int8, delimiter=np.ones(linelen, dtype=np.int8)
)


def calc_basin_size(arr, i, j, size=0):
    """recursive function that in place modifies the array
    in order to prevent back searches
    """
    if arr[i, j] == 9:
        return 0

    size += 1
    arr[i, j] = 9

    if i != 0 and arr[i - 1, j] != 9:
        size = calc_basin_size(arr, i - 1, j, size)
    if i != rowlen - 1 and arr[i + 1, j] != 9:
        size = calc_basin_size(arr, i + 1, j, size)

    if j != 0 and arr[i, j - 1] != 9:
        size = calc_basin_size(arr, i, j - 1, size)
    if j != linelen - 1 and arr[i, j + 1] != 9:
        size = calc_basin_size(arr, i, j + 1, size)

    return size


low_pts = []
for i in range(hmap.shape[0]):
    for j in range(hmap.shape[1]):
        val = hmap[i, j]

        if (
            (i == rowlen - 1 or val < hmap[i + 1, j])
            and (i == 0 or val < hmap[i - 1, j])
            and (j == 0 or val < hmap[i, j - 1])
            and (j == linelen - 1 or val < hmap[i, j + 1])
        ):
            # we've found a low point
            low_pts.append((i, j))

basins = []
for i, j in low_pts:
    basins.append(calc_basin_size(hmap, i, j))

top_basins = sorted(basins, reverse=True)

print(np.prod(top_basins[0:3]))
