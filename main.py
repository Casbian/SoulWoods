###########################################################################################
#MIT License                                                                              
#Copyright (c) 2024 Casbian

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
###########################################################################################

# IMPORTED CLASSES // FUNCTIONS // VARIABLES // CONSTANTS
import engine           #Engine for the Game
import tkinter as tk    #"Tkinter" GUI Class native to Python for some positional Args
import threading

###########################################################################################

def Main():
    def PlayerMoveUP(event):
        nonlocal PLAYERDIRECTION
        nonlocal ThreadAnimationRUNRIGHT
        nonlocal ThreadAnimationRUNLEFT
        nonlocal IDLE
        IDLE = 0
        WORLD.CANVAS.move("PLAYER",0,-10)
        if PLAYERDIRECTION == 1:
            if not ThreadAnimationRUNRIGHT or not ThreadAnimationRUNRIGHT.is_alive():
                ThreadAnimationRUNRIGHT = threading.Thread(target=PlayerAnimationRUNRIGHT)
                ThreadAnimationRUNRIGHT.start()
            else:
                pass
        elif PLAYERDIRECTION == 0:
            if not ThreadAnimationRUNLEFT or not ThreadAnimationRUNLEFT.is_alive():
                ThreadAnimationRUNLEFT = threading.Thread(target=PlayerAnimationRUNLEFT)
                ThreadAnimationRUNLEFT.start()
            else:
                pass
        else:
            pass  
         
    def PlayerMoveDOWN(event):
        nonlocal PLAYERDIRECTION
        nonlocal ThreadAnimationRUNRIGHT
        nonlocal ThreadAnimationRUNLEFT
        nonlocal IDLE
        IDLE = 0
        WORLD.CANVAS.move("PLAYER",0,10)
        if PLAYERDIRECTION == 1:
            if not ThreadAnimationRUNRIGHT or not ThreadAnimationRUNRIGHT.is_alive():
                ThreadAnimationRUNRIGHT = threading.Thread(target=PlayerAnimationRUNRIGHT)
                ThreadAnimationRUNRIGHT.start()
            else:
                pass
        elif PLAYERDIRECTION == 0:
            if not ThreadAnimationRUNLEFT or not ThreadAnimationRUNLEFT.is_alive():
                ThreadAnimationRUNLEFT = threading.Thread(target=PlayerAnimationRUNLEFT)
                ThreadAnimationRUNLEFT.start()
            else:
                pass
        else:
            pass
        
    def PlayerMoveRIGHT(event):
        nonlocal PLAYERDIRECTION
        nonlocal IDLE
        IDLE = 0
        nonlocal ThreadAnimationRUNRIGHT
        WORLD.CANVAS.move("PLAYER",10,0)
        PLAYERDIRECTION = int (1)
        if not ThreadAnimationRUNRIGHT or not ThreadAnimationRUNRIGHT.is_alive():
            ThreadAnimationRUNRIGHT = threading.Thread(target=PlayerAnimationRUNRIGHT)
            ThreadAnimationRUNRIGHT.start()
        else:
            pass
        
    def PlayerMoveLEFT(event):
        nonlocal PLAYERDIRECTION
        nonlocal IDLE
        IDLE = 0
        nonlocal ThreadAnimationRUNLEFT
        WORLD.CANVAS.move("PLAYER",-10,0)
        PLAYERDIRECTION = int (0)
        if not ThreadAnimationRUNLEFT or not ThreadAnimationRUNLEFT.is_alive():
            ThreadAnimationRUNLEFT = threading.Thread(target=PlayerAnimationRUNLEFT)
            ThreadAnimationRUNLEFT.start()
        else:
            pass
    
    def PlayerMoveJUMP(event):
        nonlocal PLAYERDIRECTION
        nonlocal ThreadAnimationJUMPRIGHT
        nonlocal ThreadAnimationJUMPLEFT
        nonlocal IDLE
        IDLE = 0
        if PLAYERDIRECTION == 1:
            if not ThreadAnimationJUMPRIGHT or not ThreadAnimationJUMPRIGHT.is_alive():
                ThreadAnimationJUMPRIGHT = threading.Thread(target=PlayerAnimationJUMPRIGHT)
                ThreadAnimationJUMPRIGHT.start()
            else:
                pass
        elif PLAYERDIRECTION == 0:
            if not ThreadAnimationJUMPLEFT or not ThreadAnimationJUMPLEFT.is_alive():
                ThreadAnimationJUMPLEFT = threading.Thread(target=PlayerAnimationJUMPLEFT)
                ThreadAnimationJUMPLEFT.start()
            else:
                pass
            
    def PlayerAnimationIDLERIGHT():
        nonlocal PLAYERDIRECTION
        nonlocal IDLE
        nonlocal JUMP
        if PLAYERDIRECTION != 1:
            pass
        else:
            if IDLE == 0:
                pass
            else:
                if JUMP == 1:
                    pass
                else:
                    try:
                        threading.Event().wait(0.2)
                        WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.IDLERIGHT2SCALED)
                        if PLAYERDIRECTION != 1:
                            pass
                        else:
                            if IDLE == 0:
                                pass
                            else:
                                if JUMP == 1:
                                    pass
                                else:
                                    threading.Event().wait(0.2)
                                    WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.IDLERIGHT3SCALED)
                                    if PLAYERDIRECTION != 1:
                                        pass
                                    else:
                                        if IDLE == 0:
                                            pass
                                        else:
                                            if JUMP == 1:
                                                pass
                                            else:
                                                threading.Event().wait(0.2)
                                                WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.IDLERIGHT4SCALED)
                                                if PLAYERDIRECTION != 1:
                                                    pass
                                                else:
                                                    if IDLE == 0:
                                                        pass
                                                    else:
                                                        if JUMP == 1:
                                                            pass
                                                        else:
                                                            threading.Event().wait(0.2)
                                                            WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.IDLERIGHT5SCALED)
                                                            if PLAYERDIRECTION != 1:
                                                                pass
                                                            else: 
                                                                if IDLE == 0:
                                                                    pass
                                                                else:   
                                                                    if JUMP == 1:
                                                                        pass
                                                                    else:       
                                                                        threading.Event().wait(0.2)
                                                                        WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.IDLERIGHT6SCALED)
                                                                        if PLAYERDIRECTION != 1:
                                                                            pass
                                                                        else:
                                                                            if IDLE == 0:
                                                                                pass
                                                                            else:
                                                                                if JUMP == 1:
                                                                                    pass
                                                                                else:
                                                                                    threading.Event().wait(0.2)
                                                                                    WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.IDLERIGHT7SCALED)
                                                                                    if PLAYERDIRECTION != 1:
                                                                                        pass
                                                                                    else:
                                                                                        if IDLE == 0:
                                                                                            pass
                                                                                        else:
                                                                                            if JUMP == 1:
                                                                                                pass
                                                                                            else:
                                                                                                threading.Event().wait(0.2)
                                                                                                WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.IDLERIGHT8SCALED)
                                                                                                if PLAYERDIRECTION != 1:
                                                                                                            pass
                                                                                                else:
                                                                                                    if IDLE == 0:
                                                                                                        pass
                                                                                                    else:
                                                                                                        if JUMP == 1:
                                                                                                            pass
                                                                                                        else:
                                                                                                            threading.Event().wait(0.2)
                                                                                                            PlayerAnimationIDLERIGHT()
                    except RuntimeError as ERROR:
                        pass
                
    def PlayerAnimationIDLELEFT():
        nonlocal PLAYERDIRECTION
        nonlocal IDLE
        nonlocal JUMP
        if PLAYERDIRECTION != 0:
            pass
        else:
            if IDLE == 0:
                pass
            else:
                if JUMP == 1:
                    pass
                else:
                    try:
                        threading.Event().wait(0.2)
                        WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.IDLELEFT2SCALED)
                        if PLAYERDIRECTION != 0:
                            pass
                        else:
                            if IDLE == 0:
                                pass
                            else:
                                if JUMP == 1:
                                    pass
                                else:
                                    threading.Event().wait(0.2)
                                    WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.IDLELEFT3SCALED)
                                    if PLAYERDIRECTION != 0:
                                        pass
                                    else:
                                        if IDLE == 0:
                                            pass
                                        else:
                                            if JUMP == 1:
                                                pass
                                            else:
                                                threading.Event().wait(0.2)
                                                WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.IDLELEFT4SCALED)
                                                if PLAYERDIRECTION != 0:
                                                    pass
                                                else:
                                                    if IDLE == 0:
                                                        pass
                                                    else:
                                                        if JUMP == 1:
                                                            pass
                                                        else:
                                                            threading.Event().wait(0.2)
                                                            WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.IDLELEFT5SCALED)
                                                            if PLAYERDIRECTION != 0:
                                                                pass
                                                            else:
                                                                if IDLE == 0:
                                                                    pass
                                                                else:
                                                                    if JUMP == 1:
                                                                        pass
                                                                    else:
                                                                        threading.Event().wait(0.2)
                                                                        WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.IDLELEFT6SCALED)
                                                                        if PLAYERDIRECTION != 0:
                                                                            pass
                                                                        else:
                                                                            if IDLE == 0:
                                                                                pass
                                                                            else:
                                                                                if JUMP == 1:
                                                                                    pass
                                                                                else:
                                                                                    threading.Event().wait(0.2)
                                                                                    WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.IDLELEFT7SCALED)
                                                                                    if PLAYERDIRECTION != 0:
                                                                                        pass
                                                                                    else:
                                                                                        if IDLE == 0:
                                                                                            pass
                                                                                        else:
                                                                                            if JUMP == 1:
                                                                                                pass
                                                                                            else:
                                                                                                threading.Event().wait(0.2)
                                                                                                WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.IDLELEFT8SCALED)
                                                                                                if PLAYERDIRECTION != 0:
                                                                                                    pass
                                                                                                else:
                                                                                                    if IDLE == 0:
                                                                                                        pass
                                                                                                    else:
                                                                                                        if JUMP == 1:
                                                                                                            pass
                                                                                                        else:
                                                                                                            threading.Event().wait(0.2)
                                                                                                            PlayerAnimationIDLELEFT()
                    except RuntimeError as ERROR:
                        pass
      
    def PlayerAnimationRUNRIGHT():
        nonlocal PLAYERDIRECTION
        nonlocal IDLE
        nonlocal JUMP
        if PLAYERDIRECTION != 1:
            pass
        else:
            if IDLE == 1:
                PlayerAnimationIDLERIGHT()
            else:
                if JUMP == 1:
                    pass
                else:
                    try:
                        threading.Event().wait(0.1)
                        WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.RUNRIGHT1SCALED)
                        if PLAYERDIRECTION != 1:
                            pass
                        else:
                            if IDLE == 1:
                                PlayerAnimationIDLERIGHT()
                            else:
                                if JUMP == 1:
                                    pass
                                else:
                                    threading.Event().wait(0.1)
                                    WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.RUNRIGHT2SCALED)
                                    if PLAYERDIRECTION != 1:
                                        pass
                                    else:
                                        if IDLE == 1:
                                            PlayerAnimationIDLERIGHT()
                                        else:
                                            if JUMP == 1:
                                                pass
                                            else:
                                                threading.Event().wait(0.1)
                                                WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.RUNRIGHT3SCALED)
                                                if PLAYERDIRECTION != 1:
                                                    pass
                                                else:
                                                    if IDLE == 1:
                                                        PlayerAnimationIDLERIGHT()
                                                    else:
                                                        if JUMP == 1:
                                                            pass
                                                        else:
                                                            threading.Event().wait(0.1)
                                                            WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.RUNRIGHT4SCALED)
                                                            if PLAYERDIRECTION != 1:
                                                                pass
                                                            else:  
                                                                if IDLE == 1:
                                                                    PlayerAnimationIDLERIGHT()
                                                                else:  
                                                                    if JUMP == 1:
                                                                        pass
                                                                    else:       
                                                                        threading.Event().wait(0.1)
                                                                        WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.RUNRIGHT6SCALED)
                                                                        if PLAYERDIRECTION != 1:
                                                                            pass
                                                                        else:
                                                                            if IDLE == 1:
                                                                                PlayerAnimationIDLERIGHT()
                                                                            else:
                                                                                if JUMP == 1:
                                                                                    pass
                                                                                else:
                                                                                    threading.Event().wait(0.1)
                                                                                    WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.RUNRIGHT7SCALED)
                                                                                    if PLAYERDIRECTION != 1:
                                                                                        pass
                                                                                    else:
                                                                                        if IDLE == 1:
                                                                                            PlayerAnimationIDLERIGHT()
                                                                                        else:
                                                                                            if JUMP == 1:
                                                                                                pass
                                                                                            else:
                                                                                                threading.Event().wait(0.1)
                                                                                                WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.RUNRIGHT8SCALED)
                                                                                                if PLAYERDIRECTION != 1:
                                                                                                    pass
                                                                                                else:
                                                                                                    if IDLE == 1:
                                                                                                        PlayerAnimationIDLERIGHT()
                                                                                                    else:
                                                                                                        if JUMP == 1:
                                                                                                            pass
                                                                                                        else:
                                                                                                            threading.Event().wait(0.1)
                                                                                                            PlayerAnimationRUNRIGHT()
                                                
                    except RuntimeError as ERROR:
                        pass  
        
    def PlayerAnimationRUNLEFT():
        nonlocal PLAYERDIRECTION
        nonlocal IDLE
        nonlocal JUMP
        if PLAYERDIRECTION != 0:
            pass
        else:
            if IDLE == 1:
                PlayerAnimationIDLELEFT()
            else:
                try:
                    if JUMP == 1:
                        pass
                    else:
                        threading.Event().wait(0.1)
                        WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.RUNLEFT1SCALED)
                        if PLAYERDIRECTION != 0:
                            pass
                        else:
                            if IDLE == 1:
                                PlayerAnimationIDLELEFT()
                            else:
                                if JUMP == 1:
                                    pass
                                else:
                                    threading.Event().wait(0.1)
                                    WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.RUNLEFT2SCALED)
                                    if PLAYERDIRECTION != 0:
                                        pass
                                    else:
                                        if IDLE == 1:
                                            PlayerAnimationIDLELEFT()
                                        else:
                                            if JUMP == 1:
                                                pass
                                            else:
                                                threading.Event().wait(0.1)
                                                WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.RUNLEFT3SCALED)
                                                if PLAYERDIRECTION != 0:
                                                    pass
                                                else:
                                                    if IDLE == 1:
                                                        PlayerAnimationIDLELEFT()
                                                    else:
                                                        if JUMP == 1:
                                                            pass
                                                        else:
                                                            threading.Event().wait(0.1)
                                                            WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.RUNLEFT4SCALED)
                                                            if PLAYERDIRECTION != 0:
                                                                pass
                                                            else:
                                                                if IDLE == 1:
                                                                    PlayerAnimationIDLELEFT()
                                                                else:
                                                                    if JUMP == 1:
                                                                        pass
                                                                    else:
                                                                        threading.Event().wait(0.1)
                                                                        WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.RUNLEFT5SCALED)
                                                                        if PLAYERDIRECTION != 0:
                                                                            pass
                                                                        else:
                                                                            if IDLE == 1:
                                                                                PlayerAnimationIDLELEFT()
                                                                            else:
                                                                                if JUMP == 1:
                                                                                    pass
                                                                                else:
                                                                                    threading.Event().wait(0.1)
                                                                                    WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.RUNLEFT6SCALED)
                                                                                    if PLAYERDIRECTION != 0:
                                                                                        pass
                                                                                    else:
                                                                                        if IDLE == 1:
                                                                                            PlayerAnimationIDLELEFT()
                                                                                        else:
                                                                                            if JUMP == 1:
                                                                                                pass
                                                                                            else:
                                                                                                threading.Event().wait(0.1)
                                                                                                WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.RUNLEFT7SCALED)
                                                                                                if PLAYERDIRECTION != 0:
                                                                                                    pass
                                                                                                else:
                                                                                                    if IDLE == 1:
                                                                                                        PlayerAnimationIDLELEFT()
                                                                                                    else:
                                                                                                        if JUMP == 1:
                                                                                                            pass
                                                                                                        else:
                                                                                                            threading.Event().wait(0.1)
                                                                                                            WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.RUNLEFT8SCALED)
                                                                                                            if PLAYERDIRECTION != 0:
                                                                                                                pass
                                                                                                            else:
                                                                                                                if IDLE == 1:
                                                                                                                    PlayerAnimationIDLELEFT()
                                                                                                                else:
                                                                                                                    if JUMP == 1:
                                                                                                                        pass
                                                                                                                    else:
                                                                                                                        threading.Event().wait(0.1)
                                                                                                                        PlayerAnimationRUNLEFT()
                except RuntimeError as ERROR:
                    pass
    
    def PlayerAnimationJUMPRIGHT():
        nonlocal JUMP
        JUMP = 1
        threading.Event().wait(0.1)
        WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.JUMPRIGHT1SCALED)
        threading.Event().wait(0.1)
        WORLD.CANVAS.move("PLAYER",20,-20)
        WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.JUMPRIGHT2SCALED)
        threading.Event().wait(0.1)
        WORLD.CANVAS.move("PLAYER",20,-20)
        WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.JUMPRIGHT3SCALED)
        threading.Event().wait(0.1)
        WORLD.CANVAS.move("PLAYER",20,-20)
        WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.JUMPRIGHT4SCALED)
        threading.Event().wait(0.1)
        WORLD.CANVAS.move("PLAYER",10,-10)
        WORLD.CANVAS.move("PLAYER",0,10)
        WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.JUMPRIGHT5SCALED)
        threading.Event().wait(0.1)
        WORLD.CANVAS.move("PLAYER",20,20)
        WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.JUMPRIGHT6SCALED)
        threading.Event().wait(0.1)
        WORLD.CANVAS.move("PLAYER",20,20)
        WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.JUMPRIGHT7SCALED)
        threading.Event().wait(0.1)
        WORLD.CANVAS.move("PLAYER",20,20)
        WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.JUMPRIGHT8SCALED)
        threading.Event().wait(0.1)
        WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.IDLERIGHT1SCALED)
        threading.Event().wait(0.1)
        JUMP = 0
        PlayerAnimationIDLERIGHT()
        
    def PlayerAnimationJUMPLEFT():
        nonlocal JUMP
        JUMP = 1
        threading.Event().wait(0.1)
        WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.JUMPLEFT1SCALED)
        threading.Event().wait(0.1)
        WORLD.CANVAS.move("PLAYER",-20,-20)
        WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.JUMPLEFT2SCALED)
        threading.Event().wait(0.1)
        WORLD.CANVAS.move("PLAYER",-20,-20)
        WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.JUMPLEFT3SCALED)
        threading.Event().wait(0.1)
        WORLD.CANVAS.move("PLAYER",-20,-20)
        WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.JUMPLEFT4SCALED)
        threading.Event().wait(0.1)
        WORLD.CANVAS.move("PLAYER",-10,-10)
        WORLD.CANVAS.move("PLAYER",0,10)
        WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.JUMPLEFT5SCALED)
        threading.Event().wait(0.1)
        WORLD.CANVAS.move("PLAYER",-20,20)
        WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.JUMPLEFT6SCALED)
        threading.Event().wait(0.1)
        WORLD.CANVAS.move("PLAYER",-20,20)
        WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.JUMPLEFT7SCALED)
        threading.Event().wait(0.1)
        WORLD.CANVAS.move("PLAYER",-20,20)
        WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.JUMPLEFT8SCALED)
        threading.Event().wait(0.1)
        WORLD.CANVAS.itemconfig("PLAYER",image=PLAYER.IDLELEFT1SCALED)
        threading.Event().wait(0.1)
        JUMP = 0
        PlayerAnimationIDLELEFT()
        
    def KeyRelease(event):
        nonlocal IDLE
        if event.keysym == 'a':
            IDLE = 1
        if event.keysym == 'A':
            IDLE = 1
        if event.keysym == 's':
            IDLE = 1
        if event.keysym == 'S':
            IDLE = 1
        if event.keysym == 'd':
            IDLE = 1
        if event.keysym == 'D':
            IDLE = 1
        if event.keysym == 'w':
            IDLE = 1
        if event.keysym == 'W':
            IDLE = 1
        if event.keysym == 'space':
            IDLE = 1
        
    GAMEINSTANCE = engine.GAME()
    WORLD = engine.WORLD(GAMEINSTANCE)
    SOULWOODS = engine.SOULWOODS()
    WORLD.CANVAS.create_image(640,512,image=SOULWOODS.TITLEARTSCALED,anchor=tk.CENTER,tags="WORLD")
    PLAYER = engine.PLAYER(GAMEINSTANCE)
    WORLD.CANVAS.itemconfig("WORLD",image=WORLD.ENVIRONMENTEMPTYSCALED)
    WORLD.RandomWorldGrass(GAMEINSTANCE)
    
    
    WORLD.CANVAS.create_image(540,512,image=PLAYER.IDLERIGHT1SCALED,anchor=tk.CENTER,tags="PLAYER")
    IDLE = int (1)
    JUMP = int (0)
    PLAYERDIRECTION = None
    PLAYERALIVEFLAG = False
    ThreadAnimationRUNRIGHT = None
    ThreadAnimationRUNLEFT = None
    ThreadAnimationJUMPRIGHT = None
    ThreadAnimationJUMPLEFT = None
    
    
    
    GAMEINSTANCE.GAME.bind('<w>', PlayerMoveUP)
    GAMEINSTANCE.GAME.bind('<a>', lambda event: PlayerMoveLEFT(event))
    GAMEINSTANCE.GAME.bind('<s>', PlayerMoveDOWN)
    GAMEINSTANCE.GAME.bind('<d>', lambda event: PlayerMoveRIGHT(event))
    GAMEINSTANCE.GAME.bind('<W>', PlayerMoveUP)
    GAMEINSTANCE.GAME.bind('<A>', lambda event: PlayerMoveLEFT(event))
    GAMEINSTANCE.GAME.bind('<S>', PlayerMoveDOWN)
    GAMEINSTANCE.GAME.bind('<D>', lambda event: PlayerMoveRIGHT(event))
    GAMEINSTANCE.GAME.bind('<space>', lambda event: PlayerMoveJUMP(event))
    GAMEINSTANCE.GAME.bind_all('<KeyRelease>', KeyRelease)
        
        
    
    
    
    GAMEINSTANCE.StartGame()

Main()