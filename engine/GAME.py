import customtkinter as ctk
import tkinter as tk
import sys
class GAME:
    def __init__(self):
        self.GAME = ctk.CTk()
        self.GAME.title("SoulWoods")
        self.GAME.geometry("1280x1024+600+150")
        self.GAME.resizable(False,False)
        self.GAME.iconbitmap("bin/assets/GameEssential/icon.ico")
        self.GAME.config(highlightthickness=0,borderwidth=0,background="#000000")  
        self.GAMEOFF = False    
    def StartGame(self):
        self.GAME.mainloop()
    def EXIT(self, MOVEMENT):
        self.GAMEOFF = True
        MOVEMENT.UPDATEPLAYERTHREAD.join()
        self.GAME.destroy()
        sys.exit()
        
        