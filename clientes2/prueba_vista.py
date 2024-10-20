import tkinter as tk
from tkinter import (
    ttk,
    LabelFrame,
    Label,
    IntVar,
    StringVar,
    Entry,
    Button,
    Scrollbar,
    Menu,
)
import webbrowser
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image
from os import getcwd
import sqlite3
from librerias.creador_ini import leer_config
from modelo import Abmc
from functools import partial
from librerias.acercade import Acercade

# from vista import Ventana
# from observador import Observer
from fabrica import FabricaWidgets

# from librerias.creador_ini import leer_config


class Ventana:

    def __init__(self, _root):
        self.root = _root
        self.imagenes = leer_config("imagenes")
        self.marco = leer_config("marco")
        self.txt_app = leer_config("aplicacion")
        self.campos_etiquetas = leer_config("campos_etiquetas")
        self.nombre_campos = leer_config("nombre_campos_entradas")
        self.campos_entradas = leer_config("campos_entradas")
        self.botones = leer_config("botones")
        self.txt_login = leer_config("texto_login")
        self.texto_botones = leer_config("texto_botones")
        self.titulo = leer_config("titulo")
        self.nombres_arbol = leer_config("col_treeview")
        self.datos_arbol = leer_config("val_treeview")
        self.col_cals = leer_config("val_col_treeview")
        # self.objeto_acciones = Abmc(self)
        self.objeto_acciones = Abmc(self)
        # self.root = tk_windows

        self.root.title(self.txt_app["titulo_p"])
        # self.title(self.txt_app["titulo_p"])
        # self.root.title(titulo)
        self.root.geometry(self.txt_app["geometria"])

        self.colocar_widgets()
        self.menu()

    def colocar_widgets(self):
        self.icono = Image.open(self.imagenes["favicon_icon"])
        self.foto = ImageTk.PhotoImage(self.icono)
        self.root.wm_iconphoto(False, self.foto)

        self.var_indice = IntVar()
        self.var_nombre_cliente = StringVar()
        self.var_apellido_cliente = StringVar()
        self.var_contacto = StringVar()
        self.var_telefono = StringVar()
        self.var_sitio = StringVar()
        self.var_perfil = StringVar()
        self.var_correo_electronico = StringVar()

        self.variables = [
            (self.var_indice, 1, "disabled"),
            (self.var_nombre_cliente, 2, "normal"),
            (self.var_apellido_cliente, 3, "normal"),
            (self.var_contacto, 4, "normal"),
            (self.var_correo_electronico, 5, "normal"),
            (self.var_telefono, 6, "normal"),
            (self.var_sitio, 7, "normal"),
            (self.var_perfil, 8, "normal"),
        ]

        self.marco_grande = FabricaWidgets.crear_widget(
            "marco",
            self.root,
            width=1320,
            height=750,
            borderwidth=1,
            **self.marco,
        )
        self.et_tit = FabricaWidgets.crear_widget(
            "etiqueta",
            self.marco_grande,
            padx=1,
            pady=1,
            **self.titulo,
        )
        self.et_tit.place(
            relx=0.5,
            rely=0.020,
            anchor="center",
        )

        self.contenedor = FabricaWidgets.crear_widget(
            "marco",
            self.marco_grande,
            borderwidth=1,
            relief="solid",
            width=1319,
            height=730,
            highlightbackground="#78A083",
            highlightthickness=2,
            **self.marco,
        )

        self.contenedor.columnconfigure(1, weight=1)
        self.contenedor.columnconfigure(2, weight=1)
        self.contenedor.columnconfigure(3, weight=1)

        for index, (key, value) in enumerate(self.nombre_campos.items()):
            self.etiqueta = FabricaWidgets.crear_widget(
                "etiqueta",
                self.contenedor,
                text=value,
                **self.campos_etiquetas,
            )
            self.etiqueta.grid(row=index, column=0, padx=1, pady=1)

            self.entrada = FabricaWidgets.crear_widget(
                "entrada",
                self.contenedor,
                textvariable=self.variables[index][0],
                **self.campos_entradas,
            )
            self.entrada.grid(row=index, column=1, padx=1, pady=1)
        self.contenedor.place(
            relx=0.5,
            rely=0.25,
            anchor="center",
        )
        self.marco_botones = FabricaWidgets.crear_widget(
            "marco",
            self.marco_grande,
            borderwidth=1,
            relief="solid",
            width=1300,
            height=330,
            highlightbackground="#78A083",
            highlightthickness=2,
            **self.marco,
        )

        for index, (key, value) in enumerate(self.texto_botones.items()):
            self.botonera = FabricaWidgets.crear_widget(
                "boton",
                self.marco_botones,
                text=value,
                width=30,
                command=self.root.destroy,
                **self.botones,
            )
            self.botonera.grid(row=index, column=0, padx=5, pady=5)

        self.marco_botones.place(
            relx=0.15,
            rely=0.25,
            anchor="center",
        )

        self.marco_arbol = FabricaWidgets.crear_widget(
            "marco",
            self.marco_grande,
            borderwidth=1,
            relief="solid",
            width=1300,
            height=330,
            highlightbackground="#78A083",
            highlightthickness=2,
            **self.marco,
        )

        self.estilo_arbol = ttk.Style()
        self.estilo_arbol.theme_use("default")
        self.estilo_arbol.configure(
            "Treeview",
            font=self.datos_arbol["fuente"],
            background=self.datos_arbol["background"],
            foreground=self.datos_arbol["foreground"],
            fieldbackground=self.datos_arbol["fieldbackground"],
        )
        self.estilo_arbol.configure(
            "Treeview.Heading",
            font=(self.datos_arbol["fuente_heading"]),
            background=self.datos_arbol["background_heading"],
            foreground=self.datos_arbol["foreground_heading"],
        )
        self.estilo_arbol.map(
            "Treeview",
            background=[("selected", self.datos_arbol["b_selected"])],
            foreground=[("selected", self.datos_arbol["f_selected"])],
        )

        cols = list(self.col_cals.values())
        self.columnas = []
        for index, (key, value) in enumerate(self.nombres_arbol.items()):
            self.columnas.append((value, cols[index], "w"))

        self.arbol_vista = FabricaWidgets.crear_widget(
            "arbol",
            self.marco_arbol,
            columns=[col[0] for col in self.columnas],
            show="headings",
            style="Treeview",
        )

        for col, width, anchor in self.columnas:
            self.arbol_vista.column(
                col, width=width, minwidth=width, anchor=anchor if anchor else "w"
            )
            self.arbol_vista.heading(col, text=col)
        self.arbol_vista.pack(expand=True, fill="both")

        self.marco_arbol.place(
            relx=0.5,
            rely=0.65,
            anchor="center",
        )

        self.marco_grande.pack(expand=True, fill="both")

    def ventana_acerca(self):
        acercade = Acercade()
        acercade.grab_set()

    def hola(self):
        print("hola")

    def abrir_documentacion(self):
        directorio = getcwd() + "/docs/build/html/index.html"
        print(directorio)
        webbrowser.open(directorio)

    def menu(self):
        menubar = Menu(self.root)
        menu_archivo = Menu(menubar, tearoff=0)
        menu_archivo.add_command(
            label="Importar",
            command=partial(self.objeto_acciones.importar_datos, self.arbol_vista),
        )
        menu_archivo.add_command(label="Exportar", command=self.hola)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.root.quit)
        menubar.add_cascade(label="Archivo", menu=menu_archivo)

        menu_tema = Menu(menubar, tearoff=0)
        menu_tema.add_command(label="Claro", command=self.hola)
        menu_tema.add_command(label="Oscuro", command=self.hola)
        # menu_tema.add_separator()
        # menu_tema.add_command(label="Cortar", command=master.quit)
        menubar.add_cascade(label="Temas", menu=menu_tema)

        menu_ayuda = Menu(menubar, tearoff=0)
        menu_ayuda.add_command(label="Documentación", command=self.abrir_documentacion)
        menu_ayuda.add_command(label="Acerca de", command=self.ventana_acerca)
        menubar.add_cascade(label="Ayuda", menu=menu_ayuda)
        self.root.config(menu=menubar)


if __name__ == "__main__":

    rut = tk.Tk()
    ventana_clientes = Ventana(rut)
    # obser = Observer(aplicacion_login.objeto_vista.objeto_acciones)
    rut.mainloop()
