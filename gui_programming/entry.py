from tkinter import *

win = Tk()

win.minsize(500, 400)

# entry is basically for input
# here width represents no of characters
en = Entry(win, font=("Arial", 15), bg="blue", fg="white", width="12")
en.pack()

b1 = Button(win, text="CLICK MEE!!", font=("Arial", 15), fg="black")
b1.pack()

win.mainloop()
