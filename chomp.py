import numpy as np
import pandas as pd
import random

EMOJI = {-1: '\u2612', 0: ' ', 1: '\u2610'}


class ChompGame:
    def __init__(self):
        playerx = input('Hi! How wide would you like the board')
        playery = input('What about height')
        if self.cols == playerx:
            self.cols = playerx
        else:
            self.cols = playerx

        if self.rows == playery:
            self.rows = playery
        else:
            self.rows = playery

    def __repr__(self):
        return f'{self.rows},{self.cols},{self.state}'

    def cointoss(self):
        cointossinput = [1,2]
        return cointossinput.random.choice

    def validsize(self):
        Board = Board()
        if Board > int(10):
            print ('Sorry thats invalid you must put something smaller')
        if Board < int(2):
            print ('Sorry thats invalid you must put something larger than that')

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
        row_idx = [chr(letter) for letter in range(65, 65 + self.rows)]
        board_emoji = np.array([[EMOJI[val] for val in row] for row in self.state])
        board_df = pd.DataFrame(data=board_emoji, index=row_idx, columns=col_idx)
        return str(board_df)

    def take(self, col, row):
        self.state[:row+1,col:]


class Player:
    def __init__(self):
        player1name = input('Player 1, what would you like your name to be?')
        player2name = input('Player 2, what would you like your name to be?')
    def __repr__(self):
        return f'{player1name},{player2name}'
