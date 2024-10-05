import tkinter as tk
from tkinter import messagebox
import webbrowser

# from tkhtmlview import HTMLLabel


class Acercade(
    tk.Toplevel,
):
    """Ventana Acerca de la aplicación Clientes."""

    def __init__(
        self,
    ):
        super().__init__()
        self.fondo = "#35374B"
        # self.resizable(0, 0)
        self.iconbitmap("referencia/favicon.ico")
        self.geometry("600x300")
        self.title("Acerca de Clientes v1.00")

        self.fuente = ("Tahoma", 12, "bold")
        self.padx = padx = 5
        self.pady = pady = 5

        self.config(bg=self.fondo)

        self.label = tk.Label(
            self,
            text="Información de Clientes.\nVersión 1.00\nPráctica del Curso de Diplomatura en Python de la UTN.\nCreado por Germán Andrés González.\n",
            padx=self.padx,
            pady=self.pady,
            bg=self.fondo,
            font=self.fuente,
            fg="white",
        )
        self.label.pack(expand=True)
        self.link1 = tk.Label(
            self,
            text="https://github.com/GermanAndresGonzalez",
            fg="white",
            cursor="hand2",
            padx=self.padx,
            pady=self.pady,
            bg=self.fondo,
            font=self.fuente,
        )
        self.link1.pack(expand=True)
        self.link1.bind(
            "<Button-1>",
            lambda e: callback("https://github.com/GermanAndresGonzalez"),
        )
        self.correo = tk.Label(
            self,
            text="gandresgonzalez@gmail.com",
            fg="white",
            cursor="hand2",
            bg=self.fondo,
        )
        self.correo.pack(pady=20)
        self.correo.bind("<Button-1>", lambda e: open_mailto())
        # self.html_label.pack()
        self.button = tk.Button(self, text="Cerrar", command=self.destroy)
        self.button.pack(
            padx=self.padx,
            pady=self.pady,
            expand=True,
        )
        # self.button.pack(padx=10, pady=10, expand=True)

        def callback(url):
            webbrowser.open_new(url)

        def open_mailto():
            webbrowser.open(
                "mailto:gandresgonzalez@gmail.com?subject=ClientesApp&body=body"
            )

        def marco(self, altura, ancho):
            self.frame = ttk.Frame(self, altura, ancho)
            self.frame["padding"] = (left, top, right, bottom)
            self.frame["borderwidth"] = 5
            self.frame["relief"] = "ridge"
            # self.contenido_marco(frame)
            self.frame.pack(expand=True)
