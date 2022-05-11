class Board:
    def __init__(self, _unit_list):
        self.chess_board = [[None] * 8 for _ in range(8)]
        for unit in _unit_list:
            self.input_unit(unit)

    def input_unit(self, unit):
        x, y = convert_pos_chess_to_coor(unit.chess_pos)
        self.chess_board[y][x] = unit

    def get_unit_from_pos(self, chess_pos):
        x, y = convert_pos_chess_to_coor(chess_pos)
        return self.chess_board[y][x]

    def print_board(self):
        for row in range(8):
            for col in range(8):
                cur = self.chess_board[row][col]
                if cur is None:
                    cur = '□'
                elif isinstance(cur, Rook):
                    cur = 'R'
                elif isinstance(cur, Knight):
                    cur = 'N'
                elif isinstance(cur, Bishop):
                    cur = 'B'
                elif isinstance(cur, Queen):
                    cur = 'Q'
                elif isinstance(cur, King):
                    cur = 'K'
                elif isinstance(cur, Pawn):
                    cur = 'P'
                print(cur, end='')
            print()


class Unit:
    def __init__(self, chess_pos, color):
        self.chess_pos, self.color = chess_pos, color

    def get_can_move(self):
        pass

    def print_info(self):
        print(self.chess_pos, self.color, end=' ')


class Rook(Unit):
    def __init__(self, chess_pos, color):
        super().__init__(chess_pos, color)

    def get_can_move(self):
        can_move_list = []
        x, y = convert_pos_chess_to_coor(self.chess_pos)
        for ny in range(8):
            if ny != y:
                can_move_list.append(convert_pos_coor_to_chess((x, ny)))
        for nx in range(8):
            if nx != x:
                can_move_list.append(convert_pos_coor_to_chess((nx, y)))

        return can_move_list


class Knight(Unit):
    def __init__(self, chess_pos, color):
        super().__init__(chess_pos, color)

    def get_can_move(self):
        can_move_list = []
        x, y = convert_pos_chess_to_coor(self.chess_pos)
        for dx, dy in zip([1, 2, 2, 1, -1, -2, -2, -1], [2, 1, -1, -2, -2, -1, 1, 2]):
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                can_move_list.append(convert_pos_coor_to_chess((nx, ny)))

        return can_move_list


class Bishop(Unit):
    def __init__(self, chess_pos, color):
        super().__init__(chess_pos, color)

    def get_can_move(self):
        can_move_list = []
        x, y = convert_pos_chess_to_coor(self.chess_pos)

        for nx, ny in zip(range(x + 1, x + 8), range(y + 1, y + 8)):
            if 0 <= nx < 8 and 0 <= ny < 8:
                can_move_list.append((convert_pos_coor_to_chess((nx, ny))))

        for nx, ny in zip(range(x - 1, x - 8, -1), range(y - 1, y - 8, -1)):
            if 0 <= nx < 8 and 0 <= ny < 8:
                can_move_list.append((convert_pos_coor_to_chess((nx, ny))))

        for nx, ny in zip(range(x + 1, x + 8), range(y - 1, y - 8, -1)):
            if 0 <= nx < 8 and 0 <= ny < 8:
                can_move_list.append((convert_pos_coor_to_chess((nx, ny))))

        for nx, ny in zip(range(x - 1, x - 8, -1), range(y + 1, y + 8, )):
            if 0 <= nx < 8 and 0 <= ny < 8:
                can_move_list.append((convert_pos_coor_to_chess((nx, ny))))

        return can_move_list


class Queen(Unit):
    def __init__(self, chess_pos, color):
        super().__init__(chess_pos, color)

    def get_can_move(self):
        can_move_list = []
        x, y = convert_pos_chess_to_coor(self.chess_pos)

        for nx, ny in zip(range(x + 1, x + 8), range(y + 1, y + 8)):
            if 0 <= nx < 8 and 0 <= ny < 8:
                can_move_list.append((convert_pos_coor_to_chess((nx, ny))))

        for nx, ny in zip(range(x - 1, x - 8, -1), range(y - 1, y - 8, -1)):
            if 0 <= nx < 8 and 0 <= ny < 8:
                can_move_list.append((convert_pos_coor_to_chess((nx, ny))))

        for nx, ny in zip(range(x + 1, x + 8), range(y - 1, y - 8, -1)):
            if 0 <= nx < 8 and 0 <= ny < 8:
                can_move_list.append((convert_pos_coor_to_chess((nx, ny))))

        for nx, ny in zip(range(x - 1, x - 8, -1), range(y + 1, y + 8, )):
            if 0 <= nx < 8 and 0 <= ny < 8:
                can_move_list.append((convert_pos_coor_to_chess((nx, ny))))

        for ny in range(8):
            if ny != y:
                can_move_list.append(convert_pos_coor_to_chess((x, ny)))
        for nx in range(8):
            if nx != x:
                can_move_list.append(convert_pos_coor_to_chess((nx, y)))

        return can_move_list


class King(Unit):
    def __init__(self, chess_pos, color):
        super().__init__(chess_pos, color)

    def get_can_move(self):
        can_move_list = []
        x, y = convert_pos_chess_to_coor(self.chess_pos)
        for dx, dy in zip([0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]):
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                can_move_list.append(convert_pos_coor_to_chess((nx, ny)))

        return can_move_list


class Pawn(Unit):
    def __init__(self, chess_pos, color, moved_yet=True):
        super().__init__(chess_pos, color)
        self.moved_yet = moved_yet

    def get_can_move(self):
        can_move_list = []
        x, y = convert_pos_chess_to_coor(self.chess_pos)
        if self.color == 'W':
            if self.moved_yet:
                can_move_list.append(convert_pos_coor_to_chess((x, y - 1)))
                can_move_list.append(convert_pos_coor_to_chess((x, y - 2)))
            else:
                can_move_list.append(convert_pos_coor_to_chess((x, y - 1)))



        elif self.color == 'B':
            if self.moved_yet:
                can_move_list.append(convert_pos_coor_to_chess((x, y + 1)))
                can_move_list.append(convert_pos_coor_to_chess((x, y + 2)))
            else:
                can_move_list.append(convert_pos_coor_to_chess((x, y + 1)))

        return can_move_list


def convert_pos_chess_to_coor(chess_pos):
    col, row = chess_pos[0], chess_pos[1]
    new_row = 8 - int(row)
    new_col = ord(col) - ord('a')
    return [new_col, new_row]


def convert_pos_coor_to_chess(coor_pos):
    col, row = coor_pos
    return chr(ord('a') + col) + str(8 - row)


unit_list = [Rook('a1', 'W'), Rook('h1', 'W'), Knight('b1', 'W'), Knight('g1', 'W'), Bishop('c1', 'W'),
             Bishop('f1', 'W'), Queen('d1', 'W'), King('e1', 'W'), Pawn('a2', 'W'), Pawn('b2', 'W'), Pawn('c2', 'W'),
             Pawn('d2', 'W'), Pawn('e2', 'W'), Pawn('f2', 'W'), Pawn('g2', 'W'), Pawn('h2', 'W'),

             Rook('a8', 'B'), Rook('h8', 'B'), Knight('b8', 'B'), Knight('g8', 'B'), Bishop('c8', 'B'),
             Bishop('f8', 'B'), Queen('d8', 'B'), King('e8', 'B'), Pawn('a7', 'B'), Pawn('b7', 'B'), Pawn('c7', 'B'),
             Pawn('d7', 'B'), Pawn('e7', 'B'), Pawn('f7', 'B'), Pawn('g7', 'B'), Pawn('h7', 'B')
             ]

board = Board(unit_list)
board.print_board()

cur = board.get_unit_from_pos('a2')
cur.print_info()
print(cur.get_can_move())
