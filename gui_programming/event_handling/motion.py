from tkinter import *

win = Tk()

win.minsize(500, 400)

b1 = Button(win, text="CLICK MEE!!", font=("Arial", 15), fg="black")
x=1
def show(e):
    global x
    x = x + 1
    if(x % 2 == 0):
        win.configure(background="teal")
    else:
        win.configure(background="black")
b1.bind("<Motion>", show)
b1.pack(pady=100)

'''e1 = Entry(win, font=("Arial", 25))
e1.bind("<FocusIn>", lambda e:win.configure(background="cyan"))
e1.bind("<FocusOut>", lambda e:win.configure(background="teal"))
e1.pack(pady=50)
'''

win.mainloop()
