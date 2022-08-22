"""
    Shayane Katchera
    SquareCraft
    Classe contenant la camera
"""

import utils

class Cam:
    def __init__(self, x, y) -> None:
        self.width = utils.Width
        self.height = utils.Height
        self.minx = x
        self.miny = y
        self.maxx = x + self.width
        self.maxy = y + self.height