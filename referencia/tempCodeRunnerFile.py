from tkinter import *
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

