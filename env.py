import numpy as np


class Reversi:
    EMPTY = 0
    WHITE = 1
    BLACK = 2

    def __init__(self, size):
        action_space = []  # the possible actions the next player / agent can make
        grid = [[Reversi.EMPTY for _ in range(size)] for _ in range(size)]

    # update the grid and action space
    def step(self, action):
        return next_state, reward, done

    def reset(self):
        pass

    def rendor(self):
        pass
