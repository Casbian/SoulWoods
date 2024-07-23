import pygame
class TITLEMENU:
    def __init__(self, GAMEINSTANCE):
        GAMEINSTANCE.SCREEN = pygame.display.set_mode((1280, 1024))
        self.TITLEMENURUNNING = True
        self.MOVEMENTSETTINGSRUNNING = False
        self.SCREENMID = pygame.Vector2(GAMEINSTANCE.SCREEN.get_width() / 2, GAMEINSTANCE.SCREEN.get_height() / 2)
        self.CONTROLSGAMEBUTTONHOVERPNG = pygame.image.load('bin/assets/GameEssential/GUI/CONTROLSGAMEBUTTONHOVER.png')
        self.CONTROLSGAMEBUTTONHOVERPNGSCALED = pygame.transform.scale(self.CONTROLSGAMEBUTTONHOVERPNG, (self.CONTROLSGAMEBUTTONHOVERPNG.get_width() // 2, self.CONTROLSGAMEBUTTONHOVERPNG.get_height() // 2))
        self.STARTGAMEBUTTONHOVERPNG = pygame.image.load('bin/assets/GameEssential/GUI/STARTGAMEBUTTONHOVER.png')
        self.STARTGAMEBUTTONHOVERPNGSCALED = pygame.transform.scale(self.STARTGAMEBUTTONHOVERPNG, (self.STARTGAMEBUTTONHOVERPNG.get_width() // 2, self.STARTGAMEBUTTONHOVERPNG.get_height() // 2))
        self.EXITGAMEBUTTONHOVERPNG = pygame.image.load('bin/assets/GameEssential/GUI/EXITGAMEBUTTONHOVER.png')
        self.EXITGAMEBUTTONHOVERPNGSCALED = pygame.transform.scale(self.EXITGAMEBUTTONHOVERPNG, (self.EXITGAMEBUTTONHOVERPNG.get_width() // 2, self.EXITGAMEBUTTONHOVERPNG.get_height() // 2))
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
                    GAMEINSTANCE.Exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.STARTGAMEBUTTONRECT.collidepoint(event.pos):
                        self.TITLEMENURUNNING = False
                    if self.CONTROLSGAMEBUTTONRECT.collidepoint(event.pos):
                        self.MOVEMENTSETTINGSRUNNING = True
                        self.MOVEMENTSETTINGRECT = self.MOVEMENTSETTINGPNGSCALED.get_rect()
                        self.MOVEMENTSETTINGRECT.center = self.SCREENMID
                        GAMEINSTANCE.SCREEN.blit(self.MOVEMENTSETTINGPNGSCALED ,self.MOVEMENTSETTINGRECT)
                        self.MOVEMENTSETTINGBACKBUTTONRECT = self.MOVEMENTSETTINGBACKBUTTONPNGSCALED.get_rect()
                        self.MOVEMENTSETTINGBACKBUTTONRECT.center = self.SCREENMID
                        self.MOVEMENTSETTINGBACKBUTTONRECT.y = self.MOVEMENTSETTINGBACKBUTTONRECT.y + 174
                        self.MOVEMENTSETTINGBACKBUTTONRECT.x = self.MOVEMENTSETTINGBACKBUTTONRECT.x + 210
                        GAMEINSTANCE.SCREEN.blit(self.MOVEMENTSETTINGBACKBUTTONPNGSCALED ,self.MOVEMENTSETTINGBACKBUTTONRECT)
                    if self.MOVEMENTSETTINGSRUNNING == True and self.MOVEMENTSETTINGBACKBUTTONRECT.collidepoint(event.pos):
                        self.MOVEMENTSETTINGSRUNNING = False               
                    if self.EXITGAMEBUTTONRECT.collidepoint(event.pos):
                        GAMEINSTANCE.Exit()     
            GAMEINSTANCE.TICK = GAMEINSTANCE.CLOCK.tick(60) / 1000
            if self.MOVEMENTSETTINGSRUNNING != True:    
                self.TITLEMENURECT = self.TITLEMENUPNGSCALED.get_rect()
                self.TITLEMENURECT.center = self.SCREENMID
                GAMEINSTANCE.SCREEN.blit(self.TITLEMENUPNGSCALED ,self.TITLEMENURECT)
                self.STARTGAMEBUTTONRECT = self.STARTGAMEBUTTONPNGSCALED.get_rect()
                self.STARTGAMEBUTTONRECT.center = self.SCREENMID
                self.STARTGAMEBUTTONRECT.y = self.STARTGAMEBUTTONRECT.y - 195
                GAMEINSTANCE.SCREEN.blit(self.STARTGAMEBUTTONPNGSCALED ,self.STARTGAMEBUTTONRECT)
                self.CONTROLSGAMEBUTTONRECT = self.CONTROLSGAMEBUTTONPNGSCALED.get_rect()
                self.CONTROLSGAMEBUTTONRECT.center = self.SCREENMID
                self.CONTROLSGAMEBUTTONRECT.y = self.CONTROLSGAMEBUTTONRECT.y + 50
                GAMEINSTANCE.SCREEN.blit(self.CONTROLSGAMEBUTTONPNGSCALED ,self.CONTROLSGAMEBUTTONRECT)
                self.EXITGAMEBUTTONRECT = self.EXITGAMEBUTTONPNGSCALED.get_rect()
                self.EXITGAMEBUTTONRECT.center = self.SCREENMID
                self.EXITGAMEBUTTONRECT.y = self.EXITGAMEBUTTONRECT.y + 260
                GAMEINSTANCE.SCREEN.blit(self.EXITGAMEBUTTONPNGSCALED ,self.EXITGAMEBUTTONRECT)       
            if self.STARTGAMEBUTTONRECT.collidepoint(pygame.mouse.get_pos()) and self.MOVEMENTSETTINGSRUNNING != True:
                GAMEINSTANCE.SCREEN.blit(self.STARTGAMEBUTTONHOVERPNGSCALED ,self.STARTGAMEBUTTONRECT)                        
            if self.CONTROLSGAMEBUTTONRECT.collidepoint(pygame.mouse.get_pos()) and self.MOVEMENTSETTINGSRUNNING != True:
                GAMEINSTANCE.SCREEN.blit(self.CONTROLSGAMEBUTTONHOVERPNGSCALED ,self.CONTROLSGAMEBUTTONRECT)
            if self.EXITGAMEBUTTONRECT.collidepoint(pygame.mouse.get_pos()) and self.MOVEMENTSETTINGSRUNNING != True:
                GAMEINSTANCE.SCREEN.blit(self.EXITGAMEBUTTONHOVERPNGSCALED ,self.EXITGAMEBUTTONRECT)       
            pygame.display.flip()