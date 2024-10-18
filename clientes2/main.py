import tkinter as tk
from PIL import ImageTk, Image
import sqlite3
from librerias.creador_ini import leer_config

# from librerias.creador_ini import leer_config


class WidgetFactory:
    @staticmethod
    def crear_widget(tipo_widget, master, **kwargs):
        if tipo_widget == "entrada":
            return tk.Entry(master, **kwargs)
        elif tipo_widget == "etiqueta":
            return tk.Label(master, **kwargs)
        elif tipo_widget == "boton":
            return tk.Button(master, **kwargs)
        elif tipo_widget == "marco":
            return tk.Frame(master, **kwargs)
        else:
            raise ValueError(f"Tipo de widget desconocido: {tipo_widget}")


class Ventana_login:

    def __init__(self):
        self.imagenes = leer_config("imagenes")
        self.marco = leer_config("marco")
        self.titulo = leer_config("titulo")
        self.campos_etiquetas = leer_config("campos_etiquetas")
        self.nombre_campos = leer_config("nombre_campos_entradas")
        self.campos_entradas = leer_config("campos_entradas")
        self.botones = leer_config("botones")
        self.txt_login = leer_config("texto_login")
        self.texto_botones = leer_config("texto_botones")

        self.root = tk.Tk()
        self.root.title("Pantalla de login")
        self.root.geometry("700x350")
        self.root.iconbitmap(self.imagenes["favicon_icon"])
        self.root.resizable(0, 0)

        self.marco_mayor = WidgetFactory.crear_widget(
            "marco", self.root, width=700, height=350, **self.marco
        )
        self.marco_izq = WidgetFactory.crear_widget(
            "marco",
            self.marco_mayor,
            width=300,
            height=345,
            borderwidth=1,
            **self.marco,
        )
        self.pinky = ImageTk.PhotoImage(Image.open(self.imagenes["imag_pinky"]))
        self.imagen_pinky = WidgetFactory.crear_widget(
            "etiqueta",
            self.marco_izq,
            image=self.pinky,
            anchor="center",
            **self.campos_etiquetas,
        )

        self.imagen_pinky.place(x=50, y=10)

        self.marco_izq.place(x=0, y=0)
        self.marco_der = WidgetFactory.crear_widget(
            "marco", self.marco_mayor, width=395, height=345, **self.marco
        )

        self.eti_usuario = WidgetFactory.crear_widget(
            "etiqueta",
            self.marco_der,
            text=self.txt_login["usuario"],
            **self.campos_etiquetas,
        )
        self.eti_usuario.place(x=40, y=10, anchor=tk.NW)

        self.entrada_usuario = WidgetFactory.crear_widget(
            "entrada", self.marco_der, **self.campos_entradas
        )
        self.entrada_usuario.place(x=20, y=50)

        self.eti_pass = WidgetFactory.crear_widget(
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

        self.entrada_pass = WidgetFactory.crear_widget(
            "entrada", self.marco_der, show="*", **self.campos_entradas
        )
        self.entrada_pass.place(x=20, y=120)

        self.btn_salir = WidgetFactory.crear_widget(
            "boton",
            self.marco_der,
            text=self.txt_login["boton"],
            command=lambda: self.root.destroy(),
            width=15,
            **self.botones,
        )
        self.btn_salir.place(x=20, y=200)

        self.btn_salir = WidgetFactory.crear_widget(
            "boton",
            self.marco_der,
            text=self.texto_botones["salir"],
            command=lambda: self.root.destroy(),
            width=15,
            **self.botones,
        )
        self.btn_salir.place(x=180, y=200)

        self.marco_der.place(x=301, y=0)
        self.marco_mayor.place(x=0, y=0)
        self.root.mainloop()

    def login(self):
        self.usuario = self.usuario_entry.get()
        self.contra = self.contra_entry.get()

        self.conn = sqlite3.connect("clientes_nuevo.db")
        self.c = self.conn.cursor()
        c.execute(
            "SELECT * FROM usuarios WHERE nombre_usuario = ? AND contrasena = ?",
            (self.usuario, self.contra),
        )
        self.result = self.c.fetchone()

        if self.result:
            self.mostrar_datos(self.result)

        else:
            self.messagebox.showerror("Login", "Usuario or contraseña inválidos")


if __name__ == "__main__":
    Ventana_login()
