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
import datetime
import webbrowser
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image
from os import getcwd
import sqlite3
from librerias.creador_ini import leer_config
from modelo import Abmc
from functools import partial
from librerias.acercade import Acercade
from registro import RegistroLogError

# from vista import Ventana
# from observador import Observer

from librerias.fabrica3 import FabricaWidgets, CreadorMultiple, CreadorEntradasMultiples

# from librerias.creador_ini import leer_config


class Ventana:

    def __init__(self, _root, usuario):
        self.root = _root
        self.usuario = usuario
        print(self.usuario)
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
        self.objeto_acciones.cargar_treeview(
            self.arbol_vista, "datos/clientes_nuevo.db", "personas"
        )
        self.llenar_entradas()

    def colocar_widgets(self):
        self.comandos = {
            "agregar": lambda: self.root.destroy(),
            "vaciar": lambda: self.vaciar(),
            "borrar": lambda: self.hola(),
            "modificar": lambda: self.hola(),
            "importar": lambda: self.hola(),
            "salir": lambda: self.root.destroy(),
        }
        self.estados = {
            0: "readonly",
            1: "normal",
            2: "normal",
            3: "normal",
            4: "normal",
            5: "normal",
            6: "normal",
            7: "normal",
        }
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

        self.marco_grande = FabricaWidgets.crear_widget(
            "marco",
            self.root,
            width=1400,
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
            rely=0.03,
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

        self.etiquetas = CreadorMultiple.crear_multiples_widgets(
            "etiqueta",
            self.contenedor,
            1,
            0,
            self.nombre_campos,
            **self.campos_etiquetas,
        )

        self.entradas = CreadorEntradasMultiples.crear_multiples_widgets(
            "entrada",
            self.contenedor,
            1,
            1,
            self.nombre_campos,
            self.estados,
            vertical=True,
            **self.campos_entradas,
        )

        self.llenar_entradas()

        self.contenedor.place(
            relx=0.5,
            rely=0.26,
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
        self.botonera = CreadorMultiple.crear_multiples_widgets(
            "boton",
            self.marco_botones,
            2,
            1,
            textos=self.texto_botones,
            vertical=True,
            acciones=self.comandos,
            **self.botones,
        )

        self.marco_botones.place(
            relx=0.15,
            rely=0.25,
            anchor="center",
        )

        self.crear_arbol(
            self.marco_grande,
            self.marco,
            self.datos_arbol,
            self.nombres_arbol,
            self.col_cals,
            0.5,
            0.66,
            marcox=1370,
            marcoy=530,
            barra=True,
        )
        self.marco_grande.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
        )

    def ventana_acerca(self):
        acercade = Acercade()
        acercade.grab_set()

    def hola(self):
        print("hola")

    def llenar_entradas(
        self,
    ):

        self.entradas["indice"].config

        for index, (key, value) in enumerate(self.entradas.items()):
            value.delete(0, "end")
            value.insert(0, self.nombre_campos[key])
        self.entradas["indice"].config(state="normal")
        self.entradas["indice"].delete(0, "end")
        self.entradas["indice"].insert(0, 0)
        self.entradas["indice"].config(state="readonly")
        # self.entradas["indice"].config(state="normal")

    def abrir_documentacion(self):
        directorio = getcwd() + "/docs/build/html/index.html"
        print(directorio)
        webbrowser.open(directorio)

    def crear_arbol(
        self,
        marco_contenedor,
        marco,
        datos_arbol,
        nombres_arbol,
        col_cals,
        x,
        y,
        marcox,
        marcoy,
        barra=True,
    ):
        self.marco_arbol = FabricaWidgets.crear_widget(
            "marco",
            marco_contenedor,
            borderwidth=1,
            relief="solid",
            width=marcox,
            height=marcoy,
            highlightbackground="#78A083",
            highlightthickness=2,
            **marco,
        )

        self.estilo_arbol = ttk.Style()
        self.estilo_arbol.theme_use("default")
        self.estilo_arbol.configure(
            "Treeview",
            font=datos_arbol["fuente"],
            background=datos_arbol["background"],
            foreground=datos_arbol["foreground"],
            fieldbackground=datos_arbol["fieldbackground"],
        )
        self.estilo_arbol.configure(
            "Treeview.Heading",
            font=(datos_arbol["fuente_heading"]),
            background=datos_arbol["background_heading"],
            foreground=datos_arbol["foreground_heading"],
        )
        self.estilo_arbol.map(
            "Treeview",
            background=[("selected", datos_arbol["b_selected"])],
            foreground=[("selected", datos_arbol["f_selected"])],
        )

        cols = list(col_cals.values())
        self.columnas = []
        for index, (key, value) in enumerate(nombres_arbol.items()):
            self.columnas.append((value, cols[index], "w"))

        self.arbol_vista = FabricaWidgets.crear_widget(
            "arbol",
            self.marco_arbol,
            columns=[col[0] for col in self.columnas],
            show="headings",
            style="Treeview",
            selectmode="browse",
        )

        for col, width, anchor in self.columnas:
            self.arbol_vista.column(
                col, width=width, minwidth=width, anchor=anchor if anchor else "w"
            )
            self.arbol_vista.heading(col, text=col)

        self.barra_desplazamiento = (
            Scrollbar(
                self.marco_arbol, orient="vertical", command=self.arbol_vista.yview
            )
            if barra
            else False
        )
        self.barra_desplazamiento.pack(side="right", fill="y") if barra else False
        (
            self.arbol_vista.configure(yscrollcommand=self.barra_desplazamiento.set)
            if barra
            else False
        )
        self.arbol_vista.bind("<ButtonRelease-1>", self.seleccionar)
        self.arbol_vista.bind("<KeyRelease-Up>", self.seleccionar)
        self.arbol_vista.bind("<KeyRelease-Down>", self.seleccionar)
        self.arbol_vista.pack()  # expand=True, fill="both")
        self.marco_arbol.place(
            relx=x,
            rely=y,
            anchor="center",
        )

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

    def seleccionar(self, event):
        """Hal hacer clic en el Treeview o mover las flechas se ve la información en los widgets de entrada.

        Args:
            event (seleccion): tecla de dirección o hacer clic.
        """
        try:
            item = self.arbol_vista.focus()
            # valor2 = self.arbol_vista.item(item, "text")
            valores = self.arbol_vista.selection()

            valores = self.arbol_vista.item(item, "values")
            self.entradas["indice"].config(state="normal")
            for index, (key, value) in enumerate(self.entradas.items()):
                value.delete(0, "end")
                value.insert(0, valores[index])

            self.entradas["indice"].config(state="readonly")

        except Exception:
            self.reg_errores = RegistroLogError(361, "Vista", datetime.datetime.now())
            self.reg_errores.registrar()

    def vaciar(self):
        """Vacía los valores de los widget de entrada."""

        self.entradas["indice"].config(state="normal")
        for index, (key, value) in enumerate(self.entradas.items()):
            value.delete(0, "end")
            value.insert(0, "")
        self.entradas["indice"].insert(0, 0)
        self.entradas["indice"].config(state="readonly")
        self.objeto_acciones.cargar_treeview(
            self.arbol_vista, "datos/clientes_nuevo.db", "personas"
        )


if __name__ == "__main__":

    rut = tk.Tk()
    ventana_clientes = Ventana(rut)
    # obser = Observer(aplicacion_login.objeto_vista.objeto_acciones)
    rut.mainloop()
