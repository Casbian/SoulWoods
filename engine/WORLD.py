####################################################################################################
import random
import pygame
####################################################################################################
class WORLD():
    def __init__(self):
        self.ENVIRONMENTEMPTY = pygame.image.load('bin/assets/Environment/Empty/0.png')
        self.ENVIRONMENTEMPTYSCALED = pygame.transform.scale(self.ENVIRONMENTEMPTY, (self.ENVIRONMENTEMPTY.get_width() // 2, self.ENVIRONMENTEMPTY.get_height() // 2))
        
        self.ENVIRONMENTDIRT1 = pygame.image.load("bin/assets/Environment/Dirt/1.png")
        self.ENVIRONMENTDIRT1SCALED = pygame.transform.scale(self.ENVIRONMENTDIRT1, (self.ENVIRONMENTDIRT1.get_width() // 2, self.ENVIRONMENTDIRT1.get_height() // 2))
        self.ENVIRONMENTDIRT2 = pygame.image.load("bin/assets/Environment/Dirt/2.png")
        self.ENVIRONMENTDIRT2SCALED = pygame.transform.scale(self.ENVIRONMENTDIRT2, (self.ENVIRONMENTDIRT2.get_width() // 2, self.ENVIRONMENTDIRT2.get_height() // 2))
        self.ENVIRONMENTDIRT3 = pygame.image.load("bin/assets/Environment/Dirt/3.png")
        self.ENVIRONMENTDIRT3SCALED = pygame.transform.scale(self.ENVIRONMENTDIRT3, (self.ENVIRONMENTDIRT3.get_width() // 2, self.ENVIRONMENTDIRT3.get_height() // 2))
        self.ENVIRONMENTDIRT4 = pygame.image.load("bin/assets/Environment/Dirt/4.png")
        self.ENVIRONMENTDIRT4SCALED = pygame.transform.scale(self.ENVIRONMENTDIRT4, (self.ENVIRONMENTDIRT4.get_width() // 2, self.ENVIRONMENTDIRT4.get_height() // 2))
        self.ENVIRONMENTDIRT5 = pygame.image.load("bin/assets/Environment/Dirt/5.png")
        self.ENVIRONMENTDIRT5SCALED = pygame.transform.scale(self.ENVIRONMENTDIRT5, (self.ENVIRONMENTDIRT5.get_width() // 2, self.ENVIRONMENTDIRT5.get_height() // 2))
        self.ENVIRONMENTDIRT6 = pygame.image.load("bin/assets/Environment/Dirt/6.png")
        self.ENVIRONMENTDIRT6SCALED = pygame.transform.scale(self.ENVIRONMENTDIRT6, (self.ENVIRONMENTDIRT6.get_width() // 2, self.ENVIRONMENTDIRT6.get_height() // 2))
        self.ENVIRONMENTDIRT7 = pygame.image.load("bin/assets/Environment/Dirt/7.png")
        self.ENVIRONMENTDIRT7SCALED = pygame.transform.scale(self.ENVIRONMENTDIRT7, (self.ENVIRONMENTDIRT7.get_width() // 2, self.ENVIRONMENTDIRT7.get_height() // 2))
        self.ENVIRONMENTDIRT8 = pygame.image.load("bin/assets/Environment/Dirt/8.png")
        self.ENVIRONMENTDIRT8SCALED = pygame.transform.scale(self.ENVIRONMENTDIRT8, (self.ENVIRONMENTDIRT8.get_width() // 2, self.ENVIRONMENTDIRT8.get_height() // 2))
        self.ENVIRONMENTDIRT9 = pygame.image.load("bin/assets/Environment/Dirt/9.png")
        self.ENVIRONMENTDIRT9SCALED = pygame.transform.scale(self.ENVIRONMENTDIRT9, (self.ENVIRONMENTDIRT9.get_width() // 2, self.ENVIRONMENTDIRT9.get_height() // 2))
        self.ENVIRONMENTDIRT10 = pygame.image.load("bin/assets/Environment/Dirt/10.png")
        self.ENVIRONMENTDIRT10SCALED = pygame.transform.scale(self.ENVIRONMENTDIRT10, (self.ENVIRONMENTDIRT10.get_width() // 2, self.ENVIRONMENTDIRT10.get_height() // 2))
        self.ENVIRONMENTDIRT11 = pygame.image.load("bin/assets/Environment/Dirt/11.png")
        self.ENVIRONMENTDIRT11SCALED = pygame.transform.scale(self.ENVIRONMENTDIRT11, (self.ENVIRONMENTDIRT11.get_width() // 2, self.ENVIRONMENTDIRT11.get_height() // 2))
        self.ENVIRONMENTDIRT12 = pygame.image.load("bin/assets/Environment/Dirt/12.png")
        self.ENVIRONMENTDIRT12SCALED = pygame.transform.scale(self.ENVIRONMENTDIRT12, (self.ENVIRONMENTDIRT12.get_width() // 2, self.ENVIRONMENTDIRT12.get_height() // 2))
        self.ENVIRONMENTDIRT13 = pygame.image.load("bin/assets/Environment/Dirt/13.png")
        self.ENVIRONMENTDIRT13SCALED = pygame.transform.scale(self.ENVIRONMENTDIRT13, (self.ENVIRONMENTDIRT13.get_width() // 2, self.ENVIRONMENTDIRT13.get_height() // 2))
        self.ENVIRONMENTDIRT14 = pygame.image.load("bin/assets/Environment/Dirt/14.png")
        self.ENVIRONMENTDIRT14SCALED = pygame.transform.scale(self.ENVIRONMENTDIRT14, (self.ENVIRONMENTDIRT14.get_width() // 2, self.ENVIRONMENTDIRT14.get_height() // 2))
        self.ENVIRONMENTDIRT15 = pygame.image.load("bin/assets/Environment/Dirt/15.png")
        self.ENVIRONMENTDIRT15SCALED = pygame.transform.scale(self.ENVIRONMENTDIRT15, (self.ENVIRONMENTDIRT15.get_width() // 2, self.ENVIRONMENTDIRT15.get_height() // 2))
        self.ENVIRONMENTDIRT16 = pygame.image.load("bin/assets/Environment/Dirt/16.png")
        self.ENVIRONMENTDIRT16SCALED = pygame.transform.scale(self.ENVIRONMENTDIRT16, (self.ENVIRONMENTDIRT16.get_width() // 2, self.ENVIRONMENTDIRT16.get_height() // 2))
        self.ENVIRONMENTDIRT17 = pygame.image.load("bin/assets/Environment/Dirt/17.png")
        self.ENVIRONMENTDIRT17SCALED = pygame.transform.scale(self.ENVIRONMENTDIRT17, (self.ENVIRONMENTDIRT17.get_width() // 2, self.ENVIRONMENTDIRT17.get_height() // 2))
        self.ENVIRONMENTDIRT18 = pygame.image.load("bin/assets/Environment/Dirt/18.png")
        self.ENVIRONMENTDIRT18SCALED = pygame.transform.scale(self.ENVIRONMENTDIRT18, (self.ENVIRONMENTDIRT18.get_width() // 2, self.ENVIRONMENTDIRT18.get_height() // 2))
        self.ENVIRONMENTDIRT19 = pygame.image.load("bin/assets/Environment/Dirt/19.png")
        self.ENVIRONMENTDIRT19SCALED = pygame.transform.scale(self.ENVIRONMENTDIRT19, (self.ENVIRONMENTDIRT19.get_width() // 2, self.ENVIRONMENTDIRT19.get_height() // 2))
        self.ENVIRONMENTDIRT20 = pygame.image.load("bin/assets/Environment/Dirt/20.png")
        self.ENVIRONMENTDIRT20SCALED = pygame.transform.scale(self.ENVIRONMENTDIRT20, (self.ENVIRONMENTDIRT20.get_width() // 2, self.ENVIRONMENTDIRT20.get_height() // 2))
        self.ENVIRONMENTDIRT21 = pygame.image.load("bin/assets/Environment/Dirt/21.png")
        self.ENVIRONMENTDIRT21SCALED = pygame.transform.scale(self.ENVIRONMENTDIRT21, (self.ENVIRONMENTDIRT21.get_width() // 2, self.ENVIRONMENTDIRT21.get_height() // 2))
        self.ENVIRONMENTDIRT22 = pygame.image.load("bin/assets/Environment/Dirt/22.png")
        self.ENVIRONMENTDIRT22SCALED = pygame.transform.scale(self.ENVIRONMENTDIRT22, (self.ENVIRONMENTDIRT22.get_width() // 2, self.ENVIRONMENTDIRT22.get_height() // 2))
        self.ENVIRONMENTDIRT23 = pygame.image.load("bin/assets/Environment/Dirt/23.png")
        self.ENVIRONMENTDIRT23SCALED = pygame.transform.scale(self.ENVIRONMENTDIRT23, (self.ENVIRONMENTDIRT23.get_width() // 2, self.ENVIRONMENTDIRT23.get_height() // 2))
        self.ENVIRONMENTDIRT24 = pygame.image.load("bin/assets/Environment/Dirt/24.png")
        self.ENVIRONMENTDIRT24SCALED = pygame.transform.scale(self.ENVIRONMENTDIRT24, (self.ENVIRONMENTDIRT24.get_width() // 2, self.ENVIRONMENTDIRT24.get_height() // 2))

        self.ENVIRONMENTGRASS1 = pygame.image.load("bin/assets/Environment/Grass/1.png")
        self.ENVIRONMENTGRASS1SCALED = pygame.transform.scale(self.ENVIRONMENTGRASS1, (self.ENVIRONMENTGRASS1.get_width() // 2, self.ENVIRONMENTGRASS1.get_height() // 2))
        self.ENVIRONMENTGRASS2 = pygame.image.load("bin/assets/Environment/Grass/2.png")
        self.ENVIRONMENTGRASS2SCALED = pygame.transform.scale(self.ENVIRONMENTGRASS2, (self.ENVIRONMENTGRASS2.get_width() // 2, self.ENVIRONMENTGRASS2.get_height() // 2))
        self.ENVIRONMENTGRASS3 = pygame.image.load("bin/assets/Environment/Grass/3.png")
        self.ENVIRONMENTGRASS3SCALED = pygame.transform.scale(self.ENVIRONMENTGRASS3, (self.ENVIRONMENTGRASS3.get_width() // 2, self.ENVIRONMENTGRASS3.get_height() // 2))
        self.ENVIRONMENTGRASS4 = pygame.image.load("bin/assets/Environment/Grass/4.png")
        self.ENVIRONMENTGRASS4SCALED = pygame.transform.scale(self.ENVIRONMENTGRASS4, (self.ENVIRONMENTGRASS4.get_width() // 2, self.ENVIRONMENTGRASS4.get_height() // 2))
        self.ENVIRONMENTGRASS5 = pygame.image.load("bin/assets/Environment/Grass/5.png")
        self.ENVIRONMENTGRASS5SCALED = pygame.transform.scale(self.ENVIRONMENTGRASS5, (self.ENVIRONMENTGRASS5.get_width() // 2, self.ENVIRONMENTGRASS5.get_height() // 2))
        self.ENVIRONMENTGRASS6 = pygame.image.load("bin/assets/Environment/Grass/6.png")
        self.ENVIRONMENTGRASS6SCALED = pygame.transform.scale(self.ENVIRONMENTGRASS6, (self.ENVIRONMENTGRASS6.get_width() // 2, self.ENVIRONMENTGRASS6.get_height() // 2))
        self.ENVIRONMENTGRASS7 = pygame.image.load("bin/assets/Environment/Grass/7.png")
        self.ENVIRONMENTGRASS7SCALED = pygame.transform.scale(self.ENVIRONMENTGRASS7, (self.ENVIRONMENTGRASS7.get_width() // 2, self.ENVIRONMENTGRASS7.get_height() // 2))
        self.ENVIRONMENTGRASS8 = pygame.image.load("bin/assets/Environment/Grass/8.png")
        self.ENVIRONMENTGRASS8SCALED = pygame.transform.scale(self.ENVIRONMENTGRASS8, (self.ENVIRONMENTGRASS8.get_width() // 2, self.ENVIRONMENTGRASS8.get_height() // 2))
        self.ENVIRONMENTGRASS9 = pygame.image.load("bin/assets/Environment/Grass/9.png")
        self.ENVIRONMENTGRASS9SCALED = pygame.transform.scale(self.ENVIRONMENTGRASS9, (self.ENVIRONMENTGRASS9.get_width() // 2, self.ENVIRONMENTGRASS9.get_height() // 2))
        self.ENVIRONMENTGRASS10 = pygame.image.load("bin/assets/Environment/Grass/10.png")
        self.ENVIRONMENTGRASS10SCALED = pygame.transform.scale(self.ENVIRONMENTGRASS10, (self.ENVIRONMENTGRASS10.get_width() // 2, self.ENVIRONMENTGRASS10.get_height() // 2))
        self.ENVIRONMENTGRASS11 = pygame.image.load("bin/assets/Environment/Grass/11.png")
        self.ENVIRONMENTGRASS11SCALED = pygame.transform.scale(self.ENVIRONMENTGRASS11, (self.ENVIRONMENTGRASS11.get_width() // 2, self.ENVIRONMENTGRASS11.get_height() // 2))
        self.ENVIRONMENTGRASS12 = pygame.image.load("bin/assets/Environment/Grass/12.png")
        self.ENVIRONMENTGRASS12SCALED = pygame.transform.scale(self.ENVIRONMENTGRASS12, (self.ENVIRONMENTGRASS12.get_width() // 2, self.ENVIRONMENTGRASS12.get_height() // 2))
        self.ENVIRONMENTGRASS13 = pygame.image.load("bin/assets/Environment/Grass/13.png")
        self.ENVIRONMENTGRASS13SCALED = pygame.transform.scale(self.ENVIRONMENTGRASS13, (self.ENVIRONMENTGRASS13.get_width() // 2, self.ENVIRONMENTGRASS13.get_height() // 2))
        self.ENVIRONMENTGRASS14 = pygame.image.load("bin/assets/Environment/Grass/14.png")
        self.ENVIRONMENTGRASS14SCALED = pygame.transform.scale(self.ENVIRONMENTGRASS14, (self.ENVIRONMENTGRASS14.get_width() // 2, self.ENVIRONMENTGRASS14.get_height() // 2))
        self.ENVIRONMENTGRASS15 = pygame.image.load("bin/assets/Environment/Grass/15.png")
        self.ENVIRONMENTGRASS15SCALED = pygame.transform.scale(self.ENVIRONMENTGRASS15, (self.ENVIRONMENTGRASS15.get_width() // 2, self.ENVIRONMENTGRASS15.get_height() // 2))
        self.ENVIRONMENTGRASS16 = pygame.image.load("bin/assets/Environment/Grass/16.png")
        self.ENVIRONMENTGRASS16SCALED = pygame.transform.scale(self.ENVIRONMENTGRASS16, (self.ENVIRONMENTGRASS16.get_width() // 2, self.ENVIRONMENTGRASS16.get_height() // 2))

        self.ENVIRONMENTGRASSSTONE1 = pygame.image.load("bin/assets/Environment/Grass/Stone/1.png")
        self.ENVIRONMENTGRASSSTONE1SCALED = pygame.transform.scale(self.ENVIRONMENTGRASSSTONE1, (self.ENVIRONMENTGRASSSTONE1.get_width() // 2, self.ENVIRONMENTGRASSSTONE1.get_height() // 2))
        self.ENVIRONMENTGRASSSTONE2 = pygame.image.load("bin/assets/Environment/Grass/Stone/2.png")
        self.ENVIRONMENTGRASSSTONE2SCALED = pygame.transform.scale(self.ENVIRONMENTGRASSSTONE2, (self.ENVIRONMENTGRASSSTONE2.get_width() // 2, self.ENVIRONMENTGRASSSTONE2.get_height() // 2))
        self.ENVIRONMENTGRASSSTONE3 = pygame.image.load("bin/assets/Environment/Grass/Stone/3.png")
        self.ENVIRONMENTGRASSSTONE3SCALED = pygame.transform.scale(self.ENVIRONMENTGRASSSTONE3, (self.ENVIRONMENTGRASSSTONE3.get_width() // 2, self.ENVIRONMENTGRASSSTONE3.get_height() // 2))
        self.ENVIRONMENTGRASSSTONE4 = pygame.image.load("bin/assets/Environment/Grass/Stone/4.png")
        self.ENVIRONMENTGRASSSTONE4SCALED = pygame.transform.scale(self.ENVIRONMENTGRASSSTONE4, (self.ENVIRONMENTGRASSSTONE4.get_width() // 2, self.ENVIRONMENTGRASSSTONE4.get_height() // 2))
        self.ENVIRONMENTGRASSSTONE5 = pygame.image.load("bin/assets/Environment/Grass/Stone/5.png")
        self.ENVIRONMENTGRASSSTONE5SCALED = pygame.transform.scale(self.ENVIRONMENTGRASSSTONE5, (self.ENVIRONMENTGRASSSTONE5.get_width() // 2, self.ENVIRONMENTGRASSSTONE5.get_height() // 2))
        self.ENVIRONMENTGRASSSTONE6 = pygame.image.load("bin/assets/Environment/Grass/Stone/6.png")
        self.ENVIRONMENTGRASSSTONE6SCALED = pygame.transform.scale(self.ENVIRONMENTGRASSSTONE6, (self.ENVIRONMENTGRASSSTONE6.get_width() // 2, self.ENVIRONMENTGRASSSTONE6.get_height() // 2))
        self.ENVIRONMENTGRASSSTONE7 = pygame.image.load("bin/assets/Environment/Grass/Stone/7.png")
        self.ENVIRONMENTGRASSSTONE7SCALED = pygame.transform.scale(self.ENVIRONMENTGRASSSTONE7, (self.ENVIRONMENTGRASSSTONE7.get_width() // 2, self.ENVIRONMENTGRASSSTONE7.get_height() // 2))
        self.ENVIRONMENTGRASSSTONE8 = pygame.image.load("bin/assets/Environment/Grass/Stone/8.png")
        self.ENVIRONMENTGRASSSTONE8SCALED = pygame.transform.scale(self.ENVIRONMENTGRASSSTONE8, (self.ENVIRONMENTGRASSSTONE8.get_width() // 2, self.ENVIRONMENTGRASSSTONE8.get_height() // 2))

        self.ENVIRONMENTGRASSLOGS1 = pygame.image.load("bin/assets/Environment/Grass/Logs/1.png")
        self.ENVIRONMENTGRASSLOGS1SCALED = pygame.transform.scale(self.ENVIRONMENTGRASSLOGS1, (self.ENVIRONMENTGRASSLOGS1.get_width() // 2, self.ENVIRONMENTGRASSLOGS1.get_height() // 2))
        self.ENVIRONMENTGRASSLOGS2 = pygame.image.load("bin/assets/Environment/Grass/Logs/2.png")
        self.ENVIRONMENTGRASSLOGS2SCALED = pygame.transform.scale(self.ENVIRONMENTGRASSLOGS2, (self.ENVIRONMENTGRASSLOGS2.get_width() // 2, self.ENVIRONMENTGRASSLOGS2.get_height() // 2))
        self.ENVIRONMENTGRASSLOGS3 = pygame.image.load("bin/assets/Environment/Grass/Logs/3.png")
        self.ENVIRONMENTGRASSLOGS3SCALED = pygame.transform.scale(self.ENVIRONMENTGRASSLOGS3, (self.ENVIRONMENTGRASSLOGS3.get_width() // 2, self.ENVIRONMENTGRASSLOGS3.get_height() // 2))
        self.ENVIRONMENTGRASSLOGS4 = pygame.image.load("bin/assets/Environment/Grass/Logs/4.png")
        self.ENVIRONMENTGRASSLOGS4SCALED = pygame.transform.scale(self.ENVIRONMENTGRASSLOGS4, (self.ENVIRONMENTGRASSLOGS4.get_width() // 2, self.ENVIRONMENTGRASSLOGS4.get_height() // 2))
        self.ENVIRONMENTGRASSLOGS5 = pygame.image.load("bin/assets/Environment/Grass/Logs/5.png")
        self.ENVIRONMENTGRASSLOGS5SCALED = pygame.transform.scale(self.ENVIRONMENTGRASSLOGS5, (self.ENVIRONMENTGRASSLOGS5.get_width() // 2, self.ENVIRONMENTGRASSLOGS5.get_height() // 2))

        self.ENVIRONMENTICE1 = pygame.image.load("bin/assets/Environment/Ice/1.png")
        self.ENVIRONMENTICE1SCALED = pygame.transform.scale(self.ENVIRONMENTICE1, (self.ENVIRONMENTICE1.get_width() // 2, self.ENVIRONMENTICE1.get_height() // 2))
        self.ENVIRONMENTICE2 = pygame.image.load("bin/assets/Environment/Ice/2.png")
        self.ENVIRONMENTICE2SCALED = pygame.transform.scale(self.ENVIRONMENTICE2, (self.ENVIRONMENTICE2.get_width() // 2, self.ENVIRONMENTICE2.get_height() // 2))
        self.ENVIRONMENTICE3 = pygame.image.load("bin/assets/Environment/Ice/3.png")
        self.ENVIRONMENTICE3SCALED = pygame.transform.scale(self.ENVIRONMENTICE3, (self.ENVIRONMENTICE3.get_width() // 2, self.ENVIRONMENTICE3.get_height() // 2))
        self.ENVIRONMENTICE4 = pygame.image.load("bin/assets/Environment/Ice/4.png")
        self.ENVIRONMENTICE4SCALED = pygame.transform.scale(self.ENVIRONMENTICE4, (self.ENVIRONMENTICE4.get_width() // 2, self.ENVIRONMENTICE4.get_height() // 2))
        self.ENVIRONMENTICE5 = pygame.image.load("bin/assets/Environment/Ice/5.png")
        self.ENVIRONMENTICE5SCALED = pygame.transform.scale(self.ENVIRONMENTICE5, (self.ENVIRONMENTICE5.get_width() // 2, self.ENVIRONMENTICE5.get_height() // 2))
        self.ENVIRONMENTICE6 = pygame.image.load("bin/assets/Environment/Ice/6.png")
        self.ENVIRONMENTICE6SCALED = pygame.transform.scale(self.ENVIRONMENTICE6, (self.ENVIRONMENTICE6.get_width() // 2, self.ENVIRONMENTICE6.get_height() // 2))
        self.ENVIRONMENTICE7 = pygame.image.load("bin/assets/Environment/Ice/7.png")
        self.ENVIRONMENTICE7SCALED = pygame.transform.scale(self.ENVIRONMENTICE7, (self.ENVIRONMENTICE7.get_width() // 2, self.ENVIRONMENTICE7.get_height() // 2))
        self.ENVIRONMENTICE8 = pygame.image.load("bin/assets/Environment/Ice/8.png")
        self.ENVIRONMENTICE8SCALED = pygame.transform.scale(self.ENVIRONMENTICE8, (self.ENVIRONMENTICE8.get_width() // 2, self.ENVIRONMENTICE8.get_height() // 2))
        self.ENVIRONMENTICE9 = pygame.image.load("bin/assets/Environment/Ice/9.png")
        self.ENVIRONMENTICE9SCALED = pygame.transform.scale(self.ENVIRONMENTICE9, (self.ENVIRONMENTICE9.get_width() // 2, self.ENVIRONMENTICE9.get_height() // 2))
        self.ENVIRONMENTICE10 = pygame.image.load("bin/assets/Environment/Ice/10.png")
        self.ENVIRONMENTICE10SCALED = pygame.transform.scale(self.ENVIRONMENTICE10, (self.ENVIRONMENTICE10.get_width() // 2, self.ENVIRONMENTICE10.get_height() // 2))

        self.ENVIRONMENTSTONE1 = pygame.image.load("bin/assets/Environment/Stone/1.png")
        self.ENVIRONMENTSTONE1SCALED = pygame.transform.scale(self.ENVIRONMENTSTONE1, (self.ENVIRONMENTSTONE1.get_width() // 2, self.ENVIRONMENTSTONE1.get_height() // 2))
        self.ENVIRONMENTSTONE2 = pygame.image.load("bin/assets/Environment/Stone/2.png")
        self.ENVIRONMENTSTONE2SCALED = pygame.transform.scale(self.ENVIRONMENTSTONE2, (self.ENVIRONMENTSTONE2.get_width() // 2, self.ENVIRONMENTSTONE2.get_height() // 2))
        self.ENVIRONMENTSTONE3 = pygame.image.load("bin/assets/Environment/Stone/3.png")
        self.ENVIRONMENTSTONE3SCALED = pygame.transform.scale(self.ENVIRONMENTSTONE3, (self.ENVIRONMENTSTONE3.get_width() // 2, self.ENVIRONMENTSTONE3.get_height() // 2))
        
        self.ENVIRONMENTSTONEDRY1 = pygame.image.load("bin/assets/Environment/StoneDry/1.png")
        self.ENVIRONMENTSTONEDRY1SCALED = pygame.transform.scale(self.ENVIRONMENTSTONEDRY1, (self.ENVIRONMENTSTONEDRY1.get_width() // 2, self.ENVIRONMENTSTONEDRY1.get_height() // 2))
        self.ENVIRONMENTSTONEDRY2 = pygame.image.load("bin/assets/Environment/StoneDry/2.png")
        self.ENVIRONMENTSTONEDRY2SCALED = pygame.transform.scale(self.ENVIRONMENTSTONEDRY2, (self.ENVIRONMENTSTONEDRY2.get_width() // 2, self.ENVIRONMENTSTONEDRY2.get_height() // 2))
        self.ENVIRONMENTSTONEDRY3 = pygame.image.load("bin/assets/Environment/StoneDry/3.png")
        self.ENVIRONMENTSTONEDRY3SCALED = pygame.transform.scale(self.ENVIRONMENTSTONEDRY3, (self.ENVIRONMENTSTONEDRY3.get_width() // 2, self.ENVIRONMENTSTONEDRY3.get_height() // 2))
        self.ENVIRONMENTSTONEDRY4 = pygame.image.load("bin/assets/Environment/StoneDry/4.png")
        self.ENVIRONMENTSTONEDRY4SCALED = pygame.transform.scale(self.ENVIRONMENTSTONEDRY4, (self.ENVIRONMENTSTONEDRY4.get_width() // 2, self.ENVIRONMENTSTONEDRY4.get_height() // 2))

        self.ENVIRONMENTSTONEWET1 = pygame.image.load("bin/assets/Environment/StoneWet/1.png")
        self.ENVIRONMENTSTONEWET1SCALED = pygame.transform.scale(self.ENVIRONMENTSTONEWET1, (self.ENVIRONMENTSTONEWET1.get_width() // 2, self.ENVIRONMENTSTONEWET1.get_height() // 2))
        self.ENVIRONMENTSTONEWET2 = pygame.image.load("bin/assets/Environment/StoneWet/2.png")
        self.ENVIRONMENTSTONEWET2SCALED = pygame.transform.scale(self.ENVIRONMENTSTONEWET2, (self.ENVIRONMENTSTONEWET2.get_width() // 2, self.ENVIRONMENTSTONEWET2.get_height() // 2))
        self.ENVIRONMENTSTONEWET3 = pygame.image.load("bin/assets/Environment/StoneWet/3.png")
        self.ENVIRONMENTSTONEWET3SCALED = pygame.transform.scale(self.ENVIRONMENTSTONEWET3, (self.ENVIRONMENTSTONEWET3.get_width() // 2, self.ENVIRONMENTSTONEWET3.get_height() // 2))
        self.ENVIRONMENTSTONEWET4 = pygame.image.load("bin/assets/Environment/StoneWet/4.png")
        self.ENVIRONMENTSTONEWET4SCALED = pygame.transform.scale(self.ENVIRONMENTSTONEWET4, (self.ENVIRONMENTSTONEWET4.get_width() // 2, self.ENVIRONMENTSTONEWET4.get_height() // 2))
        self.ENVIRONMENTSTONEWET5 = pygame.image.load("bin/assets/Environment/StoneWet/5.png")
        self.ENVIRONMENTSTONEWET5SCALED = pygame.transform.scale(self.ENVIRONMENTSTONEWET5, (self.ENVIRONMENTSTONEWET5.get_width() // 2, self.ENVIRONMENTSTONEWET5.get_height() // 2))
        self.ENVIRONMENTSTONEWET6 = pygame.image.load("bin/assets/Environment/StoneWet/6.png")
        self.ENVIRONMENTSTONEWET6SCALED = pygame.transform.scale(self.ENVIRONMENTSTONEWET6, (self.ENVIRONMENTSTONEWET6.get_width() // 2, self.ENVIRONMENTSTONEWET6.get_height() // 2))
        self.ENVIRONMENTSTONEWET7 = pygame.image.load("bin/assets/Environment/StoneWet/7.png")
        self.ENVIRONMENTSTONEWET7SCALED = pygame.transform.scale(self.ENVIRONMENTSTONEWET7, (self.ENVIRONMENTSTONEWET7.get_width() // 2, self.ENVIRONMENTSTONEWET7.get_height() // 2))
        self.ENVIRONMENTSTONEWET8 = pygame.image.load("bin/assets/Environment/StoneWet/8.png")
        self.ENVIRONMENTSTONEWET8SCALED = pygame.transform.scale(self.ENVIRONMENTSTONEWET8, (self.ENVIRONMENTSTONEWET8.get_width() // 2, self.ENVIRONMENTSTONEWET8.get_height() // 2))
        self.ENVIRONMENTSTONEWET9 = pygame.image.load("bin/assets/Environment/StoneWet/9.png")
        self.ENVIRONMENTSTONEWET9SCALED = pygame.transform.scale(self.ENVIRONMENTSTONEWET9, (self.ENVIRONMENTSTONEWET9.get_width() // 2, self.ENVIRONMENTSTONEWET9.get_height() // 2))
        self.ENVIRONMENTSTONEWET10 = pygame.image.load("bin/assets/Environment/StoneWet/10.png")
        self.ENVIRONMENTSTONEWET10SCALED = pygame.transform.scale(self.ENVIRONMENTSTONEWET10, (self.ENVIRONMENTSTONEWET10.get_width() // 2, self.ENVIRONMENTSTONEWET10.get_height() // 2))
        self.ENVIRONMENTSTONEWET11 = pygame.image.load("bin/assets/Environment/StoneWet/11.png")
        self.ENVIRONMENTSTONEWET11SCALED = pygame.transform.scale(self.ENVIRONMENTSTONEWET11, (self.ENVIRONMENTSTONEWET11.get_width() // 2, self.ENVIRONMENTSTONEWET11.get_height() // 2))
        self.ENVIRONMENTSTONEWET12 = pygame.image.load("bin/assets/Environment/StoneWet/12.png")
        self.ENVIRONMENTSTONEWET12SCALED = pygame.transform.scale(self.ENVIRONMENTSTONEWET12, (self.ENVIRONMENTSTONEWET12.get_width() // 2, self.ENVIRONMENTSTONEWET12.get_height() // 2))
        self.ENVIRONMENTSTONEWET13 = pygame.image.load("bin/assets/Environment/StoneWet/13.png")
        self.ENVIRONMENTSTONEWET13SCALED = pygame.transform.scale(self.ENVIRONMENTSTONEWET13, (self.ENVIRONMENTSTONEWET13.get_width() // 2, self.ENVIRONMENTSTONEWET13.get_height() // 2))
        self.ENVIRONMENTSTONEWET14 = pygame.image.load("bin/assets/Environment/StoneWet/14.png")
        self.ENVIRONMENTSTONEWET14SCALED = pygame.transform.scale(self.ENVIRONMENTSTONEWET14, (self.ENVIRONMENTSTONEWET14.get_width() // 2, self.ENVIRONMENTSTONEWET14.get_height() // 2))
        
        self.ENVIRONMENTWATER1 = pygame.image.load("bin/assets/Environment/Water/1.png")
        self.ENVIRONMENTWATER1SCALED = pygame.transform.scale(self.ENVIRONMENTWATER1, (self.ENVIRONMENTWATER1.get_width() // 2, self.ENVIRONMENTWATER1.get_height() // 2))
        self.ENVIRONMENTWATER2 = pygame.image.load("bin/assets/Environment/Water/2.png")
        self.ENVIRONMENTWATER2SCALED = pygame.transform.scale(self.ENVIRONMENTWATER2, (self.ENVIRONMENTWATER2.get_width() // 2, self.ENVIRONMENTWATER2.get_height() // 2))
        self.ENVIRONMENTWATER3 = pygame.image.load("bin/assets/Environment/Water/3.png")
        self.ENVIRONMENTWATER3SCALED = pygame.transform.scale(self.ENVIRONMENTWATER3, (self.ENVIRONMENTWATER3.get_width() // 2, self.ENVIRONMENTWATER3.get_height() // 2))
        self.ENVIRONMENTWATER4 = pygame.image.load("bin/assets/Environment/Water/4.png")
        self.ENVIRONMENTWATER4SCALED = pygame.transform.scale(self.ENVIRONMENTWATER4, (self.ENVIRONMENTWATER4.get_width() // 2, self.ENVIRONMENTWATER4.get_height() // 2))
        self.ENVIRONMENTWATER5 = pygame.image.load("bin/assets/Environment/Water/5.png")
        self.ENVIRONMENTWATER5SCALED = pygame.transform.scale(self.ENVIRONMENTWATER5, (self.ENVIRONMENTWATER5.get_width() // 2, self.ENVIRONMENTWATER5.get_height() // 2))
        self.ENVIRONMENTWATER6 = pygame.image.load("bin/assets/Environment/Water/6.png")
        self.ENVIRONMENTWATER6SCALED = pygame.transform.scale(self.ENVIRONMENTWATER6, (self.ENVIRONMENTWATER6.get_width() // 2, self.ENVIRONMENTWATER6.get_height() // 2))
        self.ENVIRONMENTWATER7 = pygame.image.load("bin/assets/Environment/Water/7.png")
        self.ENVIRONMENTWATER7SCALED = pygame.transform.scale(self.ENVIRONMENTWATER7, (self.ENVIRONMENTWATER7.get_width() // 2, self.ENVIRONMENTWATER7.get_height() // 2))
        self.ENVIRONMENTWATER8 = pygame.image.load("bin/assets/Environment/Water/8.png")
        self.ENVIRONMENTWATER8SCALED = pygame.transform.scale(self.ENVIRONMENTWATER8, (self.ENVIRONMENTWATER8.get_width() // 2, self.ENVIRONMENTWATER8.get_height() // 2))
        self.ENVIRONMENTWATER9 = pygame.image.load("bin/assets/Environment/Water/9.png")
        self.ENVIRONMENTWATER9SCALED = pygame.transform.scale(self.ENVIRONMENTWATER9, (self.ENVIRONMENTWATER9.get_width() // 2, self.ENVIRONMENTWATER9.get_height() // 2))
        self.ENVIRONMENTWATER10 = pygame.image.load("bin/assets/Environment/Water/10.png")
        self.ENVIRONMENTWATER10SCALED = pygame.transform.scale(self.ENVIRONMENTWATER10, (self.ENVIRONMENTWATER10.get_width() // 2, self.ENVIRONMENTWATER10.get_height() // 2))
        self.ENVIRONMENTWATER11 = pygame.image.load("bin/assets/Environment/Water/11.png")
        self.ENVIRONMENTWATER11SCALED = pygame.transform.scale(self.ENVIRONMENTWATER11, (self.ENVIRONMENTWATER11.get_width() // 2, self.ENVIRONMENTWATER11.get_height() // 2))
        self.ENVIRONMENTWATER12 = pygame.image.load("bin/assets/Environment/Water/12.png")
        self.ENVIRONMENTWATER12SCALED = pygame.transform.scale(self.ENVIRONMENTWATER12, (self.ENVIRONMENTWATER12.get_width() // 2, self.ENVIRONMENTWATER12.get_height() // 2))
        self.ENVIRONMENTWATER13 = pygame.image.load("bin/assets/Environment/Water/13.png")
        self.ENVIRONMENTWATER13SCALED = pygame.transform.scale(self.ENVIRONMENTWATER13, (self.ENVIRONMENTWATER13.get_width() // 2, self.ENVIRONMENTWATER13.get_height() // 2))
        self.ENVIRONMENTWATER14 = pygame.image.load("bin/assets/Environment/Water/14.png")
        self.ENVIRONMENTWATER14SCALED = pygame.transform.scale(self.ENVIRONMENTWATER14, (self.ENVIRONMENTWATER14.get_width() // 2, self.ENVIRONMENTWATER14.get_height() // 2))
        self.ENVIRONMENTWATER15 = pygame.image.load("bin/assets/Environment/Water/15.png")
        self.ENVIRONMENTWATER15SCALED = pygame.transform.scale(self.ENVIRONMENTWATER15, (self.ENVIRONMENTWATER15.get_width() // 2, self.ENVIRONMENTWATER15.get_height() // 2))
        self.ENVIRONMENTWATER16 = pygame.image.load("bin/assets/Environment/Water/16.png")
        self.ENVIRONMENTWATER16SCALED = pygame.transform.scale(self.ENVIRONMENTWATER16, (self.ENVIRONMENTWATER16.get_width() // 2, self.ENVIRONMENTWATER16.get_height() // 2))
        self.ENVIRONMENTWATER17 = pygame.image.load("bin/assets/Environment/Water/17.png")
        self.ENVIRONMENTWATER17SCALED = pygame.transform.scale(self.ENVIRONMENTWATER17, (self.ENVIRONMENTWATER17.get_width() // 2, self.ENVIRONMENTWATER17.get_height() // 2))
        self.ENVIRONMENTWATER18 = pygame.image.load("bin/assets/Environment/Water/18.png")
        self.ENVIRONMENTWATER18SCALED = pygame.transform.scale(self.ENVIRONMENTWATER18, (self.ENVIRONMENTWATER18.get_width() // 2, self.ENVIRONMENTWATER18.get_height() // 2))
        self.ENVIRONMENTWATER19 = pygame.image.load("bin/assets/Environment/Water/19.png")
        self.ENVIRONMENTWATER19SCALED = pygame.transform.scale(self.ENVIRONMENTWATER19, (self.ENVIRONMENTWATER19.get_width() // 2, self.ENVIRONMENTWATER19.get_height() // 2))
####################################################################################################
    def RandomWorldGrass(self, GAMEINSTANCE):
            self.SCREENMID = pygame.Vector2(GAMEINSTANCE.SCREEN.get_width() / 2, GAMEINSTANCE.SCREEN.get_height() / 2)
            self.MAXROWS = int (self.SCREENMID.y/128)*8
            self.MAXTILES = int (self.SCREENMID.x/128)*2
            self.SURFACE = pygame.Surface((self.MAXTILES * 128, self.MAXROWS * 128))
            self.SCALEDIMAGETILEGRASS = [
                self.ENVIRONMENTGRASS1SCALED, self.ENVIRONMENTGRASS2SCALED,
                self.ENVIRONMENTGRASS3SCALED, self.ENVIRONMENTGRASS4SCALED,
                self.ENVIRONMENTGRASS5SCALED, self.ENVIRONMENTGRASS6SCALED,
                self.ENVIRONMENTGRASS7SCALED, self.ENVIRONMENTGRASS8SCALED,
                self.ENVIRONMENTGRASS9SCALED, self.ENVIRONMENTGRASS10SCALED,
                self.ENVIRONMENTGRASS11SCALED, self.ENVIRONMENTGRASS12SCALED,
                self.ENVIRONMENTGRASS13SCALED, self.ENVIRONMENTGRASS14SCALED,
                self.ENVIRONMENTGRASS15SCALED, self.ENVIRONMENTGRASS16SCALED
            ]
            for row in range(-2,self.MAXROWS):
                for col in range(-1,self.MAXTILES):
                    offset = 64 if row % 2 == 1 else 0
                    x = col * 128 + offset
                    y = row * 32
                    randomScaledTileImageGrass = random.choice(self.SCALEDIMAGETILEGRASS)
                    self.SURFACE.blit(randomScaledTileImageGrass, (x,y))
            return self.SURFACE
####################################################################################################