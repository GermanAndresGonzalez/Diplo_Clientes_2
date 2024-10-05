"""from tkinter import *
import webbrowser


def callback(link):
    webbrowser.open_new(link)


root = Tk()
link = Label(
    root,
    text="Click to visit website",
    fg="blue",
    cursor="hand2",
)
link.bind("<Button-1>", callback("https://github.com/GermanAndresGonzalez"))
link.pack()
root.mainloop()

"""

import webbrowser
import tkinter as tk


my_w = tk.Tk()
my_w.geometry("400x200")

my_link = tk.Label(
    my_w,
    text="plus2net  Hyperlink",
    fg="blue",
    cursor="hand2",
    font=["Times", 22, "underline"],
)
my_link.grid(row=0, column=0, padx=20, pady=20)
my_link.bind(
    "<Button-1>",
    lambda e: webbrowser.open_new("https://github.com/GermanAndresGonzalez"),
)

my_w.mainloop()
