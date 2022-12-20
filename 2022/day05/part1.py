import re
import string

# fmt: off
input = """\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
# fmt: on

input = open("2022/day05/data.txt").read()

stacks, steps = input.split("\n\n")

# parse stacks
lines = stacks.splitlines()
num_chars = len(lines[0])

data = {}
for y, line in enumerate(lines[::-1]):
    for x, char in enumerate(line):
        data[(x, y)] = char

stack_lists = {}
for x in range(num_chars):
    cur_stack = ""
    for y in range(len(lines)):
        ch = data[(x, y)]
        if ch in " []":
            continue
        if ch in string.digits:
            stack_lists[ch] = []
            cur_stack = ch
        else:
            stack_lists[cur_stack].append(ch)

print(stack_lists)

# steps

for line in steps.splitlines():
    # move 1 from 2 to 1
    match = re.match(r"^move (\d+) from (\d) to (\d)$", line)
    amount, start, end = (int(match.group(1)), match.group(2), match.group(3))

    for n in range(amount):
        stack_lists[end].append(stack_lists[start].pop())

for stack in stack_lists.values():
    print(stack.pop(), end="")
print()
