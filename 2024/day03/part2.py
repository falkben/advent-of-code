# input = open("2024/day03/data.txt").read()

# return_data = ...
# print(return_data)
import re

input = """\
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""

# input = open("2024/day03/data.txt").read()

return_data = 0
m = re.finditer(r"mul\(\d+,\d+\)", input)
for mm in m:
    start = mm.start()
    do_find = list(re.finditer(r"do\(\)", input[0:start]))
    dont_find = list(re.finditer(r"don't\(\)", input[0:start]))
    if (
        do_find
        and dont_find
        and do_find[-1].start() > dont_find[-1].start()
        or (not do_find and not dont_find)
    ):
        parts = mm.group().split(",")
        num1 = int(parts[0][4:])
        num2 = int(parts[1][:-1])
        return_data += num1 * num2

print(return_data)
