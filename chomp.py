import numpy as np
import pandas as pd

EMOJI = {-1: '\u2612', 0: ' ', 1: '\u2610'}


class ChompGame:
    def __init__(self):
        self.self


    def __repr__(self):
        return f'{self.rows},{self.cols},{self.state}'


class Board:
    def __init__(self, rows, cols):
        # Use a 2d array to store board state
        # ones for chocolate, zeros for eaten squares, and -1 for poison
        self.rows = rows
        self.cols = cols
        self.state = np.ones((rows, cols), dtype=int)
        self.state[-1][0] = -1

    def __repr__(self):
        return f'Board({self.rows}, {self.cols})'

    def __str__(self):
        col_idx = range(self.cols)
        row_idx = [chr(letter) for letter in range(65, 65+self.rows)]
        board_emoji = np.array([[EMOJI[val] for val in row] for row in self.state])
        board_df = pd.DataFrame(data=board_emoji, index=row_idx, columns=col_idx)
        return str(board_df)

    def take(self, row, col):
        playerx = input('Hi! How wide would you like the board')
        playery = input('What about height')
        self.cols = playerx
        self.rows = playery
class Player:
    def __init__(self):
        coordinatey = self.rows
        coordinatex = self.cols
        self.player = 2
        player = coordinate

    def __repr__(self):
        pass
