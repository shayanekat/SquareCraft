"""
    Shayane Katchera
    SquareCraft
"""

import Blocks
import Player
import utils
import pygame


# ===== frontend =====
# creation de la fenetre
pygame.init()
screen = pygame.display.set_mode((utils.Width, utils.Height))
pygame.display.set_caption("SquareCraft")
# set background color
pygame.draw.rect(screen, utils.Sky, (0, 0, utils.Width, utils.Height))


# boucle principale
running = True
while running:


    # gestion des evenements
    for event in pygame.event.get():
        # quitter
        if event.type == pygame.QUIT:
            utils.save()
            running = False


    pygame.display.flip()