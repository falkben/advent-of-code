from io import StringIO

import numpy as np

# from numpy import typing as npt

input = """\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

with open("2021/day3/data.txt") as fh:
    input = fh.read()


c = StringIO(input)
arr = np.genfromtxt(c, dtype=int, delimiter=np.ones(12, int))


def conv_arr_dec(arr):
    dec = 0
    for i, v in enumerate(reversed(arr)):
        dec += v * 2 ** i
    return dec


oxy_rows = arr
for col in range(arr.shape[1]):
    col_avg = int(np.mean(oxy_rows[:, col]) + 0.5)
    oxy_rows = oxy_rows[oxy_rows[:, col] == col_avg, :]

    if oxy_rows.shape[0] == 1:
        break

oxy_rating = conv_arr_dec(oxy_rows.flatten())

co2_rows = arr
for col in range(arr.shape[1]):
    col_avg = abs(1 - int(np.mean(co2_rows[:, col]) + 0.5))
    co2_rows = co2_rows[co2_rows[:, col] == col_avg, :]

    if co2_rows.shape[0] == 1:
        break

co2_rating = conv_arr_dec(co2_rows.flatten())


print("life support:", oxy_rating * co2_rating)
