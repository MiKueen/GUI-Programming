from tkinter import *

win = Tk()

win.geometry("400x500")
win.resizable(0, 0)

lb1 = Label(win, text="Enter Name:", font=("Arial", 15), fg="teal")
lb1.grid(row=0, column=0, pady=25, sticky=W)

en1 = Entry(win, font=("Arial", 15), fg="black")
en1.grid(row=0, column=1, pady=25)

lb2 = Label(win, text="Enter Password:", font=("Arial", 15), fg="teal")
lb2.grid(row=1, column=0, pady=25, sticky=W)

en2 = Entry(win, show="*", font=("Arial", 15), fg="black")
en2.grid(row=1, column=1, pady=25)

b1 = Button(win, text="Login", font=("Arial", 15), fg="black")
#columnspan=2 means merge 2 columns into 1
b1.grid(row=2, column=0, columnspan=2)

win.mainloop()
