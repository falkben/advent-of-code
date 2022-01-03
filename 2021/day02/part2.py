input = """\
forward 5
down 5
forward 8
up 3
down 8
forward 2"""

# part 2

with open("2021/day02/data.txt") as inputfh:
    data = inputfh.read()
input = data

depth = 0
hor = 0
aim = 0

for l in input.splitlines():
    dir, amount = l.split(" ")
    amount = int(amount)
    if dir == "forward":
        hor += amount
        depth = depth + aim * amount
    elif dir == "down":
        # depth += amount
        aim += amount
    else:
        # depth -= amount
        aim -= amount

print(depth * hor)

return_value = depth * hor
