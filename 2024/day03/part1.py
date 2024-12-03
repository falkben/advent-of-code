import re

input = """\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""

# input = open("2024/day03/data.txt").read()

return_data = 0
m = re.findall(r"mul\(\d+,\d+\)", input)
for mm in m:
    parts = mm.split(",")
    num1 = int(parts[0][4:])
    num2 = int(parts[1][:-1])
    return_data += num1 * num2

print(return_data)
