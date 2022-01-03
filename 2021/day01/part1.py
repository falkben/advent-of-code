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

diff_data = [d2 - d1 for d1, d2 in zip(data[:-1], data[1:])]

count_increment = sum(1 for d_d in diff_data if d_d > 0)

print(count_increment)

return_value = count_increment
