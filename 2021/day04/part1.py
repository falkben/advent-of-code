import numpy as np

input = """\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

# with open("2021/day04/data.txt") as fh:
#     input = fh.read()

board_data_list = []

for i, line in enumerate(input.splitlines()):
    if i == 0:
        draw_nums = list(map(int, line.split(",")))
        continue
    if line:
        board_data_list.append(list(map(int, line.split())))

all_board_data = np.array(board_data_list)
boards = np.array_split(all_board_data, all_board_data.shape[0] / 5)


def calc_answer(arr, draw):
    answer = draw * np.sum(arr[arr != -1])
    print(answer)


def play():
    for draw in draw_nums:
        for board in boards:
            if draw in board:
                board[board == draw] = -1

                for row in board:
                    if np.all(row == -1):
                        # we have a winner
                        return calc_answer(board, draw)
                for col in board.transpose():
                    if np.all(col == -1):
                        # we have a winner
                        return calc_answer(board, draw)

                # if np.all(board.diagonal() == -1):
                #     # we have a winner
                #     ...
                #     raise(SystemExit)
                # if np.all(np.fliplr(board).diagonal() == -1):
                #     # we have a winner
                #     ...
                #     raise(SystemExit)


return_value = play()
