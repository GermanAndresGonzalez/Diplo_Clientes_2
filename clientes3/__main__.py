import tkinter as tk
import datetime

# from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3

from librerias.creador_ini import leer_config
from vista import Ventana

from base_datos import ManejoBD
from observador import Observer
from librerias.fabrica3 import FabricaWidgets
from registro import RegistroLogError

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
        self.marco = leer_config("marco")
        self.datos_arbol = leer_config("val_treeview")
        self.nombres_arbol = leer_config("usuarios")
        self.nombre_bd = "datos/clientes_nuevo.db"
        self.nombre_tabla = "usuarios"
        self.base_datos = ManejoBD()

        self.root.title("Pantalla de login")
        self.root.geometry("700x400")
        self.root.iconbitmap(self.imagenes["favicon_icon"])
        # self.root.resizable(0, 0)
        self.col_cals = leer_config("val_usuarios")
        self.marco_mayor = FabricaWidgets.crear_widget(
            "marco", self.root, width=700, height=400, **self.marco
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
            "marco", self.marco_mayor, width=395, height=400, **self.marco
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
            command=lambda: self.login(self.nombre_bd, self.nombre_tabla),
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

        self.eti_dat_log = FabricaWidgets.crear_widget(
            "etiqueta",
            self.marco_mayor,
            text=self.texto_etiqueta(self.nombre_bd, self.nombre_tabla),
            **self.campos_etiquetas,
        )
        self.eti_dat_log.place(x=300, y=250)

        self.marco_der.place(x=301, y=0)

        self.marco_mayor.place(x=0, y=0)

    def login(self, nombre_bd, nombre_tabla):
        self.usuario = self.entrada_usuario.get()  # entrada_usuario
        self.contra = self.entrada_pass.get()

        self.conn = sqlite3.connect(nombre_bd)
        self.c = self.conn.cursor()
        self.c.execute(
            f"SELECT * FROM {nombre_tabla} WHERE nombre_usuario = ? AND contrasena = ?",
            (self.usuario, self.contra),
        )
        self.result = self.c.fetchone()

        if self.result:
            login = True

            self.root.destroy()
            self.ventana = tk.Tk()
            self.objeto_vista = Ventana(self.ventana, self.usuario)
            self.ventana.mainloop()
            # self.mostrar_datos(self.result)

        else:
            tk.messagebox.showerror("Login", "Usuario o contraseña inválidos")
            login = False
        mensaje = "Login correcto"
        if not login:
            mensaje = "Login incorrecto"

        self.registro = RegistroLogError(
            130, "Login", 4, datetime.datetime.now(), self.usuario, mensaje
        )
        self.registro.registrar()

    def texto_etiqueta(self, nombre_bd, nombre_tabla):
        """Valores de las contraseñas."""
        # nombre_tabla = "personas"
        texto = "Usuario" + " " * 5 + "Contraseña\n"
        self.base_datos.conectar_bd(nombre_bd)
        for row in self.base_datos.cargar_datos(f"SELECT * FROM {nombre_tabla}"):
            for values in row[:2]:
                texto += str(values) + " " * 5
            texto += "\n"
        self.base_datos.cerrar_db()
        return texto


if __name__ == "__main__":

    root = tk.Tk()
    aplicacion_login = Ventana_login(root)
    # obser = Observer(aplicacion_login.objeto_vista.objeto_acciones)
    root.mainloop()
    # Ventana_login()
