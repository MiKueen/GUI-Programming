from tkinter import *

win = Tk()
win.minsize(500, 400)

x = DoubleVar()
y = DoubleVar()
z = DoubleVar()

lb1 = Label(win, text="Number 1:", font=("Arial", 15), fg="black")
lb1.pack(pady=25)
e1 = Entry(win, font=("Arial", 25), textvariable=x)
e1.pack(pady=5)

lb2 = Label(win, text="Number 2:", font=("Arial", 15), fg="black")
lb2.pack(pady=10)
e2 = Entry(win, font=("Arial", 25), textvariable=y)
e2.pack(pady=5)

def show():
    a = x.get()
    b = y.get()
    c = a + b
    z.set(c)

b1 = Button(win, text="Result!!", font=("Arial", 15), fg="black", command=show)
b1.pack(pady=20)

e3 = Entry(win, font=("Arial", 25), textvariable=z)
e3.pack(pady=10)

win.mainloop()
