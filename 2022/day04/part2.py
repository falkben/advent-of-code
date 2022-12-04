data = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

# data = open("2022/day04/data.txt").read()

count_contained = 0
for line in data.split():
    first, second = line.split(",")

    first_start, first_end = [int(x) for x in first.split("-")]
    second_start, second_end = [int(x) for x in second.split("-")]

    first_set = set(range(first_start, first_end + 1))
    second_set = set(range(second_start, second_end + 1))

    if first_set & second_set:
        count_contained += 1

print(count_contained)
