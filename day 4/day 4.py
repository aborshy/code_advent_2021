# get raw data from file
with open("input.txt") as x:
    lines = x.readlines()

# init variables

# create flattened array of all drawing number integers
draw_nums = [int(x) for x in lines[0].split(',')]

# create flattened array of all board spot integers
raw_board_spots = [line.strip() for line in lines[1:]]
rows = [spot.split() for spot in raw_board_spots if spot]

# convert all strings to ints
for a, row in enumerate(rows):
    for b, num in enumerate(row):
        rows[a][b] = int(num)

# create flattened list of every board spot
flattened_rows = [int(spot) for row in rows for spot in row]

# create flattened boards
flattened_boards = [flattened_rows[x:x + 25] for x in range(0, len(flattened_rows), 25)]

"""
visualization of board
0 1 2 3 4
5 6 7 8 9
10 11 12 13 14
15 16 17 18 19
20 21 22 23 24
"""


def check_num(draw, board):
    """
    take in board from current loop
    return board with current drawn number replaced with 0
    """
    board = [x if x != draw else 0 for x in board]
    return board


def check_rows(board):
    """
    take in board from current loop
    return string win to fulfill if statement to return from loop
    """
    for x in [0, 5, 19, 15, 20]:
        if board[x] == board[x + 1] == board[x + 2] == board[x + 3] == board[x + 4]:
            return 'win'


def check_cols(board):
    """
    take in board from current loop
    return string win to fulfill if statement to return from loop
    """
    for x in [0, 1, 2, 3, 4]:
        if board[x] == board[x + 5] == board[x + 10] == board[x + 15] == board[x + 20]:
            return 'win'


def play(flattened_boards, draw_nums):
    """
    for each drawn number
    replace number in each board with 0
    then check each board (in order) if there is a bingo
    """
    for draw in draw_nums:
        for n, board in enumerate(flattened_boards):
            flattened_boards[n] = check_num(draw, board)
            if check_cols(flattened_boards[n]) == 'win':
                return flattened_boards[n], draw
            if check_rows(flattened_boards[n]) == 'win':
                return flattened_boards[n], draw
    return "Error! No bingo's!", 1


winner, winning_draw = play(flattened_boards, draw_nums)

print(sum(winner) * winning_draw)

"""
I suppose I didn't have to replace all indexes as ints, as that would save some lines. Whatever.
"""
