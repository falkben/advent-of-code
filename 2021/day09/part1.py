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

risk_lvl = 0
for i in range(hmap.shape[0]):
    for j in range(hmap.shape[1]):
        val = hmap[i, j]

        if (
            (i == rowlen - 1 or val < hmap[i + 1, j])
            and (i == 0 or val < hmap[i - 1, j])
            and (j == 0 or val < hmap[i, j - 1])
            and (j == linelen - 1 or val < hmap[i, j + 1])
        ):
            risk_lvl += hmap[i, j] + 1
            print(hmap[i, j])

print(risk_lvl)
