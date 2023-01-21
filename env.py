import numpy as np
import pygame

class Reversi:
    EMPTY = 0
    WHITE = 1
    BLACK = 2

    def __init__(self, size):
        assert(size % 2 == 0 and size > 2)
        self.size = size
        self.grid = [[Reversi.EMPTY for _ in range(size)] for _ in range(size)] # [row][column]
        middle = int(self.size / 2)
        self.grid[middle][middle] = Reversi.BLACK
        self.grid[middle - 1][middle - 1] = Reversi.BLACK
        self.grid[middle][middle- 1] = Reversi.WHITE
        self.grid[middle- 1][middle] = Reversi.WHITE
        action_space = [(middle - 2, middle),(middle -1, middle + 1),(middle, middle -2),(middle +1, middle -1)] # the possible actions the next player / agent can make

    # update the grid and action space after the player make an action
    def step(self, action):
        pass
        #return next_state, reward, done

    def reset(self):
        pass

    def rendor(self):
        for row in self.grid:
            print(row)

if __name__=="__main__":
    r = Reversi(8)
    r.rendor()
