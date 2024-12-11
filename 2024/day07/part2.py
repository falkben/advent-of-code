import itertools
import random

input = """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

# input = open("2024/day07/data.txt").read()

total = 0
for line in input.splitlines():
    out, data = line.split(": ")
    vals = list(map(int, data.split(" ")))
    out = int(out)

    # add, multiply
    operator_places = len(vals) - 1
    operators = ("a", "m", "|")
    combs = list(itertools.product(operators, repeat=operator_places))
    # print(combs)

    for comb in combs:
        tt = vals[0]
        for i, cc in enumerate(comb):
            if cc == "a":
                tt += vals[i + 1]
            elif cc == "|":
                tt = int(str(tt) + str(vals[i + 1]))
            else:
                tt *= vals[i + 1]
        if tt == out:
            total += out
            break

print(total)
