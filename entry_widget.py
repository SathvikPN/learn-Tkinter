# Write a complete script that displays an Entry widget that’s 40 text units wide 
# and has a white background and black text. Use .insert() to display text in the widget 
# that reads "What is your name?".

import tkinter as tk

window = tk.Tk()

txt = tk.Entry(
    width=40,
    bg="white",
    fg="black",
)

txt.insert(0, "What is your name?")
txt.pack()

window.mainloop()