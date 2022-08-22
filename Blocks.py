"""
    Shayane Katchera
    SquareCraft
    Code contenant la classe Blocks
"""

import pygame
import utils

# class
class Block:
    def __init__(self, tt, X, Y):
        self.size = utils.BlockSize
        self.texture = pygame.image.load(tt)
        self.X = X
        self.Y = Y
        self._x = self.X*self.size
        self._y = self.Y*self.size