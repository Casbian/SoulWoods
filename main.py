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
import engine                                                   #Import of my Engine into the Programm
####################################################################################################
#START UP
GAMEINSTANCE = engine.GAME()                                    #Creating an Instance of the CLASS "GAME" from Engine
GAMEINSTANCE.Start()                                            #Starting the Instances Cycle
TITLE = engine.TITLE(GAMEINSTANCE)                             #Creating an Instance of the CLASS "TITLE" from Engine
del TITLE                                                      #Deleting Instance of the CLASS "TITLE" from Engine
TITLEMENU = engine.TITLEMENU(GAMEINSTANCE)                      #Creating an Instance of the CLASS "TITLEMENU" from Engine
del TITLEMENU                                                   #Deleting Instance of the CLASS "TITLEMENU" from Engine
####################################################################################################
#GAME LOOP REQUIRED VARIABLES START UP
GAMEWORLD = engine.WORLD()                                      #Creating an Instance of the CLASS "WORLD" from Engine 
CURRENTGAMEWORLDPNG = GAMEWORLD.RandomWorldGrass(GAMEINSTANCE)  #Creating random Location Variation on Assets to create World PNG
PLAYER = engine.PLAYER(GAMEINSTANCE)                            #Creating an Instance of the CLASS "PLAYER" from Engine
####################################################################################################
#GAME MAIN LOOP
while GAMEINSTANCE.GAMERUNNING:                                 #Setting GAME LOOP Requirement
    for event in engine.pygame.event.get():                     #Event Handling of the Windows Window
        if event.type == engine.pygame.QUIT:                    #Event "Close Window"
            GAMEINSTANCE.GAMERUNNING = False                    #Take away GAME LOOP Requirement
            GAMEINSTANCE.Exit()                                 #Calls the Programm Exit Point as Method from CLASS "GAME"
        if event.type == engine.pygame.KEYUP:                   #Event "Keyboard Key released"
            if event.key == engine.pygame.K_w:                  #Event Target Key "W"
                PLAYER.PLAYERRUNNING = False                    #Take away RUN ANIMATION Requirement
            if event.key == engine.pygame.K_a:                  #Event Target Key "A"
                PLAYER.PLAYERRUNNING = False                    #Take away RUN ANIMATION Requirement
            if event.key == engine.pygame.K_s:                  #Event Target Key "S"
                PLAYER.PLAYERRUNNING = False                    #Take away RUN ANIMATION Requirement
            if event.key == engine.pygame.K_d:                  #Event Target Key "D"
                PLAYER.PLAYERRUNNING = False                    #Take away RUN ANIMATION Requirement      
    GAMEINSTANCE.TICK = GAMEINSTANCE.CLOCK.tick(60) / 1000      #MAIN GAME TICK RATE (60 Frames (/1000 for Microseconds to Seconds) == 60 Frames/sec // The LOOP runs 60 Times/sec)
    GAMEINSTANCE.SCREEN.blit(CURRENTGAMEWORLDPNG, (0,0))        #PRINT "Current World PNG" to SCREEN BUFFER
    PLAYER.MOVEMENT(GAMEINSTANCE)                               #Calls the Player Movement as a Method from CLASS "PLAYER"
    if PLAYER.PLAYERPOSITION.y < -130:                                  #Setting ^ Border
        PLAYER.PLAYERPOSITION.y = 990                                   #Warp Point of Player
        CURRENTGAMEWORLDPNG = GAMEWORLD.RandomWorldGrass(GAMEINSTANCE)  #Creating random Location Variation on Assets to create new World PNG
    if PLAYER.PLAYERPOSITION.y > 990:                                   #Setting v Border
        PLAYER.PLAYERPOSITION.y = -130                                  #Warp Point of Player
        CURRENTGAMEWORLDPNG = GAMEWORLD.RandomWorldGrass(GAMEINSTANCE)  #Creating random Location Variation on Assets to create new World PNG
    if PLAYER.PLAYERPOSITION.x < -150:                                  #Setting < Border
        PLAYER.PLAYERPOSITION.x = 1180                                  #Warp Point of Player
        CURRENTGAMEWORLDPNG = GAMEWORLD.RandomWorldGrass(GAMEINSTANCE)  #Creating random Location Variation on Assets to create new World PNG
    if PLAYER.PLAYERPOSITION.x > 1180:                                  #Setting > Border
        PLAYER.PLAYERPOSITION.x = -150                                  #Warp Point of Player
        CURRENTGAMEWORLDPNG = GAMEWORLD.RandomWorldGrass(GAMEINSTANCE)  #Creating random Location Variation on Assets to create new World PNG   
    engine.pygame.display.flip()            #PRINT Everything from SCREEN BUFFER to SCREEN
####################################################################################################