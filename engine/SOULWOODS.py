import customtkinter as ctk
import tkinter as tk
import random
class SOULWOODS():
    def __init__(self):
        self.TITLEART = tk.PhotoImage(file="bin/assets/GameEssential/SoulWoodsTitle.png")
        self.TITLEARTSCALED = self.TITLEART.subsample(2,2)