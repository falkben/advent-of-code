import collections
from itertools import islice

input = """\
199
200
208
210
200
207
240
269
260
263"""

# with open("2021/day01/data.txt") as input_fh:
#     input = input_fh.read()

data = [int(item) for item in input.splitlines()]


def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


data_window = list(sliding_window(data, 3))
diff_data = [sum(d2) - sum(d1) for d1, d2 in zip(data_window[:-1], data_window[1:])]

count_increment = sum(1 for d_d in diff_data if d_d > 0)

print(count_increment)

return_value = count_increment
