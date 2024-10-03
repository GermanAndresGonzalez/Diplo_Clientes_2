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

    def __init__(self, windows):

        self.root = windows

        self.root.title("Clientes v1.01")
        self.root.geometry("1320x750")

        self.ico = Image.open("referencia/favicon.png")
        self.foto = ImageTk.PhotoImage(self.ico)
        self.root.wm_iconphoto(False, self.foto)

        # Usado para centrar los widgets:
        self.marco = LabelFrame(self.root, bg=estilo_tree["labelbg"])

        # Uso la etiqueta para como encabezado del programa
        self.titulo = Label(
            self.marco,
            text=estilo_tree["titulo_marco"],
            bg=estilo_tree["titulo_bg"],
            fg=estilo_tree["titulo_fg"],
            height=estilo_tree["titulo_height"],
            width=estilo_tree["titulo_width"],
            font=estilo_tree["titulo_font"],
        )
        self.titulo.grid(
            row=0, column=1, columnspan=3, padx=1, pady=8, sticky="w" + "E"
        )

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
            etiqueta.grid(row=row, padx=5, pady=5, column=1, sticky="E")

        self.var_indice = IntVar()
        self.var_nombre_cliente = StringVar()
        self.var_apellido_cliente = StringVar()
        self.var_contacto = StringVar()
        self.var_telefono = StringVar()
        self.var_sitio = StringVar()
        self.var_perfil = StringVar()
        self.var_correo_electronico = StringVar()

        self.ancho_entry = 25
        self.fuente_entrada = "Helvetica 11 bold"
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

        for var, row, state in variables:
            entry = Entry(
                self.marco,
                font=self.fuente_entrada,
                textvariable=var,
                width=self.ancho_entry,
                state=state,
            )
            entry.grid(row=row, column=2, pady=5, sticky="w" + "E")

        texto_etiqueta = referencia_tree["texto_etiquetas"]
        self.etiqueta_criterios_sitios = Label(
            self.marco,
            text=texto_etiqueta,
            background=estilo_tree["etiqueta_bg"],
            fg=estilo_tree["etiqueta_fg"],
            font=self.fuente_entrada,
        )
        self.etiqueta_criterios_sitios.grid(row=7, column=3, rowspan=2)

        self.fuente_botones = estilo_tree["fuente_botones"]
        botones = [
            (
                "Agregar",
                9,
                1,
                lambda: self.objeto_acciones.alta_cliente(
                    self.tree,
                    self.var_indice,
                    self.var_nombre_cliente.get(),
                    self.var_apellido_cliente.get(),
                    self.var_contacto.get(),
                    self.var_correo_electronico.get(),
                    self.var_telefono.get(),
                    self.var_sitio.get(),
                    self.var_perfil.get(),
                ),
            ),
            (
                "Vaciar Entradas",
                9,
                2,
                lambda: self.vaciar(),
            ),
            (
                "Borrar",
                9,
                3,
                lambda: self.objeto_acciones.borrar(self.tree),
            ),
            (
                "Modificar",
                10,
                1,
                lambda: self.objeto_acciones.actualizar(
                    self.tree,
                    self.var_indice.get(),
                    self.var_nombre_cliente.get(),
                    self.var_apellido_cliente.get(),
                    self.var_contacto.get(),
                    self.var_correo_electronico.get(),
                    self.var_telefono.get(),
                    self.var_sitio.get(),
                    self.var_perfil.get(),
                ),
            ),
            (
                "Importar Datos",
                10,
                2,
                lambda: self.objeto_acciones.importar_datos(self.tree),
            ),
            ("Salir", 10, 3, self.root.quit),
        ]

        for text, row, col, command in botones:
            boton = Button(
                self.marco,
                font=self.fuente_botones,
                text=text,
                background=estilo_tree["fondo_botones"],
                command=command,
            )
            boton.grid(row=row, column=col, padx=10, pady=10, sticky="w" + "E")
            boton.configure(width=35)

        self.miestilo = ttk.Style()
        self.miestilo.theme_use("default")
        self.miestilo.configure(
            "miestilo.Treeview.Heading",
            font=estilo_tree["fuente_headings"],
            fontcolor=estilo_tree["color_fuente"],
            background=estilo_tree["fondo_headings"],
        )
        self.miestilo.configure(
            "Treeview",
            font=estilo_tree["fuente_treeview"],
            background=estilo_tree["fondo_treeview"],
            foreground=estilo_tree["fore_treeview"],
            fieldbackground=estilo_tree["field_treeview"],
        )
        self.miestilo.map(
            "Treeview", background=[("selected", estilo_tree["seleccionado"])]
        )

        self.tree = ttk.Treeview(
            self.marco,
            columns=(
                "ID",
                "Nombre",
                "Apellido",
                "Contacto",
                "Correo-E",
                "Teléfono",
                "Sitio Web",
                "Otro Perfil",
            ),
            show="headings",
            style="miestilo.Treeview",
        )

        columnas = [
            ("ID", 60, "n"),
            ("Nombre", 80, "w"),
            ("Apellido", 80, "w"),
            ("Contacto", 140, "w"),
            ("Correo-E", 230, "w"),
            ("Teléfono", 150, "w"),
            ("Sitio Web", 170, "w"),
            ("Otro Perfil", 170, "w"),
        ]

        for col, width, anchor in columnas:
            self.tree.column(
                col, width=width, minwidth=width, anchor=anchor if anchor else "w"
            )

        self.tree.heading("ID", text="ID", command=lambda: self.ordener_col_por("ID"))
        self.tree.heading(
            "Nombre",
            text="Nombre",
            command=lambda: self.ordener_col_por("Nombre"),
        )
        self.tree.heading(
            "Apellido",
            text="Apellido",
            command=lambda: self.ordener_col_por("Apellido"),
        )
        self.tree.heading(
            "Contacto",
            text="Contacto",
            command=lambda: self.ordener_col_por("Contacto"),
        )
        self.tree.heading(
            "Correo-E",
            text="Correo-E",
            command=lambda: self.ordener_col_por("Correo-E"),
        )
        self.tree.heading(
            "Teléfono",
            text="Teléfono",
            command=lambda: self.ordener_col_por("Teléfono"),
        )
        self.tree.heading(
            "Sitio Web",
            text="Sitio Web",
            command=lambda: self.ordener_col_por("Sitio Web"),
        )
        self.tree.heading(
            "Otro Perfil",
            text="Otro Perfil",
            command=lambda: self.ordener_col_por("Otro Perfil"),
        )

        self.tree.grid(row=12, column=0, columnspan=5, sticky="nsew")
        self.barra_desplazamiento = Scrollbar(self.marco, command=self.tree.yview)
        self.barra_desplazamiento.grid(row=12, column=5, sticky="nsew")

        self.tree.configure(yscrollcommand=self.barra_desplazamiento.set)
        self.tree.bind("<ButtonRelease-1>", self.seleccionar)
        self.tree.bind("<KeyRelease-Up>", self.seleccionar)
        self.tree.bind("<KeyRelease-Down>", self.seleccionar)

        self.marco.place(relx=0.5, rely=0.5, anchor="center")
        self.objeto_acciones = Abmc(self)
        self.vaciar()
        self.sort_column = None
        self.sort_order = 1  # 1 para ascendente, -1 para descendente

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
