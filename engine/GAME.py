import tkinter as tk
import threading
import pygame
class GAME:
    def __init__(self):
        self.SCREEN = pygame.display.set_mode((1280, 1024))
        self.CLOCK = pygame.time.Clock()
        self.RUNNING = True
        self.TICK = 0
    def Start(self):
        pygame.init()
        pygame.display.set_caption("SoulWoods")
        self.ICON = pygame.image.load("bin/assets/GameEssential/SoulWoods.ico")
        pygame.display.set_icon(self.ICON)
    def Exit(self):
        pygame.quit()