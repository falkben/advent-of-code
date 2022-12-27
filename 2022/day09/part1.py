from dataclasses import dataclass

input = """\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""
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


head = Point(0, 0)
tail = Point(0, 0)
tail_positions = {tail}
for line in input.splitlines():
    dir = line[0]
    count = int(line[2:])

    for iter in range(count):

        # move head
        match dir:
            case "R":
                head = Point(head.x + 1, head.y)
                if check_too_far(head, tail):
                    tail = Point(tail.x + 1, head.y)
            case "L":
                head = Point(head.x - 1, head.y)
                if check_too_far(head, tail):
                    tail = Point(tail.x - 1, head.y)
            case "U":
                head = Point(head.x, head.y + 1)
                if check_too_far(head, tail):
                    tail = Point(head.x, tail.y + 1)
            case "D":
                head = Point(head.x, head.y - 1)
                if check_too_far(head, tail):
                    tail = Point(head.x, tail.y - 1)
        tail_positions.add(tail)

print(len(tail_positions))
