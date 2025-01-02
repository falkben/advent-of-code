from functools import cache

input = """\
125 17
"""

# input = open("2024/day11/data.txt").read()

BLINK_LIM = 75


@cache
def blink_num(value, iter):
    if iter >= BLINK_LIM:
        return 1

    iter += 1

    # if 0 -> 1
    if value == 0:
        return blink_num(1, iter)

    # if even digits -> 2 stones, split in half
    elif (len_val := len(str(value))) % 2 == 0:
        new_val1 = int(str(value)[0 : len_val // 2])
        new_val2 = int(str(value)[len_val // 2 :])
        return blink_num(new_val1, iter) + blink_num(new_val2, iter)

    # else old number * 2024
    else:
        return blink_num(value * 2024, iter)


total = 0
values = list(map(int, input.strip().split()))
for value in values:
    total += blink_num(value, 0)

print(total)
