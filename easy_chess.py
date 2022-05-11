def print_board():
    global board

    for row in range(8):
        for col in range(8):
            print(board[row][col], end='')
        print()


def convert_pos(chess_pos):
    # ex) h8 -> [0][7]
    row, col = chess_pos[1], chess_pos[0]
    new_row = 8 - int(row)
    new_col = ord(col) - 97  # a is 97
    return [new_row, new_col]


def input_unit(chess_pos, unit):
    global board

    new_pos = convert_pos(chess_pos)
    new_row, new_col = new_pos[0], new_pos[1]
    board[new_row][new_col] = unit


board = []
for _ in range(8):
    temp = [0] * 8
    board.append(temp)

input_unit('a1', 'R')
input_unit('b1', 'N')
input_unit('c1', 'B')
input_unit('d1', 'Q')
input_unit('e1', 'K')
input_unit('f1', 'B')
input_unit('g1', 'N')
input_unit('h1', 'R')

input_unit('a2', 'P')
input_unit('b2', 'P')
input_unit('c2', 'P')
input_unit('d2', 'P')
input_unit('e2', 'P')
input_unit('f2', 'P')
input_unit('g2', 'P')
input_unit('h2', 'P')

print_board()
