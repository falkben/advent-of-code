from collections import deque

input = """\
2333133121414131402\
"""

# input = open("2024/day09/data.txt").read()

disk = deque()
for i, ch in enumerate(input.strip()):
    if i % 2 == 0:
        disk.extend([i // 2] * int(ch))
    else:
        disk.extend("." * int(ch))

# 00...111...2...333.44.5555.6666.777.888899
# print("".join(map(str, disk)))

orig = disk.copy()
orig.reverse()
for i, ch in enumerate(orig):
    ind = disk.index(".")
    if len(disk) - i > ind:
        del disk[ind]
        disk.insert(ind, ch)
        disk[-i - 1] = "."
    else:
        break

# 0099811188827773336446555566..............
# print("".join(map(str, disk)))

total = 0
for i, ch in enumerate(disk):
    if ch != ".":
        total += i * ch
    else:
        break

print(total)
