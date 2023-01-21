import tkinter

from env import Reversi
from tkinter import *


def start():

    start_button_white.forget()
    start_button_black.forget()
    size = 8
    env = Reversi(size)
    greenbg = PhotoImage(file = r"C:\Users\elisa\Pictures\greenbg.png")
    greenbg.subsample(1, 2)


    for i in range(8):
        for j in range(8):
            frame = Frame(master=window, relief=RAISED, borderwidth=1)
            frame.grid(row=i, column=j, padx=5, pady=5)
            
            empty_button = Button(master=frame, text="", image=greenbg)
            empty_button.pack()


window = Tk()
window.configure(background='white')
window.title('Reversi')

#grid_size_entry = Entry()

start_button_white = Button(text="Play as white", command=start)
start_button_black = Button(text="Play as black", command=start)
#grid_size_entry.pack()
start_button_white.pack()
start_button_black.pack()

empty_grid_button = Button(text="", width=25, height=5, bg="white", fg="black")



window.mainloop()
