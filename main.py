####################################################################################################
# MIT License
# 
# Copyright (c) 2024 Casbian
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
####################################################################################################
#IMPORTS
import engine       #Import of my Engine into the Programm
####################################################################################################
#START UP
GAMEINSTANCE = engine.GAME()                                    #Creating an Instance of the CLASS "GAME" from Engine
GAMEINSTANCE.Start()                                            #Starting the Instances Cycle
TITLE = engine.TITLE(GAMEINSTANCE)                              #Creating an Instance of the CLASS "TITLE" from Engine
del TITLE                                                       #Deleting Instance of the CLASS "TITLE" from Engine
TITLEMENU = engine.TITLEMENU(GAMEINSTANCE)                      #Creating an Instance of the CLASS "TITLEMENU" from Engine
del TITLEMENU                                                   #Deleting Instance of the CLASS "TITLEMENU" from Engine
####################################################################################################
#GAME LOOP REQUIRED VARIABLES START UP
GAMEWORLD = engine.WORLD()                                      #Creating an Instance of the CLASS "WORLD" from Engine 
CURRENTGAMEWORLDPNG = GAMEWORLD.RandomWorldGrass(GAMEINSTANCE)  #Creating random Location Variation on Assets to create PNG
del GAMEWORLD                                                   #TEMP DELETE SINCE WORLD SWAP LOGIC IS NOT THERE YET
PLAYER = engine.PLAYER()                                        #Creating an Instance of the CLASS "PLAYER" from Engine

FRAMECOUNTERNROMAL = 1
FRAMECOUNTERATTACK = 1
FRAMECOUNTERROLL = 1
PLAYERDIRECTION = 2 #"DIRECTION" VARIABLE // 1 left // 2 right
ROLLDIRECTION = 1
PLAYERRUNNING = None
PLAYERATTACKING = None
PLAYERATTACKINGCOMPLETE = None
PLAYERROLLING = None
PLAYERROLLINGCOMPLETE = None
SCREENMIDDLE = engine.pygame.Vector2(GAMEINSTANCE.SCREEN.get_width() / 2, GAMEINSTANCE.SCREEN.get_height() / 2)
PLAYINITIALPNGCENTER = PLAYER.IDLERIGHT1SCALED.get_rect()
PLAYINITIALPNGCENTER.center = SCREENMIDDLE



while GAMEINSTANCE.GAMERUNNING:
    for event in engine.pygame.event.get():
        if event.type == engine.pygame.QUIT: 
            GAMEINSTANCE.GAMERUNNING = False
            GAMEINSTANCE.Exit()     #Exit Point for Engine and Programm
        if event.type == engine.pygame.KEYUP:
            if event.key == engine.pygame.K_w or event.key == engine.pygame.K_a or event.key == engine.pygame.K_s or event.key == engine.pygame.K_d:
                PLAYERRUNNING = False
            

    GAMEINSTANCE.TICK = GAMEINSTANCE.CLOCK.tick(60) / 1000
    FRAMECOUNTERNROMAL += 1
    if FRAMECOUNTERNROMAL > 60:
        FRAMECOUNTERNROMAL = 1
    GAMEINSTANCE.SCREEN.blit(CURRENTGAMEWORLDPNG, (0,0))
    
    USERMOUSE = engine.pygame.mouse.get_pressed()
    if USERMOUSE[0] and not PLAYERROLLING:
        PLAYERATTACKING = True
    if not USERMOUSE[0] and PLAYERATTACKINGCOMPLETE:
        PLAYERATTACKING = False
    USERKEYBOARD = engine.pygame.key.get_pressed()
    if USERKEYBOARD[engine.pygame.K_w] and USERKEYBOARD[engine.pygame.K_a] and USERKEYBOARD[engine.pygame.K_d] and not PLAYERATTACKING and not PLAYERROLLING:
        PLAYERRUNNING = True
        ROLLDIRECTION = 3
        PLAYINITIALPNGCENTER.y -= 300 * GAMEINSTANCE.TICK
    if USERKEYBOARD[engine.pygame.K_s] and USERKEYBOARD[engine.pygame.K_a] and USERKEYBOARD[engine.pygame.K_d] and not PLAYERATTACKING and not PLAYERROLLING:
        PLAYERRUNNING = True
        ROLLDIRECTION = 4
        PLAYINITIALPNGCENTER.y += 300 * GAMEINSTANCE.TICK    
    if USERKEYBOARD[engine.pygame.K_w] and USERKEYBOARD[engine.pygame.K_a] and not USERKEYBOARD[engine.pygame.K_d] and not PLAYERATTACKING and not PLAYERROLLING:
        PLAYERRUNNING = True
        PLAYERDIRECTION = 1
        ROLLDIRECTION = 7
        PLAYINITIALPNGCENTER.x -= (300 / engine.math.sqrt(2)) * GAMEINSTANCE.TICK
        PLAYINITIALPNGCENTER.y -= (300 / engine.math.sqrt(2)) * GAMEINSTANCE.TICK
    if USERKEYBOARD[engine.pygame.K_w] and USERKEYBOARD[engine.pygame.K_d] and not USERKEYBOARD[engine.pygame.K_a] and not PLAYERATTACKING and not PLAYERROLLING:
        PLAYERRUNNING = True
        PLAYERDIRECTION = 2
        ROLLDIRECTION = 5
        PLAYINITIALPNGCENTER.x += (300 / engine.math.sqrt(2)) * GAMEINSTANCE.TICK
        PLAYINITIALPNGCENTER.y -= (300 / engine.math.sqrt(2)) * GAMEINSTANCE.TICK 
    if USERKEYBOARD[engine.pygame.K_s] and USERKEYBOARD[engine.pygame.K_a] and not USERKEYBOARD[engine.pygame.K_d] and not PLAYERATTACKING and not PLAYERROLLING:
        PLAYERRUNNING = True
        PLAYERDIRECTION = 1
        ROLLDIRECTION = 6
        PLAYINITIALPNGCENTER.x -= (300 / engine.math.sqrt(2)) * GAMEINSTANCE.TICK
        PLAYINITIALPNGCENTER.y += (300 / engine.math.sqrt(2)) * GAMEINSTANCE.TICK 
    if USERKEYBOARD[engine.pygame.K_s] and USERKEYBOARD[engine.pygame.K_d] and not USERKEYBOARD[engine.pygame.K_a] and not PLAYERATTACKING and not PLAYERROLLING:
        PLAYERRUNNING = True
        PLAYERDIRECTION = 2
        ROLLDIRECTION = 8
        PLAYINITIALPNGCENTER.x += (300 / engine.math.sqrt(2)) * GAMEINSTANCE.TICK
        PLAYINITIALPNGCENTER.y += (300 / engine.math.sqrt(2)) * GAMEINSTANCE.TICK              
    if USERKEYBOARD[engine.pygame.K_w] and not USERKEYBOARD[engine.pygame.K_a] and not USERKEYBOARD[engine.pygame.K_d] and not PLAYERATTACKING and not PLAYERROLLING:
        PLAYERRUNNING = True
        ROLLDIRECTION = 3
        PLAYINITIALPNGCENTER.y -= 300 * GAMEINSTANCE.TICK           
    if USERKEYBOARD[engine.pygame.K_a] and not USERKEYBOARD[engine.pygame.K_w] and not USERKEYBOARD[engine.pygame.K_s] and not PLAYERATTACKING and not PLAYERROLLING:
        PLAYERRUNNING = True
        PLAYERDIRECTION = 1
        ROLLDIRECTION = 1
        PLAYINITIALPNGCENTER.x -= 300 * GAMEINSTANCE.TICK
    if USERKEYBOARD[engine.pygame.K_s] and not USERKEYBOARD[engine.pygame.K_a] and not USERKEYBOARD[engine.pygame.K_d] and not PLAYERATTACKING and not PLAYERROLLING:
        PLAYERRUNNING = True
        ROLLDIRECTION = 4
        PLAYINITIALPNGCENTER.y += 300 * GAMEINSTANCE.TICK
    if USERKEYBOARD[engine.pygame.K_d] and not USERKEYBOARD[engine.pygame.K_w] and not USERKEYBOARD[engine.pygame.K_s] and not PLAYERATTACKING and not PLAYERROLLING:
        PLAYERRUNNING = True
        PLAYERDIRECTION = 2
        ROLLDIRECTION = 2
        PLAYINITIALPNGCENTER.x += 300 * GAMEINSTANCE.TICK
    if USERKEYBOARD[engine.pygame.K_SPACE] and USERKEYBOARD[engine.pygame.K_w] and not USERKEYBOARD[engine.pygame.K_s] and not PLAYERATTACKING:
        PLAYERROLLING = True                  
    if USERKEYBOARD[engine.pygame.K_SPACE] and USERKEYBOARD[engine.pygame.K_s] and not USERKEYBOARD[engine.pygame.K_w] and not PLAYERATTACKING:
        PLAYERROLLING = True
    if USERKEYBOARD[engine.pygame.K_SPACE] and not USERKEYBOARD[engine.pygame.K_w] and not USERKEYBOARD[engine.pygame.K_s] and not PLAYERATTACKING:
        PLAYERROLLING = True
    if not USERKEYBOARD[engine.pygame.K_SPACE] and PLAYERROLLINGCOMPLETE:
        PLAYERROLLING = False
        
    if PLAYERDIRECTION == 1:
        if not PLAYERROLLING:
            if not PLAYERATTACKING:
                if not PLAYERRUNNING:
                    CURRENTIDLEPNG = getattr(PLAYER, "IDLELEFT{}SCALED".format(FRAMECOUNTERNROMAL))
                    GAMEINSTANCE.SCREEN.blit(CURRENTIDLEPNG, PLAYINITIALPNGCENTER)
                else:
                    CURRENTRUNNINGPNG = getattr(PLAYER, "RUNLEFT{}SCALED".format(FRAMECOUNTERNROMAL))
                    GAMEINSTANCE.SCREEN.blit(CURRENTRUNNINGPNG, PLAYINITIALPNGCENTER)
            else:
                PLAYERATTACKINGCOMPLETE = False
                FRAMECOUNTERATTACK += 2
                if FRAMECOUNTERATTACK > 60:
                    PLAYERATTACKINGCOMPLETE = True
                    FRAMECOUNTERATTACK = 1 
                CURRENTATTACKPNG = getattr(PLAYER, "ATTACKLEFT{}SCALED".format(FRAMECOUNTERATTACK))
                GAMEINSTANCE.SCREEN.blit(CURRENTATTACKPNG, PLAYINITIALPNGCENTER)
        else:
            PLAYERROLLINGCOMPLETE = False
            FRAMECOUNTERROLL += 2
            if FRAMECOUNTERROLL > 60:
                PLAYERROLLINGCOMPLETE = True
                FRAMECOUNTERROLL = 1 
            match ROLLDIRECTION:
                case 1:
                    PLAYINITIALPNGCENTER.x -= 300 * GAMEINSTANCE.TICK
                case 3:
                    PLAYINITIALPNGCENTER.y -= 300 * GAMEINSTANCE.TICK
                case 4:
                    PLAYINITIALPNGCENTER.y += 300 * GAMEINSTANCE.TICK
                case 6:
                    PLAYINITIALPNGCENTER.x -= (300 / engine.math.sqrt(2)) * GAMEINSTANCE.TICK
                    PLAYINITIALPNGCENTER.y += (300 / engine.math.sqrt(2)) * GAMEINSTANCE.TICK
                case 7:
                    PLAYINITIALPNGCENTER.x -= (300 / engine.math.sqrt(2)) * GAMEINSTANCE.TICK
                    PLAYINITIALPNGCENTER.y -= (300 / engine.math.sqrt(2)) * GAMEINSTANCE.TICK 
            CURRENTROLLPNG = getattr(PLAYER, "ROLLLEFT{}SCALED".format(FRAMECOUNTERROLL))
            GAMEINSTANCE.SCREEN.blit(CURRENTROLLPNG, PLAYINITIALPNGCENTER)                    
    if PLAYERDIRECTION == 2:
        if not PLAYERROLLING:
            if not PLAYERATTACKING:
                if not PLAYERRUNNING:
                    CURRENTIDLEPNG = getattr(PLAYER, "IDLERIGHT{}SCALED".format(FRAMECOUNTERNROMAL))
                    GAMEINSTANCE.SCREEN.blit(CURRENTIDLEPNG, PLAYINITIALPNGCENTER)
                else:
                    CURRENTRUNNINGPNG = getattr(PLAYER, "RUNRIGHT{}SCALED".format(FRAMECOUNTERNROMAL))
                    GAMEINSTANCE.SCREEN.blit(CURRENTRUNNINGPNG, PLAYINITIALPNGCENTER)
            else:
                PLAYERATTACKINGCOMPLETE = False
                FRAMECOUNTERATTACK += 2
                if FRAMECOUNTERATTACK > 60:
                    PLAYERATTACKINGCOMPLETE = True
                    FRAMECOUNTERATTACK = 1 
                CURRENTATTACKPNG = getattr(PLAYER, "ATTACKRIGHT{}SCALED".format(FRAMECOUNTERATTACK))
                GAMEINSTANCE.SCREEN.blit(CURRENTATTACKPNG, PLAYINITIALPNGCENTER)
        else:
            PLAYERROLLINGCOMPLETE = False
            FRAMECOUNTERROLL += 2
            if FRAMECOUNTERROLL > 60:
                PLAYERROLLINGCOMPLETE = True
                FRAMECOUNTERROLL = 1 
            match ROLLDIRECTION:
                case 2:
                    PLAYINITIALPNGCENTER.x += 300 * GAMEINSTANCE.TICK
                case 3:
                    PLAYINITIALPNGCENTER.y -= 300 * GAMEINSTANCE.TICK
                case 4:
                    PLAYINITIALPNGCENTER.y += 300 * GAMEINSTANCE.TICK
                case 5:
                    PLAYINITIALPNGCENTER.x += (300 / engine.math.sqrt(2)) * GAMEINSTANCE.TICK
                    PLAYINITIALPNGCENTER.y -= (300 / engine.math.sqrt(2)) * GAMEINSTANCE.TICK
                case 8:
                    PLAYINITIALPNGCENTER.x += (300 / engine.math.sqrt(2)) * GAMEINSTANCE.TICK
                    PLAYINITIALPNGCENTER.y += (300 / engine.math.sqrt(2)) * GAMEINSTANCE.TICK    
            CURRENTROLLPNG = getattr(PLAYER, "ROLLRIGHT{}SCALED".format(FRAMECOUNTERROLL))
            GAMEINSTANCE.SCREEN.blit(CURRENTROLLPNG, PLAYINITIALPNGCENTER)
            

    engine.pygame.display.flip()