from tkinter import *
import randomcolor

win = Tk()

win.minsize(500, 400)

def show():
    color = randomcolor.RandomColor()
    print("Event Handling Through Button")
    win.configure(background=color.generate())


b1 = Button(win, text="CLICK MEE!!", font=("Arial", 15), fg="black")
b1.config(command=show)
b1.pack(pady=100)

win.mainloop()
