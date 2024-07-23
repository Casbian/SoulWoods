import pygame
class TITLE:
    def __init__(self, GAMEINSTANCE):
        self.TITLERUNNING = True
        GAMEINSTANCE.SCREEN = pygame.display.set_mode((1280, 1024), pygame.NOFRAME)
        self.TITLEPNG = pygame.image.load('bin/assets/GameEssential/TITLE/SoulWoodsTitle.png')
        self.TITLEPNGSCALED = pygame.transform.scale(self.TITLEPNG, (self.TITLEPNG.get_width() // 2, self.TITLEPNG.get_height() // 2))
        self.TIMER = 0
        while self.TITLERUNNING:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.TITLERUNNING = False
            GAMEINSTANCE.TICK = GAMEINSTANCE.CLOCK.tick(60) / 1000
            self.SCREENMID = pygame.Vector2(GAMEINSTANCE.SCREEN.get_width() / 2, GAMEINSTANCE.SCREEN.get_height() / 2)
            self.PNGPOSITION = self.TITLEPNGSCALED.get_rect()
            self.PNGPOSITION.center = self.SCREENMID
            GAMEINSTANCE.SCREEN.blit(self.TITLEPNGSCALED, self.PNGPOSITION)
            self.TIMER = self.TIMER + 1
            if self.TIMER == 75:
                self.TITLERUNNING = False
            pygame.display.flip()