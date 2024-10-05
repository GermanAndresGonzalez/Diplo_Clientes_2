import tkinter as tk
import webbrowser


def open_mailto():
    webbrowser.open("mailto:example@example.com")


root = tk.Tk()
root.geometry("300x300")
root.title("Enlace Mailto en Tkinter")
marco = tk.Frame(
    root, width=300, height=300, bg="white", borderwidth=1, relief="groove"
)

correo = tk.Label(marco, text="Enviar correo", fg="blue", cursor="hand2")
correo.pack(pady=5)

correo.bind("<Button-1>", lambda e: open_mailto())
marco.pack(expand=True)
root.mainloop()
