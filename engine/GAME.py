import pygame
import sys
class GAME:
    def __init__(self):
        self.SCREEN = pygame.display.set_mode((1280, 1024))
        self.CLOCK = pygame.time.Clock()
        self.RUNNING = False
        self.TICK = 0
        self.TITLEMENURUNNING = True
        self.MOVEMENTSETTINGSRUNNING = False
        self.CURRENTTIME = 0
    def TitleMenu(self):
        self.TITLEMENUPNG = pygame.image.load('bin/assets/GameEssential/GUI/TITLEMENU.png')
        self.TITLEMENUPNGSCALED = pygame.transform.scale(self.TITLEMENUPNG, (self.TITLEMENUPNG.get_width() // 2, self.TITLEMENUPNG.get_height() // 2)) 
        self.MOVEMENTSETTINGPNG = pygame.image.load('bin/assets/GameEssential/GUI/MOVEMENTSETTING.png')
        self.MOVEMENTSETTINGPNGSCALED = pygame.transform.scale(self.MOVEMENTSETTINGPNG, (self.MOVEMENTSETTINGPNG.get_width() // 2, self.MOVEMENTSETTINGPNG.get_height() // 2))
        self.MOVEMENTSETTINGBACKBUTTONPNG = pygame.image.load('bin/assets/GameEssential/GUI/MOVEMENTSETTINGBACKBUTTON.png')
        self.MOVEMENTSETTINGBACKBUTTONPNGSCALED = pygame.transform.scale(self.MOVEMENTSETTINGBACKBUTTONPNG, (self.MOVEMENTSETTINGBACKBUTTONPNG.get_width() // 2, self.MOVEMENTSETTINGBACKBUTTONPNG.get_height() // 2))
        self.STARTGAMEBUTTONPNG = pygame.image.load('bin/assets/GameEssential/GUI/STARTGAMEBUTTON.png')
        self.STARTGAMEBUTTONPNGSCALED = pygame.transform.scale(self.STARTGAMEBUTTONPNG, (self.STARTGAMEBUTTONPNG.get_width() // 2, self.STARTGAMEBUTTONPNG.get_height() // 2))
        self.CONTROLSGAMEBUTTONPNG = pygame.image.load('bin/assets/GameEssential/GUI/CONTROLSGAMEBUTTON.png')
        self.CONTROLSGAMEBUTTONPNGSCALED = pygame.transform.scale(self.CONTROLSGAMEBUTTONPNG, (self.CONTROLSGAMEBUTTONPNG.get_width() // 2, self.CONTROLSGAMEBUTTONPNG.get_height() // 2))
        self.EXITGAMEBUTTONPNG = pygame.image.load('bin/assets/GameEssential/GUI/EXITGAMEBUTTON.png')
        self.EXITGAMEBUTTONPNGSCALED = pygame.transform.scale(self.EXITGAMEBUTTONPNG, (self.EXITGAMEBUTTONPNG.get_width() // 2, self.EXITGAMEBUTTONPNG.get_height() // 2))
        while self.TITLEMENURUNNING:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.TITLEMENURUNNING = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.STARTGAMEBUTTONRECT.collidepoint(event.pos):
                        self.TITLEMENURUNNING = False
                        self.RUNNING = True
                    if self.CONTROLSGAMEBUTTONRECT.collidepoint(event.pos):
                        self.MOVEMENTSETTINGSRUNNING = True
                        self.SCREENMID = pygame.Vector2(self.SCREEN.get_width() / 2, self.SCREEN.get_height() / 2)
                        self.PNGPOSITION = self.MOVEMENTSETTINGPNGSCALED.get_rect()
                        self.PNGPOSITION.center = self.SCREENMID
                        self.SCREEN.blit(self.MOVEMENTSETTINGPNGSCALED ,self.PNGPOSITION)
                        self.MOVEMENTSETTINGBACKBUTTONRECT = self.MOVEMENTSETTINGBACKBUTTONPNGSCALED.get_rect()
                        self.MOVEMENTSETTINGBACKBUTTONRECT.center = self.SCREENMID
                        self.MOVEMENTSETTINGBACKBUTTONRECT.y = self.MOVEMENTSETTINGBACKBUTTONRECT.y + 174
                        self.MOVEMENTSETTINGBACKBUTTONRECT.x = self.MOVEMENTSETTINGBACKBUTTONRECT.x + 210
                        self.SCREEN.blit(self.MOVEMENTSETTINGBACKBUTTONPNGSCALED ,self.MOVEMENTSETTINGBACKBUTTONRECT)
                    if self.MOVEMENTSETTINGSRUNNING == True and self.MOVEMENTSETTINGBACKBUTTONRECT.collidepoint(event.pos):
                        self.MOVEMENTSETTINGSRUNNING = False               
                    if self.EXITGAMEBUTTONRECT.collidepoint(event.pos):
                        self.Exit()
                        self.SKIPGAME = 1        
            self.TICK = self.CLOCK.tick(60) / 1000
            self.CURRENTTIME = pygame.time.get_ticks() / 1000
            if self.MOVEMENTSETTINGSRUNNING != True:    
                self.SCREENMID = pygame.Vector2(self.SCREEN.get_width() / 2, self.SCREEN.get_height() / 2)
                self.PNGPOSITION = self.TITLEMENUPNGSCALED.get_rect()
                self.PNGPOSITION.center = self.SCREENMID
                self.SCREEN.blit(self.TITLEMENUPNGSCALED ,self.PNGPOSITION)
                self.STARTGAMEBUTTONRECT = self.STARTGAMEBUTTONPNGSCALED.get_rect()
                self.STARTGAMEBUTTONRECT.center = self.SCREENMID
                self.STARTGAMEBUTTONRECT.y = self.STARTGAMEBUTTONRECT.y - 195
                self.SCREEN.blit(self.STARTGAMEBUTTONPNGSCALED ,self.STARTGAMEBUTTONRECT)
                self.CONTROLSGAMEBUTTONRECT = self.CONTROLSGAMEBUTTONPNGSCALED.get_rect()
                self.CONTROLSGAMEBUTTONRECT.center = self.SCREENMID
                self.CONTROLSGAMEBUTTONRECT.y = self.CONTROLSGAMEBUTTONRECT.y + 50
                self.SCREEN.blit(self.CONTROLSGAMEBUTTONPNGSCALED ,self.CONTROLSGAMEBUTTONRECT)
                self.PNGPOSITION = self.EXITGAMEBUTTONPNGSCALED.get_rect()
                self.EXITGAMEBUTTONRECT = self.EXITGAMEBUTTONPNGSCALED.get_rect()
                self.EXITGAMEBUTTONRECT.center = self.SCREENMID
                self.EXITGAMEBUTTONRECT.y = self.EXITGAMEBUTTONRECT.y + 260
                self.SCREEN.blit(self.EXITGAMEBUTTONPNGSCALED ,self.EXITGAMEBUTTONRECT)
            pygame.display.flip()
    def Start(self):
        pygame.init()
        pygame.display.set_caption("SoulWoods")
        self.ICON = pygame.image.load("bin/assets/GameEssential/TITLE/SoulWoods.ico")
        pygame.display.set_icon(self.ICON)
    def Exit(self):
        pygame.quit()
        sys.exit()       