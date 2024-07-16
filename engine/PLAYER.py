import tkinter as tk
import threading
class PLAYER:
    def __init__(self):
        self.IDLERIGHT1 = tk.PhotoImage(file="bin/assets/Player/IDLERIGHT/1.png")
        self.IDLERIGHT1SCALED = self.IDLERIGHT1.subsample(2,2)
        self.IDLERIGHT2 = tk.PhotoImage(file="bin/assets/Player/IDLERIGHT/2.png")
        self.IDLERIGHT2SCALED = self.IDLERIGHT2.subsample(2,2)
        self.IDLERIGHT3 = tk.PhotoImage(file="bin/assets/Player/IDLERIGHT/3.png")
        self.IDLERIGHT3SCALED = self.IDLERIGHT3.subsample(2,2)
        self.IDLERIGHT4 = tk.PhotoImage(file="bin/assets/Player/IDLERIGHT/4.png")
        self.IDLERIGHT4SCALED = self.IDLERIGHT4.subsample(2,2)
        self.IDLERIGHT5 = tk.PhotoImage(file="bin/assets/Player/IDLERIGHT/5.png")
        self.IDLERIGHT5SCALED = self.IDLERIGHT5.subsample(2,2)
        self.IDLERIGHT6 = tk.PhotoImage(file="bin/assets/Player/IDLERIGHT/6.png")
        self.IDLERIGHT6SCALED = self.IDLERIGHT6.subsample(2,2)
        self.IDLERIGHT7 = tk.PhotoImage(file="bin/assets/Player/IDLERIGHT/7.png")
        self.IDLERIGHT7SCALED = self.IDLERIGHT7.subsample(2,2)
        self.IDLERIGHT8 = tk.PhotoImage(file="bin/assets/Player/IDLERIGHT/8.png")
        self.IDLERIGHT8SCALED = self.IDLERIGHT8.subsample(2,2)
        
        self.IDLELEFT1 = tk.PhotoImage(file="bin/assets/Player/IDLELEFT/1.png")
        self.IDLELEFT1SCALED = self.IDLELEFT1.subsample(2,2)
        self.IDLELEFT2 = tk.PhotoImage(file="bin/assets/Player/IDLELEFT/2.png")
        self.IDLELEFT2SCALED = self.IDLELEFT2.subsample(2,2)
        self.IDLELEFT3 = tk.PhotoImage(file="bin/assets/Player/IDLELEFT/3.png")
        self.IDLELEFT3SCALED = self.IDLELEFT3.subsample(2,2)
        self.IDLELEFT4 = tk.PhotoImage(file="bin/assets/Player/IDLELEFT/4.png")
        self.IDLELEFT4SCALED = self.IDLELEFT4.subsample(2,2)
        self.IDLELEFT5 = tk.PhotoImage(file="bin/assets/Player/IDLELEFT/5.png")
        self.IDLELEFT5SCALED = self.IDLELEFT5.subsample(2,2)
        self.IDLELEFT6 = tk.PhotoImage(file="bin/assets/Player/IDLELEFT/6.png")
        self.IDLELEFT6SCALED = self.IDLELEFT6.subsample(2,2)
        self.IDLELEFT7 = tk.PhotoImage(file="bin/assets/Player/IDLELEFT/7.png")
        self.IDLELEFT7SCALED = self.IDLELEFT7.subsample(2,2)
        self.IDLELEFT8 = tk.PhotoImage(file="bin/assets/Player/IDLELEFT/8.png")
        self.IDLELEFT8SCALED = self.IDLELEFT8.subsample(2,2)
        
        self.RUNLEFT1 = tk.PhotoImage(file="bin/assets/Player/RUNLEFT/1.png")
        self.RUNLEFT1SCALED = self.RUNLEFT1.subsample(2, 2)
        self.RUNLEFT2 = tk.PhotoImage(file="bin/assets/Player/RUNLEFT/2.png")
        self.RUNLEFT2SCALED = self.RUNLEFT2.subsample(2, 2)
        self.RUNLEFT3 = tk.PhotoImage(file="bin/assets/Player/RUNLEFT/3.png")
        self.RUNLEFT3SCALED = self.RUNLEFT3.subsample(2, 2)
        self.RUNLEFT4 = tk.PhotoImage(file="bin/assets/Player/RUNLEFT/4.png")
        self.RUNLEFT4SCALED = self.RUNLEFT4.subsample(2, 2)
        self.RUNLEFT5 = tk.PhotoImage(file="bin/assets/Player/RUNLEFT/5.png")
        self.RUNLEFT5SCALED = self.RUNLEFT5.subsample(2, 2)
        self.RUNLEFT6 = tk.PhotoImage(file="bin/assets/Player/RUNLEFT/6.png")
        self.RUNLEFT6SCALED = self.RUNLEFT6.subsample(2, 2)
        self.RUNLEFT7 = tk.PhotoImage(file="bin/assets/Player/RUNLEFT/7.png")
        self.RUNLEFT7SCALED = self.RUNLEFT7.subsample(2, 2)
        self.RUNLEFT8 = tk.PhotoImage(file="bin/assets/Player/RUNLEFT/8.png")
        self.RUNLEFT8SCALED = self.RUNLEFT8.subsample(2, 2)

        self.RUNRIGHT1 = tk.PhotoImage(file="bin/assets/Player/RUNRIGHT/1.png")
        self.RUNRIGHT1SCALED = self.RUNRIGHT1.subsample(2, 2)
        self.RUNRIGHT2 = tk.PhotoImage(file="bin/assets/Player/RUNRIGHT/2.png")
        self.RUNRIGHT2SCALED = self.RUNRIGHT2.subsample(2, 2)
        self.RUNRIGHT3 = tk.PhotoImage(file="bin/assets/Player/RUNRIGHT/3.png")
        self.RUNRIGHT3SCALED = self.RUNRIGHT3.subsample(2, 2)
        self.RUNRIGHT4 = tk.PhotoImage(file="bin/assets/Player/RUNRIGHT/4.png")
        self.RUNRIGHT4SCALED = self.RUNRIGHT4.subsample(2, 2)
        self.RUNRIGHT5 = tk.PhotoImage(file="bin/assets/Player/RUNRIGHT/5.png")
        self.RUNRIGHT5SCALED = self.RUNRIGHT5.subsample(2, 2)
        self.RUNRIGHT6 = tk.PhotoImage(file="bin/assets/Player/RUNRIGHT/6.png")
        self.RUNRIGHT6SCALED = self.RUNRIGHT6.subsample(2, 2)
        self.RUNRIGHT7 = tk.PhotoImage(file="bin/assets/Player/RUNRIGHT/7.png")
        self.RUNRIGHT7SCALED = self.RUNRIGHT7.subsample(2, 2)
        self.RUNRIGHT8 = tk.PhotoImage(file="bin/assets/Player/RUNRIGHT/8.png")
        self.RUNRIGHT8SCALED = self.RUNRIGHT8.subsample(2, 2)
        
        self.JUMPLEFT1 = tk.PhotoImage(file="bin/assets/Player/JUMPLEFT/1.png")
        self.JUMPLEFT1SCALED = self.JUMPLEFT1.subsample(2, 2)
        self.JUMPLEFT2 = tk.PhotoImage(file="bin/assets/Player/JUMPLEFT/2.png")
        self.JUMPLEFT2SCALED = self.JUMPLEFT2.subsample(2, 2)
        self.JUMPLEFT3 = tk.PhotoImage(file="bin/assets/Player/JUMPLEFT/3.png")
        self.JUMPLEFT3SCALED = self.JUMPLEFT3.subsample(2, 2)
        self.JUMPLEFT4 = tk.PhotoImage(file="bin/assets/Player/JUMPLEFT/4.png")
        self.JUMPLEFT4SCALED = self.JUMPLEFT4.subsample(2, 2)
        self.JUMPLEFT5 = tk.PhotoImage(file="bin/assets/Player/JUMPLEFT/5.png")
        self.JUMPLEFT5SCALED = self.JUMPLEFT5.subsample(2, 2)
        self.JUMPLEFT6 = tk.PhotoImage(file="bin/assets/Player/JUMPLEFT/6.png")
        self.JUMPLEFT6SCALED = self.JUMPLEFT6.subsample(2, 2)
        self.JUMPLEFT7 = tk.PhotoImage(file="bin/assets/Player/JUMPLEFT/7.png")
        self.JUMPLEFT7SCALED = self.JUMPLEFT7.subsample(2, 2)
        self.JUMPLEFT8 = tk.PhotoImage(file="bin/assets/Player/JUMPLEFT/8.png")
        self.JUMPLEFT8SCALED = self.JUMPLEFT8.subsample(2, 2)

        self.JUMPRIGHT1 = tk.PhotoImage(file="bin/assets/Player/JUMPRIGHT/1.png")
        self.JUMPRIGHT1SCALED = self.JUMPRIGHT1.subsample(2, 2)
        self.JUMPRIGHT2 = tk.PhotoImage(file="bin/assets/Player/JUMPRIGHT/2.png")
        self.JUMPRIGHT2SCALED = self.JUMPRIGHT2.subsample(2, 2)
        self.JUMPRIGHT3 = tk.PhotoImage(file="bin/assets/Player/JUMPRIGHT/3.png")
        self.JUMPRIGHT3SCALED = self.JUMPRIGHT3.subsample(2, 2)
        self.JUMPRIGHT4 = tk.PhotoImage(file="bin/assets/Player/JUMPRIGHT/4.png")
        self.JUMPRIGHT4SCALED = self.JUMPRIGHT4.subsample(2, 2)
        self.JUMPRIGHT5 = tk.PhotoImage(file="bin/assets/Player/JUMPRIGHT/5.png")
        self.JUMPRIGHT5SCALED = self.JUMPRIGHT5.subsample(2, 2)
        self.JUMPRIGHT6 = tk.PhotoImage(file="bin/assets/Player/JUMPRIGHT/6.png")
        self.JUMPRIGHT6SCALED = self.JUMPRIGHT6.subsample(2, 2)
        self.JUMPRIGHT7 = tk.PhotoImage(file="bin/assets/Player/JUMPRIGHT/7.png")
        self.JUMPRIGHT7SCALED = self.JUMPRIGHT7.subsample(2, 2)
        self.JUMPRIGHT8 = tk.PhotoImage(file="bin/assets/Player/JUMPRIGHT/8.png")
        self.JUMPRIGHT8SCALED = self.JUMPRIGHT8.subsample(2, 2)
        
        
    def PlayerAnimationJUMPRIGHT(self, WORLD):
        WORLD.CANVAS.itemconfig("PLAYER",image=self.JUMPRIGHT1SCALED)
        #threading.Event().wait(0.001)
        WORLD.CANVAS.itemconfig("PLAYER",image=self.JUMPRIGHT2SCALED)
        #threading.Event().wait(0.001)
        WORLD.CANVAS.itemconfig("PLAYER",image=self.JUMPRIGHT3SCALED)
        #threading.Event().wait(0.001)
        WORLD.CANVAS.itemconfig("PLAYER",image=self.JUMPRIGHT4SCALED)
        #threading.Event().wait(0.001)
        WORLD.CANVAS.itemconfig("PLAYER",image=self.JUMPRIGHT5SCALED)
        #threading.Event().wait(0.001)
        WORLD.CANVAS.itemconfig("PLAYER",image=self.JUMPRIGHT6SCALED)
        #threading.Event().wait(0.001)
        WORLD.CANVAS.itemconfig("PLAYER",image=self.JUMPRIGHT7SCALED)
        #threading.Event().wait(0.001)
        WORLD.CANVAS.itemconfig("PLAYER",image=self.JUMPRIGHT8SCALED)
        #threading.Event().wait(0.001)
        WORLD.CANVAS.itemconfig("PLAYER",image=self.IDLERIGHT1SCALED)
        
        
    def PlayerAnimationJUMPLEFT(self, WORLD):
        WORLD.CANVAS.itemconfig("PLAYER",image=self.JUMPLEFT1SCALED)
        #threading.Event().wait(0.05)
        WORLD.CANVAS.itemconfig("PLAYER",image=self.JUMPLEFT2SCALED)
        #threading.Event().wait(0.05)
        WORLD.CANVAS.itemconfig("PLAYER",image=self.JUMPLEFT3SCALED)
        #threading.Event().wait(0.05)
        WORLD.CANVAS.itemconfig("PLAYER",image=self.JUMPLEFT4SCALED)
        #threading.Event().wait(0.05)
        WORLD.CANVAS.itemconfig("PLAYER",image=self.JUMPLEFT5SCALED)
        #threading.Event().wait(0.05)
        WORLD.CANVAS.itemconfig("PLAYER",image=self.JUMPLEFT6SCALED)
        #threading.Event().wait(0.05)
        WORLD.CANVAS.itemconfig("PLAYER",image=self.JUMPLEFT7SCALED)
        #threading.Event().wait(0.05)
        WORLD.CANVAS.itemconfig("PLAYER",image=self.JUMPLEFT8SCALED)
        #threading.Event().wait(0.05)
        WORLD.CANVAS.itemconfig("PLAYER",image=self.IDLELEFT1SCALED)
        
        
    def PlayerAnimationIDLERIGHT(self, WORLD, MOVEMENT, GAMEINSTANCE):
        if MOVEMENT.WPressed != True:
            if MOVEMENT.APressed != True:
                if MOVEMENT.SPressed != True:
                    if MOVEMENT.DPressed != True:
                        if MOVEMENT.SpacePressed != True:
                            if GAMEINSTANCE.GAMEOFF != True:
                                WORLD.CANVAS.itemconfig("PLAYER",image=self.IDLERIGHT1SCALED)
                                threading.Event().wait(0.1)
                                if MOVEMENT.WPressed != True:
                                    if MOVEMENT.APressed != True:
                                        if MOVEMENT.SPressed != True:
                                            if MOVEMENT.DPressed != True:
                                                if MOVEMENT.SpacePressed != True:
                                                    if GAMEINSTANCE.GAMEOFF != True:
                                                        WORLD.CANVAS.itemconfig("PLAYER",image=self.IDLERIGHT2SCALED)
                                                        threading.Event().wait(0.1)
                                                        if MOVEMENT.WPressed != True:
                                                            if MOVEMENT.APressed != True:
                                                                if MOVEMENT.SPressed != True:
                                                                    if MOVEMENT.DPressed != True:
                                                                        if MOVEMENT.SpacePressed != True:
                                                                            if GAMEINSTANCE.GAMEOFF != True:
                                                                                WORLD.CANVAS.itemconfig("PLAYER",image=self.IDLERIGHT3SCALED)                         
                                                                                threading.Event().wait(0.1)
                                                                                if MOVEMENT.WPressed != True:
                                                                                    if MOVEMENT.APressed != True:
                                                                                        if MOVEMENT.SPressed != True:
                                                                                            if MOVEMENT.DPressed != True:
                                                                                                if MOVEMENT.SpacePressed != True:
                                                                                                    if GAMEINSTANCE.GAMEOFF != True:
                                                                                                        WORLD.CANVAS.itemconfig("PLAYER",image=self.IDLERIGHT4SCALED)                                       
                                                                                                        threading.Event().wait(0.1)
                                                                                                        if MOVEMENT.WPressed != True:
                                                                                                            if MOVEMENT.APressed != True:
                                                                                                                if MOVEMENT.SPressed != True:
                                                                                                                    if MOVEMENT.DPressed != True:
                                                                                                                        if MOVEMENT.SpacePressed != True:
                                                                                                                            if GAMEINSTANCE.GAMEOFF != True:
                                                                                                                                WORLD.CANVAS.itemconfig("PLAYER",image=self.IDLERIGHT5SCALED)                                                   
                                                                                                                                threading.Event().wait(0.1)
                                                                                                                                if MOVEMENT.WPressed != True:
                                                                                                                                    if MOVEMENT.APressed != True:
                                                                                                                                        if MOVEMENT.SPressed != True:
                                                                                                                                            if MOVEMENT.DPressed != True:
                                                                                                                                                if MOVEMENT.SpacePressed != True:
                                                                                                                                                    if GAMEINSTANCE.GAMEOFF != True:
                                                                                                                                                        WORLD.CANVAS.itemconfig("PLAYER",image=self.IDLERIGHT6SCALED)                                                              
                                                                                                                                                        threading.Event().wait(0.1)
                                                                                                                                                        if MOVEMENT.WPressed != True:
                                                                                                                                                            if MOVEMENT.APressed != True:
                                                                                                                                                                if MOVEMENT.SPressed != True:
                                                                                                                                                                    if MOVEMENT.DPressed != True:
                                                                                                                                                                        if MOVEMENT.SpacePressed != True:
                                                                                                                                                                            if GAMEINSTANCE.GAMEOFF != True:
                                                                                                                                                                                WORLD.CANVAS.itemconfig("PLAYER",image=self.IDLERIGHT7SCALED)                                                                        
                                                                                                                                                                                threading.Event().wait(0.1)
                                                                                                                                                                                if MOVEMENT.WPressed != True:
                                                                                                                                                                                    if MOVEMENT.APressed != True:
                                                                                                                                                                                        if MOVEMENT.SPressed != True:
                                                                                                                                                                                            if MOVEMENT.DPressed != True:
                                                                                                                                                                                                if MOVEMENT.SpacePressed != False:
                                                                                                                                                                                                    if GAMEINSTANCE.GAMEOFF != True:
                                                                                                                                                                                                        WORLD.CANVAS.itemconfig("PLAYER",image=self.IDLERIGHT8SCALED)
                                                                                                
        
    
    def PlayerAnimationIDLELEFT(self, WORLD, MOVEMENT, GAMEINSTANCE):
        if MOVEMENT.WPressed != True:
            if MOVEMENT.APressed != True:
                if MOVEMENT.SPressed != True:
                    if MOVEMENT.DPressed != True:
                        if MOVEMENT.SpacePressed != True:
                            if GAMEINSTANCE.GAMEOFF != True: 
                                WORLD.CANVAS.itemconfig("PLAYER",image=self.IDLELEFT1SCALED)
                                threading.Event().wait(0.1)  
                                if MOVEMENT.WPressed != True:
                                    if MOVEMENT.APressed != True:
                                        if MOVEMENT.SPressed != True:
                                            if MOVEMENT.DPressed != True:
                                                if MOVEMENT.SpacePressed != True:  
                                                    if GAMEINSTANCE.GAMEOFF != True:      
                                                        WORLD.CANVAS.itemconfig("PLAYER",image=self.IDLELEFT2SCALED)              
                                                        threading.Event().wait(0.1)
                                                        if MOVEMENT.WPressed != True:
                                                            if MOVEMENT.APressed != True:
                                                                if MOVEMENT.SPressed != True:
                                                                    if MOVEMENT.DPressed != True:
                                                                        if MOVEMENT.SpacePressed != True: 
                                                                            if GAMEINSTANCE.GAMEOFF != True: 
                                                                                WORLD.CANVAS.itemconfig("PLAYER",image=self.IDLELEFT3SCALED)                     
                                                                                threading.Event().wait(0.1)
                                                                                if MOVEMENT.WPressed != True:
                                                                                    if MOVEMENT.APressed != True:
                                                                                        if MOVEMENT.SPressed != True:
                                                                                            if MOVEMENT.DPressed != True:
                                                                                                if MOVEMENT.SpacePressed != True:  
                                                                                                    if GAMEINSTANCE.GAMEOFF != True:
                                                                                                        WORLD.CANVAS.itemconfig("PLAYER",image=self.IDLELEFT4SCALED)                                     
                                                                                                        threading.Event().wait(0.1)
                                                                                                        if MOVEMENT.WPressed != True:
                                                                                                            if MOVEMENT.APressed != True:
                                                                                                                if MOVEMENT.SPressed != True:
                                                                                                                    if MOVEMENT.DPressed != True:
                                                                                                                        if MOVEMENT.SpacePressed != True:  
                                                                                                                            if GAMEINSTANCE.GAMEOFF != True:
                                                                                                                                WORLD.CANVAS.itemconfig("PLAYER",image=self.IDLELEFT5SCALED)                                                 
                                                                                                                                threading.Event().wait(0.1)
                                                                                                                                if MOVEMENT.WPressed != True:
                                                                                                                                    if MOVEMENT.APressed != True:
                                                                                                                                        if MOVEMENT.SPressed != True:
                                                                                                                                            if MOVEMENT.DPressed != True:
                                                                                                                                                if MOVEMENT.SpacePressed != True: 
                                                                                                                                                    if GAMEINSTANCE.GAMEOFF != True: 
                                                                                                                                                        WORLD.CANVAS.itemconfig("PLAYER",image=self.IDLELEFT6SCALED)                                                                                                                                 
                                                                                                                                                        threading.Event().wait(0.1)
                                                                                                                                                        if MOVEMENT.WPressed != True:
                                                                                                                                                            if MOVEMENT.APressed != True:
                                                                                                                                                                if MOVEMENT.SPressed != True:
                                                                                                                                                                    if MOVEMENT.DPressed != True:
                                                                                                                                                                        if MOVEMENT.SpacePressed != True:  
                                                                                                                                                                            if GAMEINSTANCE.GAMEOFF != True:
                                                                                                                                                                                WORLD.CANVAS.itemconfig("PLAYER",image=self.IDLELEFT7SCALED)                                                                         
                                                                                                                                                                                threading.Event().wait(0.1)
                                                                                                                                                                                if MOVEMENT.WPressed != True:
                                                                                                                                                                                    if MOVEMENT.APressed != True:
                                                                                                                                                                                        if MOVEMENT.SPressed != True:
                                                                                                                                                                                            if MOVEMENT.DPressed != True:
                                                                                                                                                                                                if MOVEMENT.SpacePressed != True:  
                                                                                                                                                                                                    if GAMEINSTANCE.GAMEOFF != True:
                                                                                                                                                                                                     WORLD.CANVAS.itemconfig("PLAYER",image=self.IDLELEFT8SCALED)                                                                                  
                                                
                                                                                                          
      
    def PlayerAnimationRUNRIGHT(self, WORLD):
        WORLD.CANVAS.itemconfig("PLAYER",image=self.RUNRIGHT1SCALED)           
        #threading.Event().wait(0.0005)
        WORLD.CANVAS.itemconfig("PLAYER",image=self.RUNRIGHT2SCALED)                       
        #threading.Event().wait(0.05)
        WORLD.CANVAS.itemconfig("PLAYER",image=self.RUNRIGHT3SCALED)                                      
        #threading.Event().wait(0.05)        
        WORLD.CANVAS.itemconfig("PLAYER",image=self.RUNRIGHT4SCALED)                                                    
        #threading.Event().wait(0.05)            
        WORLD.CANVAS.itemconfig("PLAYER",image=self.RUNRIGHT6SCALED)                                                           
        #threading.Event().wait(0.05)           
        WORLD.CANVAS.itemconfig("PLAYER",image=self.RUNRIGHT7SCALED)                                                                       
        #threading.Event().wait(0.05)
        WORLD.CANVAS.itemconfig("PLAYER",image=self.RUNRIGHT8SCALED)
                                                                                                          
    def PlayerAnimationRUNLEFT(self, WORLD):         
        WORLD.CANVAS.itemconfig("PLAYER",image=self.RUNLEFT1SCALED)    
        #threading.Event().wait(0.05)               
        WORLD.CANVAS.itemconfig("PLAYER",image=self.RUNLEFT2SCALED)                          
        #threading.Event().wait(0.05)                   
        WORLD.CANVAS.itemconfig("PLAYER",image=self.RUNLEFT3SCALED)                                      
        #threading.Event().wait(0.05)                       
        WORLD.CANVAS.itemconfig("PLAYER",image=self.RUNLEFT4SCALED)                                                  
        #threading.Event().wait(0.05)                       
        WORLD.CANVAS.itemconfig("PLAYER",image=self.RUNLEFT5SCALED)                                                                
        #threading.Event().wait(0.05)                  
        WORLD.CANVAS.itemconfig("PLAYER",image=self.RUNLEFT6SCALED)                                                                          
        #threading.Event().wait(0.05)            
        WORLD.CANVAS.itemconfig("PLAYER",image=self.RUNLEFT7SCALED)                                                                                     
        #threading.Event().wait(0.05)                           
        WORLD.CANVAS.itemconfig("PLAYER",image=self.RUNLEFT8SCALED)
        
                                                                                                                   