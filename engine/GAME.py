import pygame
import sys
class GAME:
    def __init__(self):
        self.SCREEN = None
        self.CLOCK = pygame.time.Clock()
        self.GAMERUNNING = True
        self.TICK = None
    def Start(self):
        pygame.init()
        pygame.display.set_caption("SoulWoods")
        self.ICON = pygame.image.load("bin/assets/GameEssential/TITLE/SoulWoods.ico")
        pygame.display.set_icon(self.ICON)
    def Exit(self):
        pygame.quit()
        sys.exit()  