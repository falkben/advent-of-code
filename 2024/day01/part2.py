data = """\
3   4
4   3
2   5
1   3
3   9
3   3
"""

# data = open("2024/day01/data.txt").read()


list1 = []
list2 = []
for line in data.splitlines():
    l1, l2 = line.split("   ")
    list1.append(int(l1))
    list2.append(int(l2))

list1.sort()
list2.sort()

sim_score = 0
for l1 in list1:
    sim_score += l1 * list2.count(l1)

print(sim_score)
