"""
    Shayane Katchera
    SquareCraft
    Code contenant la classe Player
"""

import utils

class Player():
    def __init__(self, X, Y) -> None:
        self.X = X
        self.Y = Y
        self._x = int(utils.BlockSize*(self.X+0.5))
        self._y = utils.BlockSize*self.Y