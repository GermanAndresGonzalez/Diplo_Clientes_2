from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
img = ImageTk.PhotoImage(Image.open("referencia/pinky_01.png"))
panel = Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")
root.mainloop()
