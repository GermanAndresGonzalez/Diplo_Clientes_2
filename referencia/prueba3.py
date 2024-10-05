import tkinter as tk
import webbrowser


def open_mailto():
    webbrowser.open("mailto:example@example.com")


root = tk.Tk()
root.title("Enlace Mailto en Tkinter")

correo = tk.Label(root, text="Enviar correo", fg="blue", cursor="hand2")
correo.pack(pady=20)

correo.bind("<Button-1>", lambda e: open_mailto())

root.mainloop()
