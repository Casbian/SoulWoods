####################################################################################################
import pygame
####################################################################################################
class ENEMY:
    def __init__(self):
        self.ENEMYRIGHT = pygame.image.load('bin/assets/Enemy/1.png')
        self.ENEMYRIGHTSCALED = pygame.transform.scale(self.ENEMYRIGHT, (self.ENEMYRIGHT.get_width() // 2, self.ENEMYRIGHT.get_height() // 2))
        self.ENEMYLEFT= pygame.image.load('bin/assets/Enemy/2.png')
        self.ENEMYLEFTSCALED = pygame.transform.scale(self.ENEMYLEFT, (self.ENEMYLEFT.get_width() // 2, self.ENEMYLEFT.get_height() // 2))
####################################################################################################