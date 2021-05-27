import tkinter as tk
import random
from functools import partial


def clickity(r, c):
    print(r, c)


window = tk.Tk()
cell_width = 20
top_cell_height = 22
bottom_cell_height = 2
buttons = {}
for row in range(0, 2):
    for column in range(0,3):
        frame = tk.Frame(master=window)
        frame.grid(row=row, column=column)
        action = partial(clickity,row,column)
        if row == 0:
            cell_height = top_cell_height
        else:
            cell_height = bottom_cell_height
        button = tk.Button(
                master=frame,
                bg=random.choices(['red', 'blue', 'green', 'yellow', 'black']),
                command=action,
                text="(.)",
                width=cell_width,
                height=cell_height
            )
        button.pack()

window.mainloop()
