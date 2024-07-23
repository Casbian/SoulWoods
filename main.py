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
PLAYERSTAMINA = 100
SCREENMIDDLE = engine.pygame.Vector2(GAMEINSTANCE.SCREEN.get_width() / 2, GAMEINSTANCE.SCREEN.get_height() / 2)
PLAYINITIALPNGCENTER = PLAYER.IDLERIGHT1SCALED.get_rect()
PLAYINITIALPNGCENTER.center = SCREENMIDDLE
HEALTHBARINITIALPNGCENTER = PLAYER.HEALTHBAR1SCALED.get_rect()
STAMINABARINITIALPNGCENTER = PLAYER.STAMINABAR1SCALED.get_rect()
MAGICABARINITIALPNGCENTER = PLAYER.MAGICABAR1SCALED.get_rect()
#GAME MAIN LOOP
while GAMEINSTANCE.GAMERUNNING:
    for event in engine.pygame.event.get():
        if event.type == engine.pygame.QUIT: 
            GAMEINSTANCE.GAMERUNNING = False
            GAMEINSTANCE.Exit()     #Exit Point for Engine and Programm
        if event.type == engine.pygame.KEYUP:
            if event.key == engine.pygame.K_w or event.key == engine.pygame.K_a or event.key == engine.pygame.K_s or event.key == engine.pygame.K_d:
                PLAYERRUNNING = False      
    #GAME TICK RATE
    GAMEINSTANCE.TICK = GAMEINSTANCE.CLOCK.tick(60) / 1000
    #Normal Frames
    FRAMECOUNTERNROMAL += 1
    if FRAMECOUNTERNROMAL > 60:
        FRAMECOUNTERNROMAL = 1
    #WORLD 
    GAMEINSTANCE.SCREEN.blit(CURRENTGAMEWORLDPNG, (0,0))
    #MOVEMENT
    #MOUSE and KEYBOARD EVENTS
    USERMOUSE = engine.pygame.mouse.get_pressed()
    if USERMOUSE[0] and not PLAYERROLLING and not PLAYERSTAMINA < 15:
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
    if USERKEYBOARD[engine.pygame.K_SPACE] and USERKEYBOARD[engine.pygame.K_w] and not USERKEYBOARD[engine.pygame.K_s] and not PLAYERATTACKING and not PLAYERSTAMINA < 30:
        PLAYERROLLING = True                  
    if USERKEYBOARD[engine.pygame.K_SPACE] and USERKEYBOARD[engine.pygame.K_s] and not USERKEYBOARD[engine.pygame.K_w] and not PLAYERATTACKING and not PLAYERSTAMINA < 30:
        PLAYERROLLING = True
    if USERKEYBOARD[engine.pygame.K_SPACE] and not USERKEYBOARD[engine.pygame.K_w] and not USERKEYBOARD[engine.pygame.K_s] and not PLAYERATTACKING and not PLAYERSTAMINA < 30:
        PLAYERROLLING = True
    if not USERKEYBOARD[engine.pygame.K_SPACE] and PLAYERROLLINGCOMPLETE:
        PLAYERROLLING = False
    #Animation Switch on DIRECTION and ROLLDIRECTION    
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
    #STATUS BARS
    #Positions
    HEALTHBARINITIALPNGCENTER.center = PLAYINITIALPNGCENTER.center
    STAMINABARINITIALPNGCENTER.center = PLAYINITIALPNGCENTER.center
    MAGICABARINITIALPNGCENTER.center = PLAYINITIALPNGCENTER.center
    HEALTHBARINITIALPNGCENTER.y -= 76
    STAMINABARINITIALPNGCENTER.y -= 64
    MAGICABARINITIALPNGCENTER.y -= 52
    #TEMP Health and Magica
    GAMEINSTANCE.SCREEN.blit(PLAYER.HEALTHBAR1SCALED, HEALTHBARINITIALPNGCENTER)
    GAMEINSTANCE.SCREEN.blit(PLAYER.MAGICABAR1SCALED, MAGICABARINITIALPNGCENTER)
    #PLAYER STAMINA
    #STAMINA Resets on min and max
    if PLAYERSTAMINA > 100:
        PLAYERSTAMINA = 100
    elif PLAYERSTAMINA < 0:
        PLAYERSTAMINA = 0
        #STOP ATTACK or ROLL
        PLAYERATTACKING = False
        PLAYERROLLING = False
    else:
        pass
        #STAMINA Recover Rate
        PLAYERSTAMINA += 8 * GAMEINSTANCE.TICK
    #CALULATE current STAMINA
    if PLAYERATTACKING:
        PLAYERSTAMINA -= 30 * GAMEINSTANCE.TICK
    if PLAYERROLLING:
        PLAYERSTAMINA -= 60 * GAMEINSTANCE.TICK
    #DISPLAY STAMINA Based on current STAMINA
    if PLAYERSTAMINA < 5:
        GAMEINSTANCE.SCREEN.blit(PLAYER.STAMINABAR20SCALED, STAMINABARINITIALPNGCENTER)
    if PLAYERSTAMINA >=5:
        GAMEINSTANCE.SCREEN.blit(PLAYER.STAMINABAR19SCALED, STAMINABARINITIALPNGCENTER)  
    if PLAYERSTAMINA >=10:
        GAMEINSTANCE.SCREEN.blit(PLAYER.STAMINABAR18SCALED, STAMINABARINITIALPNGCENTER) 
    if PLAYERSTAMINA >=15:
        GAMEINSTANCE.SCREEN.blit(PLAYER.STAMINABAR17SCALED, STAMINABARINITIALPNGCENTER)
    if PLAYERSTAMINA >=20:
        GAMEINSTANCE.SCREEN.blit(PLAYER.STAMINABAR16SCALED, STAMINABARINITIALPNGCENTER)
    if PLAYERSTAMINA >=25:
        GAMEINSTANCE.SCREEN.blit(PLAYER.STAMINABAR15SCALED, STAMINABARINITIALPNGCENTER)
    if PLAYERSTAMINA >=30:
        GAMEINSTANCE.SCREEN.blit(PLAYER.STAMINABAR14SCALED, STAMINABARINITIALPNGCENTER)
    if PLAYERSTAMINA >=35:
        GAMEINSTANCE.SCREEN.blit(PLAYER.STAMINABAR13SCALED, STAMINABARINITIALPNGCENTER)
    if PLAYERSTAMINA >=40:
        GAMEINSTANCE.SCREEN.blit(PLAYER.STAMINABAR12SCALED, STAMINABARINITIALPNGCENTER)
    if PLAYERSTAMINA >=45:
        GAMEINSTANCE.SCREEN.blit(PLAYER.STAMINABAR11SCALED, STAMINABARINITIALPNGCENTER)  
    if PLAYERSTAMINA >=50:
        GAMEINSTANCE.SCREEN.blit(PLAYER.STAMINABAR10SCALED, STAMINABARINITIALPNGCENTER) 
    if PLAYERSTAMINA >=55:
        GAMEINSTANCE.SCREEN.blit(PLAYER.STAMINABAR9SCALED, STAMINABARINITIALPNGCENTER)
    if PLAYERSTAMINA >=60:
        GAMEINSTANCE.SCREEN.blit(PLAYER.STAMINABAR8SCALED, STAMINABARINITIALPNGCENTER)
    if PLAYERSTAMINA >=65:
        GAMEINSTANCE.SCREEN.blit(PLAYER.STAMINABAR7SCALED, STAMINABARINITIALPNGCENTER)
    if PLAYERSTAMINA >=70:
        GAMEINSTANCE.SCREEN.blit(PLAYER.STAMINABAR6SCALED, STAMINABARINITIALPNGCENTER)
    if PLAYERSTAMINA >=75:
        GAMEINSTANCE.SCREEN.blit(PLAYER.STAMINABAR5SCALED, STAMINABARINITIALPNGCENTER)
    if PLAYERSTAMINA >=80:
        GAMEINSTANCE.SCREEN.blit(PLAYER.STAMINABAR4SCALED, STAMINABARINITIALPNGCENTER)
    if PLAYERSTAMINA >=85:
        GAMEINSTANCE.SCREEN.blit(PLAYER.STAMINABAR3SCALED, STAMINABARINITIALPNGCENTER)
    if PLAYERSTAMINA >=90:
        GAMEINSTANCE.SCREEN.blit(PLAYER.STAMINABAR2SCALED, STAMINABARINITIALPNGCENTER)  
    if PLAYERSTAMINA >=95:
        GAMEINSTANCE.SCREEN.blit(PLAYER.STAMINABAR1SCALED, STAMINABARINITIALPNGCENTER)       
    #BORDER and WORLD Logic
    if PLAYINITIALPNGCENTER.y < 0:
        PLAYINITIALPNGCENTER.y = 1024
        CURRENTGAMEWORLDPNG = GAMEWORLD.RandomWorldGrass(GAMEINSTANCE)
    if PLAYINITIALPNGCENTER.y > 1024:
        PLAYINITIALPNGCENTER.y = 0
        CURRENTGAMEWORLDPNG = GAMEWORLD.RandomWorldGrass(GAMEINSTANCE)
    if PLAYINITIALPNGCENTER.x < 0:
        PLAYINITIALPNGCENTER.x = 1280
        CURRENTGAMEWORLDPNG = GAMEWORLD.RandomWorldGrass(GAMEINSTANCE)
    if PLAYINITIALPNGCENTER.x > 1280:
        PLAYINITIALPNGCENTER.x = 0
        CURRENTGAMEWORLDPNG = GAMEWORLD.RandomWorldGrass(GAMEINSTANCE)
    engine.pygame.display.flip()