from collections import deque

input = """\
125 17
"""

# input = open("2024/day11/data.txt").read()

values = deque(map(int, input.strip().split()))
for _ in range(25):
    i = 0
    while i < len(values):
        value = values[i]

        # if 0 -> 1
        if value == 0:
            values[i] = 1

        # if even digits -> 2 stones, split in half
        elif (len_val := len(str(value))) % 2 == 0:
            new_val1 = int(str(value)[0 : len_val // 2])
            new_val2 = int(str(value)[len_val // 2 :])
            values[i] = new_val1
            values.insert(i + 1, new_val2)
            i += 1

        # else old number * 2024
        else:
            value *= 2024
            values[i] = value
        i += 1

total = len(values)
print(total)
