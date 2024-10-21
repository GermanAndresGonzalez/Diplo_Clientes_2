import tkinter as tk
from tkinter import LabelFrame, Label, Button
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image
import sqlite3
from librerias.creador_ini import leer_config
from prueba_vista import Ventana
from observador import Observer
from fabrica3 import FabricaWidgets

# from librerias.creador_ini import leer_config


class Ventana_login:

    def __init__(self, _root):
        self.root = _root  # Inicializar self.root
        self.imagenes = leer_config("imagenes")
        self.marco = leer_config("marco")
        self.titulo = leer_config("titulo")
        self.campos_etiquetas = leer_config("campos_etiquetas")
        self.nombre_campos = leer_config("nombre_campos_entradas")
        self.campos_entradas = leer_config("campos_entradas")
        self.botones = leer_config("botones")
        self.txt_login = leer_config("texto_login")
        self.texto_botones = leer_config("texto_botones")

        self.root.title("Pantalla de login")
        self.root.geometry("700x350")
        self.root.iconbitmap(self.imagenes["favicon_icon"])
        self.root.resizable(0, 0)

        self.marco_mayor = FabricaWidgets.crear_widget(
            "marco", self.root, width=700, height=350, **self.marco
        )
        self.marco_izq = FabricaWidgets.crear_widget(
            "marco",
            self.marco_mayor,
            width=300,
            height=345,
            borderwidth=1,
            **self.marco,
        )
        self.pinky = ImageTk.PhotoImage(Image.open(self.imagenes["imag_pinky"]))
        self.imagen_pinky = FabricaWidgets.crear_widget(
            "etiqueta",
            self.marco_izq,
            image=self.pinky,
            anchor="center",
            **self.campos_etiquetas,
        )

        self.imagen_pinky.place(x=50, y=10)

        self.marco_izq.place(x=0, y=0)
        self.marco_der = FabricaWidgets.crear_widget(
            "marco", self.marco_mayor, width=395, height=345, **self.marco
        )

        self.eti_usuario = FabricaWidgets.crear_widget(
            "etiqueta",
            self.marco_der,
            text=self.txt_login["usuario"],
            **self.campos_etiquetas,
        )
        self.eti_usuario.place(x=40, y=10, anchor=tk.NW)

        self.entrada_usuario = FabricaWidgets.crear_widget(
            "entrada", self.marco_der, **self.campos_entradas
        )
        self.entrada_usuario.place(x=20, y=50)

        self.eti_pass = FabricaWidgets.crear_widget(
            "etiqueta",
            self.marco_der,
            text=self.txt_login["contraseña"],
            **self.campos_etiquetas,
        )
        self.eti_pass.place(
            x=40,
            y=80,
            anchor=tk.NW,
        )

        self.entrada_pass = FabricaWidgets.crear_widget(
            "entrada", self.marco_der, show="*", **self.campos_entradas
        )
        self.entrada_pass.place(x=20, y=120)

        self.btn_login = FabricaWidgets.crear_widget(
            "boton",
            self.marco_der,
            text=self.txt_login["boton"],
            command=lambda: self.login(),
            ancho=15,
            **self.botones,
        )
        self.btn_login.place(x=20, y=200)

        self.btn_salir = FabricaWidgets.crear_widget(
            "boton",
            self.marco_der,
            text=self.texto_botones["salir"],
            command=lambda: self.root.destroy(),
            ancho=15,
            **self.botones,
        )
        self.btn_salir.place(x=180, y=200)

        self.marco_der.place(x=301, y=0)
        self.marco_mayor.place(x=0, y=0)

    def login(self):
        self.usuario = self.entrada_usuario.get()  # entrada_usuario
        self.contra = self.entrada_pass.get()

        self.conn = sqlite3.connect("clientes_nuevo.db")
        self.c = self.conn.cursor()
        self.c.execute(
            "SELECT * FROM usuarios WHERE nombre_usuario = ? AND contrasena = ?",
            (self.usuario, self.contra),
        )
        self.result = self.c.fetchone()

        if self.result:
            print("Login correcto")
            self.root.destroy()
            self.ventana = tk.Tk()
            self.objeto_vista = Ventana(self.ventana)
            self.ventana.mainloop()
            # self.mostrar_datos(self.result)

        else:
            self.root.messagebox.showerror("Login", "Usuario or contraseña inválidos")


if __name__ == "__main__":

    root = tk.Tk()
    aplicacion_login = Ventana_login(root)
    # obser = Observer(aplicacion_login.objeto_vista.objeto_acciones)
    root.mainloop()
    # Ventana_login()