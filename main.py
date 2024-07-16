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
    
    GAMEINSTANCE = engine.GAME()
    WORLD = engine.WORLD(GAMEINSTANCE)
    SOULWOODS = engine.SOULWOODS()
    WORLD.CANVAS.create_image(640,512,image=SOULWOODS.TITLEARTSCALED,anchor=tk.CENTER,tags="WORLD")
    WORLD.CANVAS.itemconfig("WORLD",image=WORLD.ENVIRONMENTEMPTYSCALED)
    WORLD.RandomWorldGrass(GAMEINSTANCE)
    
    PLAYER = engine.PLAYER()
    MOVEMENT = engine.MOVEMENT()
    GAMEINSTANCE.GAME.protocol("WM_DELETE_WINDOW",lambda: GAMEINSTANCE.EXIT(MOVEMENT))
    
    WORLD.CANVAS.create_image(540,512,image=PLAYER.IDLERIGHT1SCALED,anchor=tk.CENTER,tags="PLAYER")
    MOVEMENT.UpdatePlayerThread(WORLD, PLAYER, GAMEINSTANCE)
    
    
    
    
    
    GAMEINSTANCE.GAME.bind('<w>', MOVEMENT.KeyPress)
    GAMEINSTANCE.GAME.bind('<a>', MOVEMENT.KeyPress)
    GAMEINSTANCE.GAME.bind('<s>', MOVEMENT.KeyPress)
    GAMEINSTANCE.GAME.bind('<d>', MOVEMENT.KeyPress)
    GAMEINSTANCE.GAME.bind('<W>', MOVEMENT.KeyPress)
    GAMEINSTANCE.GAME.bind('<A>', MOVEMENT.KeyPress)
    GAMEINSTANCE.GAME.bind('<S>', MOVEMENT.KeyPress)
    GAMEINSTANCE.GAME.bind('<D>', MOVEMENT.KeyPress)
    GAMEINSTANCE.GAME.bind('<space>', MOVEMENT.KeyPress)
    GAMEINSTANCE.GAME.bind_all('<KeyRelease>', MOVEMENT.KeyRelease)
        
    GAMEINSTANCE.StartGame()

Main()
