import tkinter as tk
from tkinter import messagebox
import webbrowser
from PIL import ImageTk, Image
import os

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
        self.resizable(0, 0)
        self.iconbitmap("referencia/favicon.ico")
        self.geometry("700x300")
        self.title("Acerca de Clientes v1.00")

        self.fuente = ("Tahoma", 11, "bold")
        self.padx = 5
        self.pady = 5

        self.config(bg=self.fondo)
        self.marco()

    def etiquetas(self):
        self.label = tk.Label(
            self.marco3,
            text="Información de Clientes.\nVersión 1.00\nPráctica del Curso de Diplomatura en Python de la UTN.\nCreado por Germán Andrés González.\n",
            padx=self.padx,
            pady=self.pady,
            bg=self.fondo,
            font=self.fuente,
            fg="white",
        )
        self.label.pack(expand=True)
        self.link1 = tk.Label(
            self.marco3,
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
            self.marco3,
            text="gandresgonzalez@gmail.com",
            fg="white",
            cursor="hand2",
            bg=self.fondo,
            font=self.fuente,
        )
        self.correo.pack(pady=20)
        self.correo.bind("<Button-2>", lambda e: open_mailto())

        self.button = tk.Button(self.marco3, text="Cerrar", command=self.destroy)
        self.button.config(bg=self.fondo, fg="white")
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

    def marco(self):
        """Frame para la imagen y las etiquetas."""
        self.frame = tk.Frame(self, bg=self.fondo)

        self.frame["borderwidth"] = 1
        self.frame["relief"] = "flat"

        self.izquierdo()
        self.derecha()

    def izquierdo(self):
        """Marco para el logo."""
        self.marco2 = tk.Frame(
            self.frame,
            width=200,
            height=200,
            bg=self.fondo,
            borderwidth=1,
            relief="flat",
        )
        self.logo = ImageTk.PhotoImage(Image.open("referencia/pinky_011.png"))
        self.marco2 = tk.Label(
            self.frame, image=self.logo, bg=self.fondo, width=200, height=200
        )
        self.marco2.image = self.logo
        self.marco2.pack(side="left", expand="yes")

    def derecha(self):
        """Marco para las etiquetas."""
        self.marco3 = tk.Frame(
            self.frame,
            width=300,
            height=300,
            bg=self.fondo,
            borderwidth=1,
            relief="flat",
        )
        self.etiquetas()
        self.marco3.pack(side="right", expand=True)
        # self.contenido_marco(frame)
        self.frame.pack(expand=True)


if __name__ == "__main__":

    acercade = Acercade()
    acercade.mainloop()
