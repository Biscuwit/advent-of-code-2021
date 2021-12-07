class BingoBoard:
    def __init__(self, board):
        self.position = self._set_positions(board)
        self.bingo = {
            "row": [0, 0, 0, 0, 0],
            "col": [0, 0, 0, 0, 0],
        }
    @staticmethod
    def _set_positions(board):
        positions = {}
        for i, row in enumerate(board):
            for j, val in enumerate(row.split()):
                positions[val] = {'pos': (i, j), 'marked': False}
        return positions

    def updateBoard(self, val):
        if val in self.position:
            x, y = self.position[val]['pos']
            self.position[val]['marked'] = True
            self.updateBingo(x, y)

    def updateBingo(self, x, y):
        self.bingo["row"][x] += 1
        self.bingo["col"][y] += 1

    def checkBingo(self):
        return 5 in self.bingo["row"] or 5 in self.bingo["col"]

    def calc_win(self, new_number):
        sum = 0
        for key, val in self.position.items():
            if not val['marked']:
                sum += int(key)
        return sum*int(new_number)


with open('input.txt', 'r') as file:
    data = file.readlines()
    stripped_data = [line.rstrip() for line in data]
    board_data = data[1:]
    temp_boards = [board_data[i:i+5] for i in range(1, len(board_data), 6)]
    bingo_numbers = stripped_data[0].split(',')
    boards = [BingoBoard(board) for board in temp_boards]


def day4_A(boards):
    bingo_boards = [BingoBoard(board) for board in boards]
    for number in bingo_numbers:
        for board in bingo_boards:
            if not board.checkBingo():
                board.updateBoard(number)
                if board.checkBingo():
                    print(number)
                    print(board.calc_win(number))
                    return


def day4_B(boards):
    bingo_boards = [BingoBoard(board) for board in boards]
    final = 0
    for number in bingo_numbers:
        for board in bingo_boards:
            if not board.checkBingo():
                board.updateBoard(number)
                if board.checkBingo():
                    final = board.calc_win(number)
    print(final)


if __name__ == '__main__':
    day4_A(temp_boards)
    day4_B(temp_boards)
