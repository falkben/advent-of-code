import numpy as np

input = "16,1,2,0,4,2,7,1,2,14"

# with open("2021/day7/data.txt") as fh:
#     input = fh.read()

pos = np.fromstring(input, dtype=np.int16, sep=",")

# cost for each move
# cost for a 3 move = 1 + 2 + 3 = n * (n + 1) / 2

# minimize the diff to a shared mid point

max_pos = pos.max()
min_pos = pos.min()

check_vals = np.zeros((pos.shape[0], max_pos), dtype=np.int16)

for i in range(max_pos):
    check_vals[:, i] = i

target = np.round(np.mean(pos))
fuel = np.sum(np.abs(pos - target) * (np.abs(pos - target) + 1) / 2)

print(fuel)
