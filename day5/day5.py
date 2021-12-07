import numpy
import numpy as np
from typing import Tuple


class Board:
    def __init__(self, size: int):
        self.board = np.zeros((size, size))

    def add_line(self, start_pos: Tuple[int, int], end_pos: Tuple[int, int]):
        x1, y1 = start_pos  # 0, 9
        x2, y2 = end_pos  # 5, 9
        x_dist = x1 - x2  # -5
        y_dist = y1 - y2  # 0
        x_points = []
        y_points = []
        direction = numpy.sign([x_dist, y_dist])
        steps = max(abs(x_dist), abs(y_dist)) + 1
        if abs(x_dist) > abs(y_dist):
            x_points = [x1 - (i * direction[0]) for i in range(steps)]
            y_points = [y1 for i in range(steps)]
        elif abs(x_dist) < abs(y_dist):
            x_points = [x1 for i in range(steps)]
            y_points = [y1 - (i * direction[1]) for i in range(steps)]
        else:
            x_points = [x1 - (i * direction[0]) for i in range(steps)]
            y_points = [y1 - (i * direction[1]) for i in range(steps)]
        if x_points and y_points:
            steps = list(zip(x_points, y_points))
            for step in steps:
                x, y = step
                self.board[y, x] += 1

    def get_danger_points(self):
        _, count = numpy.unique(self.board, return_counts=True)
        number_of_danger_points = sum(count[2:])
        return number_of_danger_points

with open('input.txt', 'r') as file:
    lines = file.readlines()
    data = [line.rstrip().split(' -> ') for line in lines]



def main():
    board = Board(1000)
    for line in data:
        board.add_line(eval(line[0]), eval(line[1]))
    # print(board.board)
    print(board.get_danger_points())



if __name__ == '__main__':
    main()
