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
#Main Screen and Game
pngMainScreenRoot1 = tk.PhotoImage(file="SoulWoods/assets/MainScreen/MainScreenRoot1.png")
pngMainScreenScaledRoot1 = pngMainScreenRoot1.subsample(2,2)
pngMainScreenRoot2 = tk.PhotoImage(file="SoulWoods/assets/MainScreen/MainScreenRoot2.png")
pngMainScreenScaledRoot2 = pngMainScreenRoot2.subsample(2,2)
pngMainScreenRoot3 = tk.PhotoImage(file="SoulWoods/assets/MainScreen/MainScreenRoot3.png")
pngMainScreenScaledRoot3 = pngMainScreenRoot3.subsample(2,2)
pngMainScreenButtonAttack = tk.PhotoImage(file="SoulWoods/assets/MainScreen/Attack.png")
pngMainScreenButtonAttackScaled = pngMainScreenButtonAttack.subsample(2,2)
pngMainScreenButtonGuard = tk.PhotoImage(file="SoulWoods/assets/MainScreen/Guard.png")
pngMainScreenButtonGuardScaled = pngMainScreenButtonGuard.subsample(2,2)
pngMonsterIDLE = tk.PhotoImage(file="SoulWoods/assets/MainScreen/MonsterIDLE.png")
pngMonsterIDLEScaled = pngMonsterIDLE.subsample(2,2)
pngMonsterHURT = tk.PhotoImage(file="SoulWoods/assets/MainScreen/MonsterHURT.png")
pngMonsterHURTScaled = pngMonsterHURT.subsample(2,2)
pngMonsterATTACK1 = tk.PhotoImage(file="SoulWoods/assets/MainScreen/MonsterATTACK1.png")
pngMonsterATTACKScaled1 = pngMonsterATTACK1.subsample(2,2)
pngMonsterATTACK2 = tk.PhotoImage(file="SoulWoods/assets/MainScreen/MonsterATTACK2.png")
pngMonsterATTACKScaled2 = pngMonsterATTACK2.subsample(2,2)
pngMonsterATTACK3 = tk.PhotoImage(file="SoulWoods/assets/MainScreen/MonsterATTACK3.png")
pngMonsterATTACKScaled3 = pngMonsterATTACK3.subsample(2,2)
pngPlayerIDLE = tk.PhotoImage(file="SoulWoods/assets/MainScreen/PlayerIDLE.png")
pngPlayerIDLEScaled = pngPlayerIDLE.subsample(2,2)
pngPlayerHURT = tk.PhotoImage(file="SoulWoods/assets/MainScreen/PlayerHURT.png")
pngPlayerHURTScaled = pngPlayerHURT.subsample(2,2)
pngPlayerATTACK1 = tk.PhotoImage(file="SoulWoods/assets/MainScreen/PlayerATTACK1.png")
pngPlayerATTACKScaled1 = pngPlayerATTACK1.subsample(2,2)
pngPlayerATTACK2 = tk.PhotoImage(file="SoulWoods/assets/MainScreen/PlayerATTACK2.png")
pngPlayerATTACKScaled2 = pngPlayerATTACK2.subsample(2,2)
pngPlayerATTACK3 = tk.PhotoImage(file="SoulWoods/assets/MainScreen/PlayerATTACK3.png")
pngPlayerATTACKScaled3 = pngPlayerATTACK3.subsample(2,2)
pngMainScreenButtonACK = tk.PhotoImage(file="SoulWoods/assets/MainScreen/ACKButton.png")
pngMainScreenButtonACKScaled = pngMainScreenButtonACK.subsample(2,2)
def MainScreen():
    main = tk.Canvas(game,borderwidth=0,highlightthickness=0)
    main.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relheight=1, relwidth=1)
    main.create_image(512, 256, image=pngMainScreenScaledRoot1,tags="ROOT")
    mainButtonAttack = tk.Button(main,borderwidth=0,highlightthickness=0,background="#ecddc0",activebackground="#ecddc0")
    mainButtonAttack.place(relx=0.4, rely=0.81, anchor=tk.CENTER)
    mainButtonGuard = tk.Button(main,borderwidth=0,highlightthickness=0,background="#ecddc0",activebackground="#ecddc0")
    mainButtonGuard.place(relx=0.33, rely=0.81, anchor=tk.CENTER)
    mainButtonAttack.config(image=pngMainScreenButtonAttackScaled)
    mainButtonGuard.config(image=pngMainScreenButtonGuardScaled)
    mainButtonAttack.config(state="disabled")
    mainButtonGuard.config(state="disabled")
    consoleText = "-- GUARD Button\nNegates all DAMAGE this round\n\n-- ATTACK Button\nStarts Combat\n\n-- UPGRADES\nUse mouse to choose"
    console = tk.Message(main, text=consoleText, width=180,borderwidth=0,highlightthickness=0,background="#ecddc0")
    console.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
    mainButtonACK = tk.Button(main,borderwidth=0,highlightthickness=0,background="#ecddc0",activebackground="#ecddc0",command=lambda: ACKStartGame(main,console,mainButtonACK,mainButtonAttack,mainButtonGuard))
    mainButtonACK.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
    mainButtonACK.config(image=pngMainScreenButtonACKScaled)      
def Game(main,mainButtonAttack,mainButtonGuard):
    ROUNDCOUNTER = 0
    PLAYER = Player
    MONSTER = Monster
    ROUNDCOUNTER = ROUNDCOUNTER+1
    PLAYER.playerLevel = ROUNDCOUNTER
    MONSTER.monsterLevel = ROUNDCOUNTER
    main.itemconfig("ROOT",image=pngMainScreenScaledRoot2)
    main.create_image(200, 350, image=pngPlayerIDLEScaled,tags="PLAYER")
    main.create_image(775, 350, image=pngMonsterIDLEScaled,tags="MONSTER")
    playerHP = tk.Message(main, text=PLAYER.playerHP, width=180,borderwidth=0,highlightthickness=0,background="#ecddc0",foreground="#4ad607")
    playerHP.place(relx=0.28, rely=0.30, anchor=tk.CENTER)
    playerSpeed = tk.Message(main, text=PLAYER.playerSpeed, width=180,borderwidth=0,highlightthickness=0,background="#ecddc0",foreground="#0051ca")
    playerSpeed.place(relx=0.28, rely=0.37, anchor=tk.CENTER)
    playerDamage = tk.Message(main, text=PLAYER.playerDamage, width=180,borderwidth=0,highlightthickness=0,background="#ecddc0",foreground="#e70000")
    playerDamage.place(relx=0.28, rely=0.43, anchor=tk.CENTER)
    playerLevel = tk.Message(main, text=PLAYER.playerLevel, width=180,borderwidth=0,highlightthickness=0,background="#ecddc0",foreground="#000000")
    playerLevel.place(relx=0.28, rely=0.49, anchor=tk.CENTER)
    monsterHP = tk.Message(main, text=MONSTER.monsterHP, width=180,borderwidth=0,highlightthickness=0,background="#ecddc0",foreground="#4ad607")
    monsterHP.place(relx=0.80, rely=0.30, anchor=tk.CENTER)
    monsterSpeed = tk.Message(main, text=MONSTER.monsterSpeed, width=180,borderwidth=0,highlightthickness=0,background="#ecddc0",foreground="#0051ca")
    monsterSpeed.place(relx=0.80, rely=0.37, anchor=tk.CENTER)
    monsterDamage = tk.Message(main, text=MONSTER.monsterDamage, width=180,borderwidth=0,highlightthickness=0,background="#ecddc0",foreground="#e70000")
    monsterDamage.place(relx=0.80, rely=0.43, anchor=tk.CENTER)
    monsterLevel = tk.Message(main, text=MONSTER.monsterLevel, width=180,borderwidth=0,highlightthickness=0,background="#ecddc0",foreground="#000000")
    monsterLevel.place(relx=0.80, rely=0.49, anchor=tk.CENTER)
    def Attack():
        DEATHLOOP = False
        while DEATHLOOP==False:
            if PLAYER.playerSpeed>=MONSTER.monsterSpeed:
                main.itemconfig("PLAYER",image=pngPlayerATTACKScaled1)
                threading.Event().wait(0.1)
                main.itemconfig("PLAYER",image=pngPlayerATTACKScaled2)
                threading.Event().wait(0.1)
                main.itemconfig("MONSTER",image=pngMonsterHURT)
                threading.Event().wait(0.1)
                main.itemconfig("MONSTER",image=pngMonsterIDLEScaled)
                threading.Event().wait(0.1)
                main.itemconfig("PLAYER",image=pngPlayerATTACKScaled3)
                MONSTER.monsterHP = MONSTER.monsterHP-PLAYER.playerDamage
                monsterHP.config(text=MONSTER.monsterHP)
                threading.Event().wait(0.1)
                main.itemconfig("PLAYER",image=pngPlayerIDLEScaled)
                threading.Event().wait(0.1)
                main.itemconfig("MONSTER",image=pngMonsterATTACKScaled1)
                threading.Event().wait(0.1)
                main.itemconfig("MONSTER",image=pngMonsterATTACKScaled2)
                threading.Event().wait(0.1)
                main.itemconfig("PLAYER",image=pngPlayerHURT)
                threading.Event().wait(0.1)
                main.itemconfig("PLAYER",image=pngPlayerIDLEScaled)
                threading.Event().wait(0.1)
                main.itemconfig("MONSTER",image=pngMonsterATTACKScaled3)
                PLAYER.playerHP = PLAYER.playerHP-MONSTER.monsterDamage
                playerHP.config(text=PLAYER.playerHP)
                threading.Event().wait(0.1)
                main.itemconfig("MONSTER",image=pngMonsterIDLEScaled)
                if PLAYER.playerHP<=0:
                    DEATHLOOP = True
                    playerHP.destroy()
                    playerSpeed.destroy()
                    playerDamage.destroy()
                    playerLevel.destroy()
                    monsterHP.destroy()
                    monsterSpeed.destroy()
                    monsterDamage.destroy()
                    monsterLevel.destroy()
                    main.itemconfig("ROOT",image=pngMainScreenScaledRoot3)
                    mainButtonAttack.config(state="disabled")
                    mainButtonGuard.config(state="disabled") 
                elif MONSTER.monsterHP<=0:
                    DEATHLOOP = True
                    mainButtonAttack.config(state="disabled")
                    mainButtonGuard.config(state="disabled")
                else:
                    pass
            else:
                main.itemconfig("MONSTER",image=pngMonsterATTACKScaled1)
                threading.Event().wait(0.1)
                main.itemconfig("MONSTER",image=pngMonsterATTACKScaled2)
                threading.Event().wait(0.1)
                main.itemconfig("MONSTER",image=pngMonsterATTACKScaled3)
                PLAYER.playerHP = PLAYER.playerHP-MONSTER.monsterDamage
                playerHP.config(text=PLAYER.playerHP)
                threading.Event().wait(0.1)
                main.itemconfig("MONSTER",image=pngMonsterIDLEScaled)
                threading.Event().wait(0.1)
                main.itemconfig("PLAYER",image=pngPlayerATTACKScaled1)
                threading.Event().wait(0.1)
                main.itemconfig("PLAYER",image=pngPlayerATTACKScaled2)
                threading.Event().wait(0.1)
                main.itemconfig("PLAYER",image=pngPlayerATTACKScaled3)
                MONSTER.monsterHP = MONSTER.monsterHP-PLAYER.playerDamage
                monsterHP.config(text=MONSTER.monsterHP)
                threading.Event().wait(0.1)
                main.itemconfig("PLAYER",image=pngPlayerIDLEScaled)
                if PLAYER.playerHP<=0:
                    DEATHLOOP = True
                    playerHP.destroy()
                    playerSpeed.destroy()
                    playerDamage.destroy()
                    playerLevel.destroy()
                    monsterHP.destroy()
                    monsterSpeed.destroy()
                    monsterDamage.destroy()
                    monsterLevel.destroy()
                    main.itemconfig("ROOT",image=pngMainScreenScaledRoot3)
                    mainButtonAttack.config(state="disabled")
                    mainButtonGuard.config(state="disabled")  
                elif MONSTER.monsterHP<=0:
                    DEATHLOOP = True
                    mainButtonAttack.config(state="disabled")
                    mainButtonGuard.config(state="disabled")
                else:
                    pass
                
                
            
    def Guard():
        pass
    def AttackThread():
        gameAttackThread = threading.Thread(target=Attack)
        gameAttackThread.start()
    def GuardThread():
        gameGuardThread = threading.Thread(target=Guard)
        gameGuardThread.start()
    mainButtonAttack.config(command=AttackThread)
    mainButtonGuard.config(command=GuardThread)
    mainButtonAttack.config(state="active")
    mainButtonGuard.config(state="active")
    
       
        
        
        
    
        
    
    
   
    

    
    
    
#Automated Thread Starts from other Functions
def ACKStartGame(main,console,mainButtonACK,mainButtonAttack,mainButtonGuard):
    console.destroy()
    mainButtonACK.destroy() 
    gameGameThread = threading.Thread(target=Game(main,mainButtonAttack,mainButtonGuard))
    gameGameThread.start()
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