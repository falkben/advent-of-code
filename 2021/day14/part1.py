from collections import Counter

input = """\
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""

# with open("2021/day14/data.txt") as fh:
#     input = fh.read()

template, rules_s = input.split("\n\n")

rules = {}
for line in rules_s.splitlines():
    rule_pair, insert_char = line.split(" -> ")
    rules[rule_pair] = insert_char

for step in range(10):
    insertions = []

    # go through the template
    for i in range(len(template)):
        char_pair = template[i : i + 2]
        if char_pair in rules:
            # evaluate rule against template
            # store insertions to make
            insertions.append((i + 1, rules[char_pair]))
    # apply insertions
    insertions_applied = 0
    for i, char in insertions:
        template = (
            template[: i + insertions_applied]
            + char
            + template[i + insertions_applied :]
        )
        insertions_applied += 1

    # print(template)

c = Counter(template)
print(c.most_common()[0][1] - c.most_common()[-1][1])

# print(template)
# print(rules)

return_value = c.most_common()[0][1] - c.most_common()[-1][1]
