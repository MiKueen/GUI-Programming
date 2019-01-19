from tkinter import *
import randomcolor

win = Tk()

win.minsize(500, 400)

def show(b):
    b["text"] = "SURPRISE!!"
    color = randomcolor.RandomColor()
    win.configure(background=color.generate())


b1 = Button(win, text="CLICK MEE!!", font=("Arial", 15), fg="black", command=lambda:show(b1))
b1.pack(pady=100)

win.mainloop()
