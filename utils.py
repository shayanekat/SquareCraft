"""
    Katchera Shayane
    SquareCraft
    Fonctions utiles
"""

# functions
from logging.config import stopListening


def open():
    """
    ouvrir le fichier de sauvegarde ou le creer si il n'existe pas
    """
    pass

def save():
    """
    sauvegarder le fichier de sauvegarde
    """
    pass

def load():
    """
    charger le fichier de sauvegarde
    """
    pass

def generate():
    """
    generer le terrain
    """
    world = [air*WorldWidth for i in range(WorldHeight)]
    world[-1] = bedrock*WorldWidth

# constants
BlockSize = 100
WorldWidth = 100
WorldHeight = 50
Width = 1000
Height = 500

# colors
Sky = (135, 206, 250)

# block dict
bedrock = "@"
stone = "O"
dirt = "D"
grass = "_"
log = "|"
plank = "="
leaves = "L"
diamond = "d"
gold = "g"
air = " "