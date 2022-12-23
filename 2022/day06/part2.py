# input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
# input = "bvwbjplbgvbhsrlpgdmjqwftvncz"

input = open("2022/day06/data.txt").read()

for i in range(14, len(input)):
    if len(set(input[i - 14 : i])) == 14:
        print(i)
        break
