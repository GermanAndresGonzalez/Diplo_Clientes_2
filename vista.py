"""Módulo para la vista de la aplicación."""

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

# from tkinter.messagebox import showinfo
import datetime
from PIL import Image, ImageTk
from modelo import Abmc
from registro_errores import RegistroLogError
from referencia.estilos_treeview import estilo_tree
from referencia.referencia_treeview import referencia_tree

# from referencia.diccionario import diccionario
# from base_datos import ManejoBD


class Ventana:
    """Ventana Tkinter de la aplicación."""

    def __init__(self, windows, titulo="Clientes v1.00", geometria="1320x750"):

        self.root = windows

        self.root.title(titulo)
        self.root.geometry(geometria)
        self.menu()
        self.setup_widgets()
        # self.objeto_acciones = Abmc(self)

    def setup_widgets(self):
        self.ico = Image.open("referencia/favicon.png")
        self.foto = ImageTk.PhotoImage(self.ico)
        self.root.wm_iconphoto(False, self.foto)

        self.marco = LabelFrame(self.root, bg="#35374B")
        self.titulo = Label(
            self.marco,
            text="Administración de Clientes",
            bg="#78A083",
            fg="black",
            height=1,
            width=60,
            font=("Helvetica 16 bold"),
        )
        self.titulo.grid(row=0, column=1, columnspan=3, padx=1, pady=8, sticky="we")

        # Etiquetas y campos de entrada
        self.fuente_etiqueta = "Helvetica 12"
        etiquetas = [
            ("Indice", 1),
            ("Nombre de cliente", 2),
            ("Apellido", 3),
            ("Nombre del contacto", 4),
            ("Correo electrónico", 5),
            ("Número de telefono", 6),
            ("Sitio web", 7),
            ("Otro perfil", 8),
        ]

        for text, row in etiquetas:
            etiqueta = Label(
                self.marco,
                text=text,
                background="#35374B",
                fg="white",
                font=self.fuente_etiqueta,
            )
            etiqueta.grid(row=row, padx=5, pady=5, column=1, sticky="e")

        # Variables y campos de entrada
        self.var_indice = IntVar()
        self.var_nombre_cliente = StringVar()
        self.var_apellido_cliente = StringVar()
        self.var_contacto = StringVar()
        self.var_telefono = StringVar()
        self.var_sitio = StringVar()
        self.var_perfil = StringVar()
        self.var_correo_electronico = StringVar()

        variables = [
            (self.var_indice, 1, "disabled"),
            (self.var_nombre_cliente, 2, "normal"),
            (self.var_apellido_cliente, 3, "normal"),
            (self.var_contacto, 4, "normal"),
            (self.var_correo_electronico, 5, "normal"),
            (self.var_telefono, 6, "normal"),
            (self.var_sitio, 7, "normal"),
            (self.var_perfil, 8, "normal"),
        ]

        self.ancho_entry = 25
        self.fuente_entrada = "Helvetica 11 bold"
        for var, row, state in variables:
            entry = Entry(
                self.marco,
                font=self.fuente_entrada,
                textvariable=var,
                width=self.ancho_entry,
                state=state,
            )
            entry.grid(row=row, column=2, pady=5, sticky="we")

        # Configuración del Treeview
        self.setup_treeview()

        # Botones
        botones = [
            ("Agregar", 9, 1, self.agregar_cliente),
            ("Vaciar Entradas", 9, 2, self.vaciar),
            ("Borrar", 9, 3, self.borrar_cliente),
            ("Modificar", 10, 1, self.modificar_cliente),
            ("Importar Datos", 10, 2, self.importar_datos),
            ("Salir", 10, 3, self.root.quit),
        ]

        self.fuente_botones = "Helvetica 11 bold"
        for text, row, col, command in botones:
            boton = Button(
                self.marco,
                font=self.fuente_botones,
                text=text,
                background="#78A083",
                command=command,
            )
            boton.grid(row=row, column=col, padx=10, pady=10, sticky="we")
            boton.configure(width=35)

        self.marco.place(relx=0.5, rely=0.5, anchor="center")

    def setup_treeview(self):
        # Treeview style
        self.miestilo = ttk.Style()
        self.miestilo.theme_use("default")
        self.miestilo.configure(
            "miestilo.Treeview.Heading",
            font=("Helvetica 11 bold"),
            background="#78A083",
            foreground="white",
        )
        self.miestilo.configure(
            "Treeview",
            font=("Helvetica 11"),
            background="#4E5275",
            foreground="#bababa",
            fieldbackground="#D3D3D3",
        )
        self.miestilo.map("Treeview", background=[("selected", "#35374B")])

        # Define Treeview columns
        columnas = [
            ("ID", 60, "w"),
            ("Nombre", 150, ""),
            ("Tipo de Cliente", 120, ""),
            ("Contacto", 150, "w"),
            ("Correo-E", 230, ""),
            ("Teléfono", 150, ""),
            ("Sitio Web", 180, "w"),
            ("Otro Perfil", 230, "w"),
        ]

        self.tree = ttk.Treeview(
            self.marco,
            columns=[col[0] for col in columnas],
            show="headings",
            style="miestilo.Treeview",
        )

        for col, width, anchor in columnas:
            self.tree.column(
                col, width=width, minwidth=width, anchor=anchor if anchor else "w"
            )
            self.tree.heading(col, text=col)

        # Scrollbar
        self.barra_desplazamiento = Scrollbar(self.marco, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.barra_desplazamiento.set)
        self.tree.bind("<ButtonRelease-1>", self.seleccionar)
        self.tree.bind("<KeyRelease-Up>", self.seleccionar)
        self.tree.bind("<KeyRelease-Down>", self.seleccionar)
        # Layout Treeview
        self.tree.grid(row=12, column=0, columnspan=5, sticky="nsew")
        self.barra_desplazamiento.grid(row=12, column=5, sticky="ns")

    def hola(self):
        print("hola")

    def menu(self):
        menubar = Menu(self.root)
        menu_archivo = Menu(menubar, tearoff=0)
        menu_archivo.add_command(label="Importar", command=self.hola)
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
        menu_ayuda.add_command(label="Documentación", command=self.hola)
        menu_ayuda.add_command(label="Acerca de", command=self.hola)
        menubar.add_cascade(label="Ayuda", menu=menu_ayuda)
        self.root.config(menu=menubar)

    def ordener_col_por(self, col):
        """Ordena el Treeview al hacer 2 veces click en el encabezado elegido.

        Args:
            col (row): columna del treeview
        """

        # Obtener índice de la columna
        try:
            col_index = self.tree["columns"].index(col)

            # Cambiar orden si se hace clic en la misma columna
            if self.sort_column == col:
                self.sort_order *= -1
            else:
                self.sort_order = 1
                self.sort_column = col

            # Obtiene los artículos y ordena
            items = [
                (self.tree.item(item_id)["values"], item_id)
                for item_id in self.tree.get_children()
            ]
            items.sort(
                key=lambda x: self.ordenar_llave(x[0][col_index]),
                reverse=self.sort_order == -1,
            )
            # items.sort(key=lambda x: x[0][col_index], reverse=self.sort_order == -1)

            # Actualiza el  Treeview
            for index, (values, item_id) in enumerate(items):
                self.tree.move(item_id, "", index)

            # Actualiza encabezado de columna para mostrar indicador
            self.actualizar_encabezados()
        except TypeError as e:
            self.reg_errores = RegistroLogError(
                323, "Vista", datetime.datetime.now(), e
            )
            self.reg_errores.registrar_error()

    def ordenar_llave(self, valor):
        """Convierte los valores a un mismo tipo para ordenar."""
        try:
            # Intento convertir el valor a un float para su comparación
            return float(valor)
        except ValueError:
            # Si falla la conversión, el valor es una cadena
            return valor

    def actualizar_encabezados(self):
        """Actualiza encabezados de la columna para mostrar orden."""

        try:
            for col in self.tree["columns"]:
                heading_text = col
                if col == self.sort_column:
                    if self.sort_order == 1:
                        heading_text += " ▲"  # Ascendente
                    else:
                        heading_text += " ▼"  # Descendente
                self.tree.heading(col, text=heading_text)
        except Exception:
            self.reg_errores = RegistroLogError(337, "Vista", datetime.datetime.now())
            self.reg_errores.registrar_error()

    def seleccionar(self, event):
        """Hal hacer clic en el Treeview o mover las flechas se ve la información en los widgets de entrada.

        Args:
            event (seleccion): tecla de dirección o hacer clic.
        """
        try:
            item = self.tree.focus()
            valor2 = self.tree.item(item, "text")
            valores = self.tree.selection()

            valores = self.tree.item(item, "values")

            self.var_indice.set(valores[0])
            self.var_nombre_cliente.set(valores[1])
            self.var_apellido_cliente.set(valores[2])
            self.var_contacto.set(valores[3])
            self.var_correo_electronico.set(valores[4])
            self.var_telefono.set(valores[5])
            self.var_sitio.set(valores[6])
            self.var_perfil.set(valores[7])
        except Exception:
            self.reg_errores = RegistroLogError(361, "Vista", datetime.datetime.now())
            self.reg_errores.registrar_error()

    def vaciar(self):
        """Vacía los valores de los widget de entrada."""

        self.var_indice.set(0)
        self.var_nombre_cliente.set(" ")
        self.var_apellido_cliente.set(" ")
        self.var_contacto.set(" ")
        self.var_telefono.set(" ")
        self.var_sitio.set(" ")
        self.var_perfil.set(" ")
        self.var_correo_electronico.set(" ")
        self.objeto_acciones.cargar_treeview(self.tree)
