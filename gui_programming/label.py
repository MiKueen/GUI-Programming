from tkinter import *

win = Tk()

win.minsize(500, 400)

#here height represents no of rows
lb = Label(win, text="Tkinter\nWindow", font=("Arial", 15), bg="blue", fg="red", width="10",  height="4")
lb.pack()

win.mainloop()
