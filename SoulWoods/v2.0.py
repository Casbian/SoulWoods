################################################################################
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
###############################################################################
#Game Classes
from Player import Player
from Monster import Monster
from Upgrade import UpgradeClass
import customtkinter as ctk
import tkinter as tk
import sys
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
pngMainScreenButtonACK = tk.PhotoImage(file="SoulWoods/assets/MainScreen/ACKButton.png")
pngMainScreenButtonACKScaled = pngMainScreenButtonACK.subsample(2,2)
pngMonsterIDLE = tk.PhotoImage(file="SoulWoods/assets/MainScreen/MonsterIDLE.png")
pngMonsterIDLEScaled = pngMonsterIDLE.subsample(2,2)
pngMonsterHURT = tk.PhotoImage(file="SoulWoods/assets/MainScreen/MonsterHURT.png")
pngMonsterHURTScaled = pngMonsterHURT.subsample(2,2)
pngMonsterDEATH1 = tk.PhotoImage(file="SoulWoods/assets/MainScreen/MonsterDEATH1.png")
pngMonsterDEATHScaled1 = pngMonsterDEATH1.subsample(2,2)
pngMonsterDEATH2 = tk.PhotoImage(file="SoulWoods/assets/MainScreen/MonsterDEATH2.png")
pngMonsterDEATHScaled2 = pngMonsterDEATH2.subsample(2,2)
pngMonsterDEATH3 = tk.PhotoImage(file="SoulWoods/assets/MainScreen/MonsterDEATH3.png")
pngMonsterDEATHScaled3 = pngMonsterDEATH3.subsample(2,2)
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


pngUpgradeHP = tk.PhotoImage(file="SoulWoods/assets/MainScreen/UpgradeHP.png")
pngUpgradeHPScaled = pngUpgradeHP.subsample(2,2)
pngUpgradeSpeed = tk.PhotoImage(file="SoulWoods/assets/MainScreen/UpgradeSpeed.png")
pngUpgradeSpeedScaled = pngUpgradeSpeed.subsample(2,2)
pngUpgradeAttack = tk.PhotoImage(file="SoulWoods/assets/MainScreen/UpgradeAttack.png")
pngUpgradeAttackScaled = pngUpgradeAttack.subsample(2,2)

def MainScreen():
    PLAYER = Player
    ROUNDCOUNTER = 0
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
    mainButtonACK = tk.Button(main,borderwidth=0,highlightthickness=0,background="#ecddc0",activebackground="#ecddc0",command=lambda: ACKStartGame(main,console,mainButtonACK,mainButtonAttack,mainButtonGuard,PLAYER,ROUNDCOUNTER))
    mainButtonACK.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
    mainButtonACK.config(image=pngMainScreenButtonACKScaled) 
def Game(main,mainButtonAttack,mainButtonGuard,PLAYER,ROUNDCOUNTER):
    ROUNDCOUNTER = ROUNDCOUNTER+1
    PLAYER.playerLevel = ROUNDCOUNTER
    MONSTER = Monster(ROUNDCOUNTER)
    MONSTER.monsterLevel = ROUNDCOUNTER
    mainButtonAttack.config(state="active")
    mainButtonGuard.config(state="active")
    main.itemconfig("ROOT",image=pngMainScreenScaledRoot2)
    main.create_image(200, 400, image=pngPlayerIDLEScaled,tags="PLAYER")
    main.create_image(775, 400, image=pngMonsterIDLEScaled,tags="MONSTER")
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
        mainButtonAttack.config(state="disabled")
        mainButtonGuard.config(state="disabled")
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
                elif MONSTER.monsterHP<=0:
                    DEATHLOOP = True
                    main.itemconfig("MONSTER",image=pngMonsterDEATHScaled1)
                    threading.Event().wait(0.1)
                    main.itemconfig("MONSTER",image=pngMonsterDEATHScaled2)
                    threading.Event().wait(0.1)
                    main.itemconfig("MONSTER",image=pngMonsterDEATHScaled3)
                    gameGameLoopThread = threading.Thread(target=Upgrade(main,mainButtonAttack,mainButtonGuard,PLAYER,ROUNDCOUNTER))
                    gameGameLoopThread.start()
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
                elif MONSTER.monsterHP<=0:
                    DEATHLOOP = True
                    main.itemconfig("MONSTER",image=pngMonsterDEATHScaled1)
                    threading.Event().wait(0.1)
                    main.itemconfig("MONSTER",image=pngMonsterDEATHScaled2)
                    threading.Event().wait(0.1)
                    main.itemconfig("MONSTER",image=pngMonsterDEATHScaled3)
                    gameGameLoopThread = threading.Thread(target=Upgrade(main,mainButtonAttack,mainButtonGuard,PLAYER,ROUNDCOUNTER))
                    gameGameLoopThread.start()
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
    def Upgrade(main,mainButtonAttack,mainButtonGuard,PLAYER,ROUNDCOUNTER):
        UPGRADE = UpgradeClass(ROUNDCOUNTER)
        main.itemconfig("ROOT",image=pngMainScreenScaledRoot1)
        mainButtonUpgradeHP = tk.Button(main,borderwidth=0,highlightthickness=0,background="#ecddc0",activebackground="#ecddc0",foreground="#4ad607")
        mainButtonUpgradeHP.place(relx=0.5, rely=0.28, anchor=tk.CENTER)
        mainButtonUpgradeSpeed = tk.Button(main,borderwidth=0,highlightthickness=0,background="#ecddc0",activebackground="#ecddc0",foreground="#0051ca")
        mainButtonUpgradeSpeed.place(relx=0.5, rely=0.38, anchor=tk.CENTER)
        mainButtonUpgradeAttack =  tk.Button(main,borderwidth=0,highlightthickness=0,background="#ecddc0",activebackground="#ecddc0",foreground="#e70000")
        mainButtonUpgradeAttack.place(relx=0.5, rely=0.48, anchor=tk.CENTER)
        mainButtonUpgradeHP.config(image=pngUpgradeHPScaled)
        mainButtonUpgradeSpeed.config(image=pngUpgradeSpeedScaled)
        mainButtonUpgradeAttack.config(image=pngUpgradeAttackScaled)
        upgradeHPText = tk.Message(main, text=UPGRADE.heilung, width=180,borderwidth=0,highlightthickness=0,background="#675454",foreground="#4ad607")
        upgradeHPText.place(relx=0.55, rely=0.28, anchor=tk.CENTER)
        upgradeSpeedText = tk.Message(main, text=UPGRADE.speedBuff, width=180,borderwidth=0,highlightthickness=0,background="#675454",foreground="#0051ca")
        upgradeSpeedText.place(relx=0.55, rely=0.38, anchor=tk.CENTER)
        upgradeAttackText = tk.Message(main, text=UPGRADE.damageBuff, width=180,borderwidth=0,highlightthickness=0,background="#675454",foreground="#e70000")
        upgradeAttackText.place(relx=0.55, rely=0.48, anchor=tk.CENTER)
        mainButtonUpgradeHP.config(command=lambda: UpgradeHPFunctionThread(main,mainButtonAttack,mainButtonGuard,PLAYER,ROUNDCOUNTER,mainButtonUpgradeHP,mainButtonUpgradeSpeed,mainButtonUpgradeAttack,upgradeHPText,upgradeSpeedText,upgradeAttackText,UPGRADE))
        mainButtonUpgradeSpeed.config(command=lambda: UpgradeSpeedFunctionThread(main,mainButtonAttack,mainButtonGuard,PLAYER,ROUNDCOUNTER,mainButtonUpgradeHP,mainButtonUpgradeSpeed,mainButtonUpgradeAttack,upgradeHPText,upgradeSpeedText,upgradeAttackText,UPGRADE))
        mainButtonUpgradeAttack.config(command=lambda: UpgradeAttackFunctionThread(main,mainButtonAttack,mainButtonGuard,PLAYER,ROUNDCOUNTER,mainButtonUpgradeHP,mainButtonUpgradeSpeed,mainButtonUpgradeAttack,upgradeHPText,upgradeSpeedText,upgradeAttackText,UPGRADE))
    def UpgradeHPFunction(main,mainButtonAttack,mainButtonGuard,PLAYER,ROUNDCOUNTER,mainButtonUpgradeHP,mainButtonUpgradeSpeed,mainButtonUpgradeAttack,upgradeHPText,upgradeSpeedText,upgradeAttackText,UPGRADE):
        mainButtonUpgradeHP.destroy()
        mainButtonUpgradeSpeed.destroy()
        mainButtonUpgradeAttack.destroy()
        upgradeHPText.destroy()
        upgradeSpeedText.destroy()
        upgradeAttackText.destroy()
        main.itemconfig("ROOT",image=pngMainScreenScaledRoot2)
        PLAYER.playerHP = PLAYER.playerHP+UPGRADE.heilung
        playerHP.config(text=PLAYER.playerHP)
        monsterHP.destroy()
        monsterSpeed.destroy()
        monsterDamage.destroy()
        monsterLevel.destroy()
        main.delete("MONSTER")
        
        gameGameThread = threading.Thread(target=Game(main,mainButtonAttack,mainButtonGuard,PLAYER,ROUNDCOUNTER))
        gameGameThread.start()
        
    def UpgradeSpeedFunction(main,mainButtonAttack,mainButtonGuard,PLAYER,ROUNDCOUNTER,mainButtonUpgradeHP,mainButtonUpgradeSpeed,mainButtonUpgradeAttack,upgradeHPText,upgradeSpeedText,upgradeAttackText,UPGRADE):
        mainButtonUpgradeHP.destroy()
        mainButtonUpgradeSpeed.destroy()
        mainButtonUpgradeAttack.destroy()
        upgradeHPText.destroy()
        upgradeSpeedText.destroy()
        upgradeAttackText.destroy()
        main.itemconfig("ROOT",image=pngMainScreenScaledRoot2)
        PLAYER.playerSpeed = PLAYER.playerSpeed+UPGRADE.speedBuff
        playerSpeed.config(text=PLAYER.playerSpeed)
        monsterHP.destroy()
        monsterSpeed.destroy()
        monsterDamage.destroy()
        monsterLevel.destroy()
        main.delete("MONSTER")
        
        gameGameThread = threading.Thread(target=Game(main,mainButtonAttack,mainButtonGuard,PLAYER,ROUNDCOUNTER))
        gameGameThread.start()
        
    def UpgradeAttackFunction(main,mainButtonAttack,mainButtonGuard,PLAYER,ROUNDCOUNTER,mainButtonUpgradeHP,mainButtonUpgradeSpeed,mainButtonUpgradeAttack,upgradeHPText,upgradeSpeedText,upgradeAttackText,UPGRADE):
        mainButtonUpgradeHP.destroy()
        mainButtonUpgradeSpeed.destroy()
        mainButtonUpgradeAttack.destroy()
        upgradeHPText.destroy()
        upgradeSpeedText.destroy()
        upgradeAttackText.destroy()
        main.itemconfig("ROOT",image=pngMainScreenScaledRoot2)
        PLAYER.playerDamage = PLAYER.playerDamage+UPGRADE.damageBuff
        playerDamage.config(text=PLAYER.playerDamage)
        monsterHP.destroy()
        monsterSpeed.destroy()
        monsterDamage.destroy()
        monsterLevel.destroy()
        main.delete("MONSTER")
        
        gameGameThread = threading.Thread(target=Game(main,mainButtonAttack,mainButtonGuard,PLAYER,ROUNDCOUNTER))
        gameGameThread.start()
        
    def UpgradeHPFunctionThread(main,mainButtonAttack,mainButtonGuard,PLAYER,ROUNDCOUNTER,mainButtonUpgradeHP,mainButtonUpgradeSpeed,mainButtonUpgradeAttack,upgradeHPText,upgradeSpeedText,upgradeAttackText,UPGRADE):
        gameGameUpgradeHPThread = threading.Thread(target=UpgradeHPFunction(main,mainButtonAttack,mainButtonGuard,PLAYER,ROUNDCOUNTER,mainButtonUpgradeHP,mainButtonUpgradeSpeed,mainButtonUpgradeAttack,upgradeHPText,upgradeSpeedText,upgradeAttackText,UPGRADE))
        gameGameUpgradeHPThread.start()
    def UpgradeSpeedFunctionThread(main,mainButtonAttack,mainButtonGuard,PLAYER,ROUNDCOUNTER,mainButtonUpgradeHP,mainButtonUpgradeSpeed,mainButtonUpgradeAttack,upgradeHPText,upgradeSpeedText,upgradeAttackText,UPGRADE):
        gameGameUpgradeSpeedThread = threading.Thread(target=UpgradeSpeedFunction(main,mainButtonAttack,mainButtonGuard,PLAYER,ROUNDCOUNTER,mainButtonUpgradeHP,mainButtonUpgradeSpeed,mainButtonUpgradeAttack,upgradeHPText,upgradeSpeedText,upgradeAttackText,UPGRADE))
        gameGameUpgradeSpeedThread.start()
    def UpgradeAttackFunctionThread(main,mainButtonAttack,mainButtonGuard,PLAYER,ROUNDCOUNTER,mainButtonUpgradeHP,mainButtonUpgradeSpeed,mainButtonUpgradeAttack,upgradeHPText,upgradeSpeedText,upgradeAttackText,UPGRADE):
        gameGameUpgradeAttackThread = threading.Thread(target=UpgradeAttackFunction(main,mainButtonAttack,mainButtonGuard,PLAYER,ROUNDCOUNTER,mainButtonUpgradeHP,mainButtonUpgradeSpeed,mainButtonUpgradeAttack,upgradeHPText,upgradeSpeedText,upgradeAttackText,UPGRADE))
        gameGameUpgradeAttackThread.start()
        
    
    mainButtonAttack.config(command=AttackThread)
    mainButtonGuard.config(command=GuardThread)
    mainButtonAttack.config(state="active")
    mainButtonGuard.config(state="active")
    
       
        
        
        
    
        
    
    
   
    

    
    
    
#Automated Thread Starts from other Functions
def ACKStartGame(main,console,mainButtonACK,mainButtonAttack,mainButtonGuard,PLAYER,ROUNDCOUNTER):
    console.destroy()
    mainButtonACK.destroy() 
    gameGameThread = threading.Thread(target=Game(main,mainButtonAttack,mainButtonGuard,PLAYER,ROUNDCOUNTER))
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
sys.exit()