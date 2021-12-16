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

with open("2021/day14/data.txt") as fh:
    input = fh.read()

template_s, rules_s = input.split("\n\n")

# convert template to a count of pairs
# note, we'll have to divide our counts of each char. by 2 later
pair_count = Counter()
for i in range(len(template_s) - 1):
    pair_count.update([template_s[i : i + 2]])

rules = {}
for line in rules_s.splitlines():
    rule_pair, insert_char = line.split(" -> ")
    rules[rule_pair] = insert_char

for step in range(40):

    # identify the insertions to do on the pair data before modifications
    # create a new counter only of insertions
    insert_c = Counter()
    for rule_pair, insert_char in rules.items():
        insert_amount = pair_count[rule_pair]
        if insert_amount > 0:
            insert_c.update({rule_pair: -insert_amount})
            insert_c.update({rule_pair[0] + insert_char: insert_amount})
            insert_c.update({insert_char + rule_pair[1]: insert_amount})

    # apply insertions simultaneously
    pair_count = pair_count + insert_c

c = Counter()
for (char1, char2), count in pair_count.items():
    c.update({char1: count})
    c.update({char2: count})

# dealing with leading and trailing character not being part of 2 pairs like ever other
c[template_s[0]] += 1
c[template_s[-1]] += 1

# divide our char. counts by 2 because we count each char twice
print(int(c.most_common()[0][1] / 2 - c.most_common()[-1][1] / 2))
