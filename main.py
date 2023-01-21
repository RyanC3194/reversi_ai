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
            empty_button = tk.Button(master=frame, text=f"", command=lambda row=i, col=j: click(row, col), width=10, height=3, bg="gray", fg="black")
            #empty_button = tk.Button(master=frame, text=f"", image=photo_image)
            #empty_button = tk.Button(master=frame, text="%s,%s" % (row, col), command=lambda row=row, col=col: click(row, col))
            #button.grid(row=row, column=col, sticky="nsew")
            #label = tk.Label(window, text="")
            #label.grid(row=8, column=0, columnspan=8, sticky="new")
            empty_button.pack()

    #window.grid_rowconfigure(8, weight=1)
    #window.grid_columnconfigure(8, weight=1)
            
    white_button = tk.Button(master=frame, text=f"", width=10, height=3, bg="white", fg="black")
    black_button = tk.Button(master=frame, text=f"", width=10, height=3, bg="black", fg="black")
    pass

window = tk.Tk()
window.configure(background='white')
window.title('Reversi')

def click(row, col):
    print(row, col)
    tk.Label.configure(text="you clicked row %s column %s" % (row, col))
    x = row
    y = col
    
'''
for row in range(8):
    for col in range(8):
        button = tk.Button(window, text="%s,%s" % (row, col), 
                           command=lambda row=row, col=col: click(row, col))
        button.grid(row=row, column=col, sticky="nsew")
label = tk.Label(window, text="")
label.grid(row=8, column=0, columnspan=8, sticky="new")

window.grid_rowconfigure(8, weight=1)
window.grid_columnconfigure(8, weight=1)
'''

#grid_size_entry = Entry()

start_button_white = tk.Button(text="Play as white", command=start)
start_button_black = tk.Button(text="Play as black", command=start)
#grid_size_entry.pack()
start_button_white.pack()
start_button_black.pack()

window.mainloop()

