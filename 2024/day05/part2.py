from collections import defaultdict

input = """\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

input = open("2024/day05/data.txt").read()

page_order_rules_section, update_section = input.split("\n\n")


rules = defaultdict(set)
for page_order_rule in page_order_rules_section.splitlines():
    first, second = page_order_rule.split("|")
    rules[int(first)].add(int(second))

updates_to_order = []
for update in update_section.splitlines():
    pages = [int(page) for page in update.split(",")]
    after_pages = pages.copy()
    for i, page in enumerate(pages):
        after_pages.remove(page)
        bef_pages = set(pages[:i])

        if rules[page] & bef_pages:
            updates_to_order.append(pages)
            break


total = 0
for pages in updates_to_order:
    new_pages = pages.copy()
    for i, page in enumerate(pages):
        bef_pages = set(pages[:i])
        if page_rule_wrong := rules[page] & bef_pages:
            new_pages.pop(i)
            new_pages.insert(min(new_pages.index(gg) for gg in page_rule_wrong), page)
    # print(new_pages)
    total += new_pages[len(pages) // 2]
print(total)

# return_data = ...
# print(return_data)
