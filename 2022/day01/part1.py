data = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""
data = open("2022/day01/data.txt").read()

data_split = data.splitlines()
elves = []
c = 0
for d in data_split:
    if d == "":
        elves.append(c)
        c = 0
    else:
        c += int(d)
elves.append(c)

# part1
print(max(elves))

# part2
mm = [max(elves)]
elves.pop(elves.index(max(elves)))
mm.append(max(elves))
elves.pop(elves.index(max(elves)))
mm.append(max(elves))
print(sum(mm))
