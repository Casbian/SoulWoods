import threading
class MOVEMENT:
    def __init__(self):
        self.WPressed = False
        self.APressed = False
        self.SPressed = False
        self.DPressed = False
        self.SpacePressed = False
        self.DIRECTION = 0
        self.UPDATEPLAYERLOOP = True
    
    def KeyPress(self, event):
        if event.keysym == 'a':
            self.APressed = True
            self.DIRECTION = 0
        if event.keysym == 'A':
            self.APressed = True
            self.DIRECTION = 0
        if event.keysym == 's':
            self.SPressed = True
        if event.keysym == 'S':
            self.SPressed = True
        if event.keysym == 'd':
            self.DPressed = True
            self.DIRECTION = 1
        if event.keysym == 'D':
            self.DPressed = True
            self.DIRECTION = 1
        if event.keysym == 'w':
            self.WPressed = True
        if event.keysym == 'W':
            self.WPressed = True
        if event.keysym == 'space':
            self.SpacePressed = True
    
    def KeyRelease(self, event):
        if event.keysym == 'a':
            self.APressed = False
        if event.keysym == 'A':
            self.APressed = False
        if event.keysym == 's':
            self.SPressed = False
        if event.keysym == 'S':
            self.SPressed = False
        if event.keysym == 'd':
            self.DPressed = False
        if event.keysym == 'D':
            self.DPressed = False
        if event.keysym == 'w':
            self.WPressed = False
        if event.keysym == 'W':
            self.WPressed = False
        if event.keysym == 'space':
            self.SpacePressed = False
    
    def UpdatePlayerThread(self, WORLD, PLAYER, GAMEINSTANCE):
        self.UPDATEPLAYERTHREAD = threading.Thread(target=self.UpdatePlayer, args=(WORLD, PLAYER, GAMEINSTANCE))
        self.UPDATEPLAYERTHREAD.start()
            
    def UpdatePlayer(self, WORLD, PLAYER, GAMEINSTANCE):
        while self.UPDATEPLAYERLOOP == True:
            if GAMEINSTANCE.GAMEOFF == True:
                self.UPDATEPLAYERLOOP = False
            #x,y = WORLD.CANVAS.coords("PLAYER")
            if self.APressed == False and self.SPressed == False and self.DPressed == False and self.WPressed == False and self.SpacePressed == False and GAMEINSTANCE.GAMEOFF== False:
                if self.DIRECTION == 1:
                    PLAYER.PlayerAnimationIDLERIGHT(WORLD, self, GAMEINSTANCE)
                if self.DIRECTION == 0:
                    PLAYER.PlayerAnimationIDLELEFT(WORLD, self, GAMEINSTANCE)
            if self.SpacePressed == True:
                if self.DIRECTION == 1:
                    WORLD.CANVAS.move("PLAYER",0,-30)
                    PLAYER.PlayerAnimationJUMPRIGHT(WORLD)
                    WORLD.CANVAS.move("PLAYER",0,30)
                if self.DIRECTION == 0:
                    WORLD.CANVAS.move("PLAYER",0,-30)
                    PLAYER.PlayerAnimationJUMPLEFT(WORLD)
                    WORLD.CANVAS.move("PLAYER",0,30)
            if self.DPressed == True:
                if self.DIRECTION == 1:
                    WORLD.CANVAS.move("PLAYER",6,0)
                    PLAYER.PlayerAnimationRUNRIGHT(WORLD)
                if self.DIRECTION == 0:
                    WORLD.CANVAS.move("PLAYER",6,0)        
            if self.APressed == True:
                if self.DIRECTION == 1:
                    WORLD.CANVAS.move("PLAYER",-6,0)
                if self.DIRECTION == 0:
                    WORLD.CANVAS.move("PLAYER",-6,0)
                    PLAYER.PlayerAnimationRUNLEFT(WORLD)           
            if self.WPressed == True:
                if self.DIRECTION == 1:
                    WORLD.CANVAS.move("PLAYER",0,-6)
                    PLAYER.PlayerAnimationRUNRIGHT(WORLD)
                if self.DIRECTION == 0:
                    WORLD.CANVAS.move("PLAYER",0,-6)
                    PLAYER.PlayerAnimationRUNLEFT(WORLD)      
            if self.SPressed == True:
                if self.DIRECTION == 1:
                    WORLD.CANVAS.move("PLAYER",0,6)
                    PLAYER.PlayerAnimationRUNRIGHT(WORLD)
                if self.DIRECTION == 0:
                    WORLD.CANVAS.move("PLAYER",0,6)
                    PLAYER.PlayerAnimationRUNLEFT(WORLD)
            
          
                        
            
                    
            
            

  