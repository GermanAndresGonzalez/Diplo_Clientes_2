from tkinter import *
import webbrowser


def callback(url):
    webbrowser.open_new(url)


root = Tk()
link1 = Label(root, text="Enlace a Github", fg="blue", cursor="hand2")
link1.pack()
link1.bind("<Button-1>", lambda e: callback("https://github.com/GermanAndresGonzalez"))

link2 = Label(root, text="Correo electrónico", fg="blue", cursor="hand2")
link2.pack()
link2.bind("<Button-1>", lambda e: callback("gandresgonzalez@gmail.com"))

root.mainloop()
