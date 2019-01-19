from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("TIC-TAC-TOE-XOXO")

win.geometry("390x340")
win.resizable(0, 0)

c = 0
click = True
def show(b):
    global c
    c = c + 1
    global click
    if b["text"] == "" and click == True:
        b["text"] = "O"
        click = False
    elif b["text"] == "" and click == False:
        b["text"] = "X"
        click = True

    if (
            (b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X") or
            (b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X") or
            (b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X") or
            (b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X") or
            (b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X") or
            (b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X") or
            (b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X") or
            (b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X")
    ):
        messagebox.showinfo("Winner X", "Player X won!!")
        exit()

    elif (
                (b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O") or
                (b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O") or
                (b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O") or
                (b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O") or
                (b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O") or
                (b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O") or
                (b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O") or
                (b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O")
    ):
        messagebox.showinfo("Winner O", "Player 0 won!!")
        exit()

    elif c >= 9:
        messagebox.showinfo("Draw", "This is a draw. Wanna play again? :)")
        exit()

b1 = Button(win, text="", width=10, height=4, font=("Arial", 15, "bold"), fg="black", bg="teal", command=lambda: show(b1))
b1.grid(row=0, column=0)

b2 = Button(win, text="", width=10, height=4, font=("Arial", 15, "bold"), fg="black", bg="teal", command=lambda: show(b2))
b2.grid(row=0, column=1)

b3 = Button(win, text="", width=10, height=4, font=("Arial", 15, "bold"), fg="black", bg="teal", command=lambda: show(b3))
b3.grid(row=0, column=2)

b4 = Button(win, text="", width=10, height=4, font=("Arial", 15, "bold"), fg="black", bg="teal", command=lambda: show(b4))
b4.grid(row=1, column=0)

b5 = Button(win, text="", width=10, height=4, font=("Arial", 15, "bold"), fg="black", bg="teal", command=lambda: show(b5))
b5.grid(row=1, column=1)

b6 = Button(win, text="", width=10, height=4, font=("Arial", 15, "bold"), fg="black", bg="teal", command=lambda: show(b6))
b6.grid(row=1, column=2)

b7 = Button(win, text="", width=10, height=4, font=("Arial", 15, "bold"), fg="black", bg="teal", command=lambda: show(b7))
b7.grid(row=2, column=0)

b8 = Button(win, text="", width=10, height=4, font=("Arial", 15, "bold"), fg="black", bg="teal", command=lambda: show(b8))
b8.grid(row=2, column=1)

b9 = Button(win, text="", width=10, height=4, font=("Arial", 15, "bold"), fg="black", bg="teal", command=lambda: show(b9))
b9.grid(row=2, column=2)

win.mainloop()
