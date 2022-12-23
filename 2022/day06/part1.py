input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
input = "bvwbjplbgvbhsrlpgdmjqwftvncz"

input = open("2022/day06/data.txt").read()

for i in range(3, len(input)):
    if len(set(input[i - 4 : i])) == 4:
        print(i)
        break
