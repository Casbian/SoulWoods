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
        self.GAME.protocol("WM_DELETE_WINDOW", self.EXIT)        
    def StartGame(self):
        self.GAME.mainloop()
    def EXIT(self):
        self.GAME.destroy()
        sys.exit()