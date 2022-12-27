import math
from dataclasses import dataclass

# input = """\
# R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2
# """
# input = """\
# R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20
# """
input = open("2022/day09/data.txt").read()

# head/tail start at same position
# iterate in steps
# tail follows head, never more than two spaces away
# R: right
# L: left
# U: up
# D: down
# diagonal spacing also counted

# part1: count all positions Tail visits


@dataclass(frozen=True)
class Point:
    x: int
    y: int


def check_too_far(p1: Point, p2: Point):
    if abs(p1.x - p2.x) > 1:
        return True
    if abs(p1.y - p2.y) > 1:
        return True
    return False


def modify_knots(x_mod, y_mod):
    # head always moves
    knots[0] = Point(knots[0].x + x_mod, knots[0].y + y_mod)

    for k in range(9):
        lead = knots[k]
        follower = knots[k + 1]
        if check_too_far(lead, follower):
            if lead.x == follower.x:
                # in the same column
                knots[k + 1] = Point(
                    follower.x, follower.y + int(math.copysign(1, lead.y - follower.y))
                )
            elif lead.y == follower.y:
                # in the same row
                knots[k + 1] = Point(
                    follower.x + int(math.copysign(1, lead.x - follower.x)), follower.y
                )
            else:
                # diag., move one step diagonally to catch up
                knots[k + 1] = Point(
                    follower.x + int(math.copysign(1, lead.x - follower.x)),
                    follower.y + int(math.copysign(1, lead.y - follower.y)),
                )


# 0: head, -1: tail
knots = [Point(0, 0)] * 10

tail_positions = {knots[-1]}
for line in input.splitlines():
    dir = line[0]
    count = int(line[2:])

    for iter in range(count):

        # move head
        match dir:
            case "R":
                # knots[0] = Point(knots[0].x + 1, knots[0].y)
                modify_knots(1, 0)
                # for k, lead in enumerate(knots[:-2]):
                #     if check_too_far(lead, knots[k + 1]):
                #         tail = Point(knots[k + 1].x + 1, lead.y)
            case "L":
                # knots[0] = Point(knots[0].x - 1, knots[0].y)
                modify_knots(-1, 0)
                # if check_too_far(head, tail):
                #     tail = Point(tail.x - 1, head.y)
            case "U":
                # knots[0] = Point(knots[0].x, knots[0].y + 1)
                modify_knots(0, 1)
                # if check_too_far(head, tail):
                #     tail = Point(head.x, tail.y + 1)
            case "D":
                # knots[0] = Point(knots[0].x, knots[0].y - 1)
                modify_knots(0, -1)
                # if check_too_far(head, tail):
                #     tail = Point(head.x, tail.y - 1)
        tail_positions.add(knots[-1])

print(len(tail_positions))
