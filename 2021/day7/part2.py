import numpy as np

# input = "16,1,2,0,4,2,7,1,2,14"

with open("2021/day7/data.txt") as fh:
    input = fh.read()

pos = np.fromstring(input, dtype=int, sep=",")

# cost for each move
# cost for a 3 move = 1 + 2 + 3 = n * (n + 1) / 2

# minimize the diff to a shared mid point

max_pos = pos.max()
min_pos = pos.min()

check_vals = np.dot(np.ones(pos.shape, dtype=int)[:, None], np.arange(min_pos, max_pos + 1, dtype=int)[None, :])
pos_vals = np.dot(pos[:, None], np.ones(check_vals.shape[1], dtype=int)[None, :])

cost = np.abs(pos_vals - check_vals) * (np.abs(pos_vals - check_vals) + 1) / 2
target = np.argmin(np.sum(cost, axis=0))

fuel = np.sum(np.abs(pos - target) * (np.abs(pos - target) + 1) / 2)

print(fuel)
