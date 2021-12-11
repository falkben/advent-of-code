import numpy as np

input = "16,1,2,0,4,2,7,1,2,14"

with open("2021/day7/data.txt") as fh:
    input = fh.read()

pos = np.fromstring(input, dtype=np.int16, sep=",")

# minimize the diff to a shared mid point


target = np.median(pos)
fuel = np.sum(np.abs(pos - target))

print(fuel)
