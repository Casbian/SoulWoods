#Game Classes
from Player import Player
from Monster import Monster
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading


font = ('Verdana',10)
game = ctk.CTk()
game.title("SoulWoods")
game.geometry("1024x512+600+300")
game.resizable(False,False)
game.iconbitmap("SoulWoods/assets/SoulWoods.ico")

#Startup Screen
pngStartupScreen1 = tk.PhotoImage(file="SoulWoods/assets/StartupScreen/1.png")
pngStartupScreenScaled1 = pngStartupScreen1.subsample(2,2)
pngStartupScreenButton1 = tk.PhotoImage(file="SoulWoods/assets/StartupScreen/Button1.png")
pngStartupScreenButtonScaled1 = pngStartupScreenButton1.subsample(2,2)
pngStartupScreenButton2 = tk.PhotoImage(file="SoulWoods/assets/StartupScreen/Button2.png")
pngStartupScreenButtonScaled2 = pngStartupScreenButton2.subsample(2,2)
pngStartupScreenButton3 = tk.PhotoImage(file="SoulWoods/assets/StartupScreen/Button3.png")
pngStartupScreenButtonScaled3 = pngStartupScreenButton3.subsample(2,2)
def StartUpScreen():
    main = tk.Canvas(game,borderwidth=0,highlightthickness=0)
    main.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relheight=1, relwidth=1)
    main.create_image(512, 256, image=pngStartupScreenScaled1)
    threading.Event().wait(2)
    mainButton = tk.Button(game,borderwidth=0,highlightthickness=0,background="#000000",activebackground="#000000",command=lambda:StartStoryThread(main,mainButton))
    mainButton.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
    mainButton.config(state="disabled")
    mainButton.config(image=pngStartupScreenButtonScaled1)
    threading.Event().wait(0.5)
    mainButton.config(image=pngStartupScreenButtonScaled2)
    threading.Event().wait(0.5)
    mainButton.config(image=pngStartupScreenButtonScaled3)
    mainButton.config(state="active")
#Story Screen
pngMainScreenBG = tk.PhotoImage(file="SoulWoods/assets/Story/bg.png")
pngMainScreenScaledBG = pngMainScreenBG.subsample(2,2)
pngMainScreen1 = tk.PhotoImage(file="SoulWoods/assets/Story/0.png")
pngMainScreenScaled1 = pngMainScreen1.subsample(2,2)
pngMainScreen2 = tk.PhotoImage(file="SoulWoods/assets/Story/1.png")
pngMainScreenScaled2 = pngMainScreen2.subsample(2,2) 
pngMainScreen3 = tk.PhotoImage(file="SoulWoods/assets/Story/2.png")
pngMainScreenScaled3 = pngMainScreen3.subsample(2,2) 
pngMainScreen4 = tk.PhotoImage(file="SoulWoods/assets/Story/3.png")
pngMainScreenScaled4 = pngMainScreen4.subsample(2,2) 
pngMainScreen5 = tk.PhotoImage(file="SoulWoods/assets/Story/4.png")
pngMainScreenScaled5 = pngMainScreen5.subsample(2,2) 
pngMainScreen6 = tk.PhotoImage(file="SoulWoods/assets/Story/5.png")
pngMainScreenScaled6 = pngMainScreen6.subsample(2,2) 
pngMainScreen7 = tk.PhotoImage(file="SoulWoods/assets/Story/6.png")
pngMainScreenScaled7 = pngMainScreen7.subsample(2,2) 
pngMainScreen8 = tk.PhotoImage(file="SoulWoods/assets/Story/7.png")
pngMainScreenScaled8 = pngMainScreen8.subsample(2,2) 
pngMainScreen9 = tk.PhotoImage(file="SoulWoods/assets/Story/8.png")
pngMainScreenScaled9 = pngMainScreen9.subsample(2,2) 
pngMainScreen10 = tk.PhotoImage(file="SoulWoods/assets/Story/9.png")
pngMainScreenScaled10 = pngMainScreen10.subsample(2,2)  
pngMainScreen11 = tk.PhotoImage(file="SoulWoods/assets/Story/10.png")
pngMainScreenScaled11 = pngMainScreen11.subsample(2,2)
pngMainScreenButton1 = tk.PhotoImage(file="SoulWoods/assets/Story/Button1.png")
pngMainScreenButtonScaled1 = pngMainScreenButton1.subsample(2,2)
pngMainScreenButton2 = tk.PhotoImage(file="SoulWoods/assets/Story/Button2.png")
pngMainScreenButtonScaled2 = pngMainScreenButton2.subsample(2,2)
pngMainScreenButton3 = tk.PhotoImage(file="SoulWoods/assets/Story/Button3.png")
pngMainScreenButtonScaled3 = pngMainScreenButton3.subsample(2,2)
def StoryScreen():
    main = tk.Canvas(game,borderwidth=0,highlightthickness=0)
    main.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relheight=1, relwidth=1)
    main.create_image(512, 256, image=pngMainScreenScaledBG)
    main.create_image(512, 256, image=pngMainScreenScaled1,tags="StoryPNG")
    threading.Event().wait(0.5)
    mainButton = tk.Button(main,borderwidth=0,highlightthickness=0,background="#000000",activebackground="#000000",command=lambda:StartMainThread(main,mainButton))
    mainButton.place(relx=0.5, rely=0.90, anchor=tk.CENTER)
    mainButton.config(state="disabled")
    mainButton.config(image=pngMainScreenButtonScaled1)
    main.delete("StoryPNG")
    main.create_image(512, 256, image=pngMainScreenScaled2,tags="StoryPNG")
    threading.Event().wait(0.5)
    main.delete("StoryPNG")
    main.create_image(512, 256, image=pngMainScreenScaled3,tags="StoryPNG")
    threading.Event().wait(0.5)
    main.delete("StoryPNG")
    main.create_image(512, 256, image=pngMainScreenScaled4,tags="StoryPNG")
    threading.Event().wait(0.5)
    main.delete("StoryPNG")
    main.create_image(512, 256, image=pngMainScreenScaled5,tags="StoryPNG")
    threading.Event().wait(0.5)
    main.delete("StoryPNG")
    main.create_image(512, 256, image=pngMainScreenScaled6,tags="StoryPNG")
    threading.Event().wait(0.5)
    main.delete("StoryPNG")
    main.create_image(512, 256, image=pngMainScreenScaled7,tags="StoryPNG")
    threading.Event().wait(0.5)
    mainButton.config(image=pngMainScreenButtonScaled2)
    main.delete("StoryPNG")
    main.create_image(512, 256, image=pngMainScreenScaled8,tags="StoryPNG")
    threading.Event().wait(0.5)
    main.delete("StoryPNG")
    main.create_image(512, 256, image=pngMainScreenScaled9,tags="StoryPNG")
    threading.Event().wait(0.5)
    main.delete("StoryPNG")
    main.create_image(512, 256, image=pngMainScreenScaled10,tags="StoryPNG")
    threading.Event().wait(0.5)
    main.delete("StoryPNG")
    main.create_image(512, 256, image=pngMainScreenScaled11,tags="StoryPNG")
    mainButton.config(image=pngMainScreenButtonScaled3)
    mainButton.config(state="active")
#Main Screen
pngMainScreenRoot = tk.PhotoImage(file="SoulWoods/assets/MainScreen/MainScreenRoot.png")
pngMainScreenScaledRoot = pngMainScreenRoot.subsample(2,2)
pngMainScreenButtonAttack = tk.PhotoImage(file="SoulWoods/assets/MainScreen/Attack.png")
pngMainScreenButtonAttackScaled = pngMainScreenButtonAttack.subsample(2,2)
pngMainScreenButtonGuard = tk.PhotoImage(file="SoulWoods/assets/MainScreen/Guard.png")
pngMainScreenButtonGuardScaled = pngMainScreenButtonGuard.subsample(2,2)

def MainScreen():
    main = tk.Canvas(game,borderwidth=0,highlightthickness=0)
    main.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relheight=1, relwidth=1)
    main.create_image(512, 256, image=pngMainScreenScaledRoot)
    mainButtonAttack = tk.Button(main,borderwidth=0,highlightthickness=0,background="#ecddc0",activebackground="#ecddc0",command=game.quit)
    mainButtonAttack.place(relx=0.4, rely=0.81, anchor=tk.CENTER)
    mainButtonGuard = tk.Button(main,borderwidth=0,highlightthickness=0,background="#ecddc0",activebackground="#ecddc0",command=game.quit)
    mainButtonGuard.place(relx=0.33, rely=0.81, anchor=tk.CENTER)
    mainButtonAttack.config(image=pngMainScreenButtonAttackScaled)
    mainButtonGuard.config(image=pngMainScreenButtonGuardScaled)
    message_text = "This is a long message that will automatically wrap to fit the width of the message widget. You can use this widget to display larger blocks of text in your application."
    message = tk.Message(main, text=message_text, width=180,borderwidth=0,highlightthickness=0,background="#ecddc0")
    message.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
    
    
    
    
    
    
    

    
    
    
#Automated Thread Starts from other Functions
def StartStoryThread(main,mainButton):
    main.destroy()
    mainButton.destroy()
    gameStoryThread = threading.Thread(target=StoryScreen)
    gameStoryThread.start()
def StartMainThread(main,mainButton):
    main.destroy()
    mainButton.destroy()
    gameMainThread = threading.Thread(target=MainScreen)
    gameMainThread.start()
#Programm Logic
gameStartThread = threading.Thread(target=StartUpScreen)
gameStartThread.start()









game.mainloop()
exit()