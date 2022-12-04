import string

data = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

data = open("2022/day03/data.txt").read()

priorities = []
for line in data.split():
    first = line[: len(line) // 2]
    second = line[len(line) // 2 :]

    dupl_char = (set(first) & set(second)).pop()
    if dupl_char in string.ascii_lowercase:
        priorities.append(ord(dupl_char) - ord("a") + 1)
    else:
        priorities.append(ord(dupl_char) - ord("A") + 1 + 26)

print(sum(priorities))
