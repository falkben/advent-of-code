from io import StringIO

import numpy as np

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

# with open("2021/day03/data.txt") as fh:
#     input = fh.read()


c = StringIO(input)
arr = np.genfromtxt(c, dtype=int, delimiter=np.ones(12, int))

arr_avg = np.mean(arr, axis=0)

gamma_bin = np.round(arr_avg).astype(int)
epsilon_bin = np.abs(1 - gamma_bin)


def conv_arr_dec(arr):
    dec = 0
    for i, v in enumerate(reversed(arr)):
        dec += v * 2 ** i
    return dec


print("power consumption:", conv_arr_dec(gamma_bin) * conv_arr_dec(epsilon_bin))

return_value = conv_arr_dec(gamma_bin) * conv_arr_dec(epsilon_bin)
