import tkinter as tk
class TITLE:
    def __init__(self):
        self.TKINTERSTARTWINDOW = tk.Tk()
        self.TKINTERSTARTWINDOW.overrideredirect(True)
        x = int (self.TKINTERSTARTWINDOW.winfo_screenwidth() / 4)
        y = int (self.TKINTERSTARTWINDOW.winfo_screenheight() / 8)
        self.TKINTERSTARTWINDOW.geometry("1280x1024+{}+{}".format(x,y))
    def PASSBUFFER(self):
        pass
    def TKINTERSTARTWINDOWLOGIC(self):
        self.TKINTERSTARTWINDOW.protocol("WM_DELETE_WINDOW", self.PASSBUFFER)
        self.CANVAS = tk.Canvas(self.TKINTERSTARTWINDOW,borderwidth=0,highlightthickness=0,background="#000000")
        self.CANVAS.place(relheight=1,relwidth=1,relx=0.5,rely=0.5,anchor=tk.CENTER)
        self.TITLEPNG = tk.PhotoImage(file="bin/assets/GameEssential/SoulWoodsTitle.png")
        self.TITLEPNGSCALED = self.TITLEPNG.subsample(2,2)
        self.CANVAS.create_image(640,512,image=self.TITLEPNGSCALED, anchor=tk.CENTER)
        self.TKINTERSTARTWINDOW.after(5000, self.TKINTERSTARTWINDOW.destroy)
        self.TKINTERSTARTWINDOW.mainloop()      