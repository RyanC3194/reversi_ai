import tkinter
from PIL import Image, ImageTk
from env import Reversi
import tkinter as tk


def start():

    start_button_white.forget()
    start_button_black.forget()
    size = 8
    env = Reversi(size)
    image = Image.open(r'C:\Users\elisa\Pictures\greenbg.png')
    image = image.resize((10, 10))
    photo_image = ImageTk.PhotoImage(image)

    for i in range(8):
        for j in range(8):
            frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
            frame.grid(row=i, column=j, padx=5, pady=5)
            #empty_button = Button(master=frame, text=f"", width=10, height=3, bg="gray", fg="black")
            empty_button = tk.Button(master=frame, text=f"", image=photo_image)
            empty_button.pack()

    white_button = tk.Button(master=frame, text=f"", width=10, height=3, bg="white", fg="black")
    black_button = tk.Button(master=frame, text=f"", width=10, height=3, bg="black", fg="black")

"""
 def press_empty():
   x = 
   y =         
"""

window = tk.Tk()
window.configure(background='white')
window.title('Reversi')

#grid_size_entry = Entry()

start_button_white = tk.Button(text="Play as white", command=start)
start_button_black = tk.Button(text="Play as black", command=start)
#grid_size_entry.pack()
start_button_white.pack()
start_button_black.pack()

window.mainloop()
