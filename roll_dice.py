import tkinter as tk
import random

def roll():
    lbl_no["text"] = random.randint(1,6)

window = tk.Tk()
window.title("DICE simulator")
# window.columnconfigure(0, minsize=150)
# window.rowconfigure([0, 1], minsize=50)

btn_roll = tk.Button(text="Roll", command=roll)
lbl_no = tk.Label()

# btn_roll.grid(row=0, column=0, sticky="NSEW")
# lbl_no.grid(row=1, column=0, sticky="NSEW")

btn_roll.pack()
lbl_no.pack()

window.mainloop()