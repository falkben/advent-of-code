with open("2021/day01/data.txt") as input_fh:
    data = input_fh.read().splitlines()

data = [int(item) for item in data]

diff_data = [d2 - d1 for d1, d2 in zip(data[:-1], data[1:])]

count_increment = sum(1 for d_d in diff_data if d_d > 0)

print(count_increment)

return_value = count_increment
