input = """\
forward 5
down 5
forward 8
up 3
down 8
forward 2"""

# part 1

# with open("2021/day2/data.txt") as inputfh:
#     input = inputfh.read()

depth = 0
hor = 0

for l in input.splitlines():
    dir, amount = l.split(" ")
    amount = int(amount)
    if dir == "forward":
        hor += amount
    elif dir == "down":
        depth += amount
    else:
        depth -= amount

print(depth * hor)

return_value = depth * hor
