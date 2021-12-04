import random

class Board():
    def __init__(self, dim, bombs):
        self.dim = dim
        self.bombs = bombs

    def make_board(self):
        board = [[-1 for _ in range(self.dim)] for _ in range(self.dim)]
        bombs_put = 0
        
        while bombs_put < self.bombs:
            bomb_loc = random.randint(0, self.dim**2 - 1)
            row = bomb_loc // self.dim
            col = bomb_loc % self.dim

            if board[row][col] == '*':
                continue

            board[row][col] == '*'
            bombs_put += 1

        return board

def play(dim=10, bombs=10):
    pass

# Testing
def testing():
    print(Board(10, 12).make_board())
testing()
