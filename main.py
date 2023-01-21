import tkinter

from env import Reversi
from tkinter import *


def start():
    grid_size_entry.forget()
    start_button_white.forget()
    start_button_black.forget()
    canvas = Canvas(window, width=1000, height=1000)
    canvas.pack()
    size = int(grid_size_entry.get())
    env = Reversi(size)
    env.render()


window = Tk()
window.configure(background='white')
window.title('Reversi')

grid_size_entry = Entry()

start_button_white = Button(text="Play as white", command=start)
start_button_black = Button(text="Play as black", command=start)
grid_size_entry.pack()
start_button_white.pack()
start_button_black.pack()
window.mainloop()

