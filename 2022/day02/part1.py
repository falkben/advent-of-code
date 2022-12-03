guide = """\
A Y
B X
C Z
"""
guide = open("2022/day02/data.txt").read()

scores = [8, 1, 6]
expected = sum(scores)

# rock=A/X, paper=B/Y, scissors=C/Z

#         A/X B/Y C/Z
#         0,  1,  2
# wins:   1,  2,  0
# losses: 2,  0,  1

results = []
for line in guide.splitlines():
    # identify shape
    # X,Y,Z = 1,2,3
    # outcome
    # L=0, D=3, W=6
    opp = line[0]
    my = line[2]

    opp_id = ord(opp) - ord("A")
    my_id = ord(my) - ord("X")

    diff = my_id - opp_id
    if diff == 1 or diff == -2:
        # win
        result = (my_id + 1) + 6
    elif diff == 2 or diff == -1:
        # loss
        result = my_id + 1 + 0
    else:
        # draw
        result = my_id + 1 + 3
    results.append(result)

print(sum(results))
