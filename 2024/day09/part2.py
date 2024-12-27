from collections import deque

input = """\
2333133121414131402
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
i = -1
while True:
    try:
        first_open_idx = disk.index(".", 0, i)
    except ValueError:
        # "." not found
        break

    start_i = i
    f_id = disk[i]
    while disk[i - 1] == f_id:
        i -= 1

    block_size = abs(i - start_i - 1)

    empty_ct = 1
    while empty_ct < block_size:
        if disk[first_open_idx + empty_ct] == ".":
            empty_ct += 1
        else:
            try:
                first_open_idx = disk.index(".", first_open_idx + 1, i)
            except ValueError:
                first_open_idx = None
                break
            empty_ct = 1

    if first_open_idx is not None:
        for ii in range(first_open_idx, first_open_idx + block_size):
            disk[ii] = f_id

        for ii in range(i, start_i + 1):
            disk[ii] = "."

    i -= 1
    while disk[i] == "." or i == 0:
        i -= 1

    # print("".join(map(str, disk)))


# 00992111777.44.333....5555.6666.....8888..
# print("".join(map(str, disk)))

total = 0
for i, ch in enumerate(disk):
    if ch != ".":
        total += i * ch

print(total)
