import string

data = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

# data = open("2022/day03/data.txt").read()

priorities = []
lines = data.split()
# data grouped into lines of 3
for group in [lines[i : i + 3] for i in range(0, len(lines), 3)]:

    dupl_char = set.intersection(*[set(l) for l in group]).pop()

    if dupl_char in string.ascii_lowercase:
        priorities.append(ord(dupl_char) - ord("a") + 1)
    else:
        priorities.append(ord(dupl_char) - ord("A") + 1 + 26)


print(sum(priorities))
