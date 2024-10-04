import tkinter as tk
from tkinter import messagebox


def show_about():
    about_window = tk.Toplevel(root)
    about_window.title("About")
    about_window.geometry("300x200")

    label = tk.Label(
        about_window, text="This is an About window.\nYour App v1.0", padx=10, pady=10
    )
    label.pack(expand=True)

    button = tk.Button(about_window, text="Close", command=about_window.destroy)
    button.pack(pady=10)


root = tk.Tk()
root.title("Main Window")
root.geometry("400x300")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=show_about)

root.mainloop()
