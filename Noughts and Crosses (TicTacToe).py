#!/usr/bin/python

from Tkinter import *
import tkMessageBox

tk = Tk()
tk.title("Noughts and Crosses")
tk.geometry('630x630')

turn = True
turnCounter = 0

# if True O has played, False X has played (used to check who won)

class squareButton(Button):
    def __init__(self, master=None, size=None, **kwargs):
        self.img = PhotoImage()
        Button.__init__(self, master, image=self.img, compound=CENTER, width=size, height=size, **kwargs)
# set buttons to contain empty image to make them square more easily


def resetGrid():
    global turnCounter, turn
    turnCounter = 0
    turn = True
    # reset turn counter and turn variable, set buttons back to default state

    b1.configure(text=" ", state='normal')
    b2.configure(text=" ", state='normal')
    b3.configure(text=" ", state='normal')
    b4.configure(text=" ", state='normal')
    b5.configure(text=" ", state='normal')
    b6.configure(text=" ", state='normal')
    b7.configure(text=" ", state='normal')
    b8.configure(text=" ", state='normal')
    b9.configure(text=" ", state='normal')
  

def checkWin():
    global turn, turnCounter
    if (b1["text"] == b2["text"] == b3["text"] and b1["state"] == b2["state"] == b3["state"] == 'disabled') or \
       (b4["text"] == b5["text"] == b6["text"] and b4["state"] == b5["state"] == b6["state"] == 'disabled') or \
       (b7["text"] == b8["text"] == b9["text"] and b7["state"] == b8["state"] == b9["state"] == 'disabled') or \
       (b1["text"] == b4["text"] == b7["text"] and b1["state"] == b4["state"] == b7["state"] == 'disabled') or \
       (b2["text"] == b5["text"] == b8["text"] and b2["state"] == b5["state"] == b8["state"] == 'disabled') or \
       (b3["text"] == b6["text"] == b9["text"] and b3["state"] == b6["state"] == b9["state"] == 'disabled') or \
       (b1["text"] == b5["text"] == b9["text"] and b1["state"] == b5["state"] == b9["state"] == 'disabled') or \
       (b3["text"] == b5["text"] == b7["text"] and b3["state"] == b5["state"] == b7["state"] == 'disabled'):
        # checks victory conditions, I could have made this shorter with a for loop by keeping the buttons in a list
        if turn:
            choice = tkMessageBox.askquestion("Winner!", "O Won!\nRematch?")
            if choice == 'no':
                tk.quit()
            else:
                resetGrid()
        else:
            choice = tkMessageBox.askquestion("Winner!", "X Won!\nRematch?")
            if choice == 'no':
                tk.quit()
            else:
                resetGrid()

    else:
        if turnCounter == 9:
            choice = tkMessageBox.askquestion("Draw!", "You drew!\nRematch?")
            if choice == 'no':
                tk.quit()
            else:
                resetGrid()
    # players have to play to the end for a draw

    
def click(button):
    global turn, turnCounter
    if turn:
        button.configure(text="X", font='Helvetica 96', disabledforeground='white')
        turnCounter += 1
        turn = False
        button.config(state='disabled')
        checkWin()

    else:
        button.configure(text="O", font='Helvetica 96', disabledforeground='white')
        turnCounter += 1
        turn = True
        button.config(state='disabled')
        checkWin()

        
b1 = squareButton(tk, text=' ', size=200, bg='black', fg='white', command=lambda: click(b1))
b2 = squareButton(tk, text=' ', size=200, bg='black', fg='white', command=lambda: click(b2))
b3 = squareButton(tk, text=' ', size=200, bg='black', fg='white', command=lambda: click(b3))
b4 = squareButton(tk, text=' ', size=200, bg='black', fg='white', command=lambda: click(b4))
b5 = squareButton(tk, text=' ', size=200, bg='black', fg='white', command=lambda: click(b5))
b6 = squareButton(tk, text=' ', size=200, bg='black', fg='white', command=lambda: click(b6))
b7 = squareButton(tk, text=' ', size=200, bg='black', fg='white', command=lambda: click(b7))
b8 = squareButton(tk, text=' ', size=200, bg='black', fg='white', command=lambda: click(b8))
b9 = squareButton(tk, text=' ', size=200, bg='black', fg='white', command=lambda: click(b9))
# defined buttons in main instead of in a class for ease of access

b1.grid(row=0, column=0, padx=2, pady=2)
b2.grid(row=0, column=1, padx=2, pady=2)
b3.grid(row=0, column=2, padx=2, pady=2)
b4.grid(row=1, column=0, padx=2, pady=2)
b5.grid(row=1, column=1, padx=2, pady=2)
b6.grid(row=1, column=2, padx=2, pady=2)
b7.grid(row=2, column=0, padx=2, pady=2)
b8.grid(row=2, column=1, padx=2, pady=2)
b9.grid(row=2, column=2, padx=2, pady=2)
# shaping the grid with a 2 pixel padding on each side

tk.mainloop()
