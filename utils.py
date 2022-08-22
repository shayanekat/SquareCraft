"""
    Katchera Shayane
    SquareCraft
    Fonctions utiles
"""

import random

# functions
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
    # initialiser le terrain
    world = [[air for j in range(WorldWidth)] for i in range(WorldHeight)]
    world[-1] = [bedrock for j in range(WorldWidth)]
    
    # bruit
    noise = [random.randint(25, 30) for i in range(WorldWidth)]
    for j in range(3):
        new = [0 for i in range(WorldWidth)]
        new[0] = (noise[0]+noise[1])/2
        new[-1] = (noise[-1]+noise[-2])/2
        for i in range(1, WorldWidth-1):
            new[i] = int((noise[i-1]+noise[i]+noise[i+1])/3)
        noise = new.copy()
    
    # generer le terrain
    for j in range(WorldHeight-1):
        h = WorldHeight-j
        for i in range(WorldWidth):
            if h < noise[i]:
                world[j][i] = stone
            elif h == noise[i]:
                world[j][i] = grass
            elif h == noise[i]-1:
                world[j][i] = dirt
            else:
                world[j][i] = air

    # afficher le terrain
    for j in range(WorldHeight):
        print("".join(world[j]))

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

if __name__ == '__main__':
    generate()