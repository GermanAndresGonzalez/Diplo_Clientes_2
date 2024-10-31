import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import os, sys, inspect
from openpyxl import load_workbook
from librerias.carpetas import obtAnterior
from creador_ini import leer_config
from librerias.fabrica1 import FabricaWidgets, CreadorMultiple, CreadorEntradasMultiples
from collections import defaultdict


from validacion import ValidacionCampos
from vista import Ventana
from modelo import Abmc


class ExcelLoaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cargar y Validar Archivo Excel")
        geo = leer_config("aplicacion")["geometria"]
        self.root.geometry(geo)
        self.inicial = obtAnterior("datos")
        self.validador = ValidacionCampos()
        self.marco = leer_config("marco")
        self.campos_etiquetas = leer_config("campos_etiquetas")
        self.nombre_campos = leer_config("nombre_campos_entradas")
        self.categorias_validacion = {
            "nombre": ("nombre", "apellido", "contacto"),
            "sitio_web": ("sitio_web", "otro_perfil"),
            "correo_electronico": ("correo_electronico",),
            "telefono": ("telefono",),
        }
        self.nombres_arbol_viejo = leer_config("col_treeview")
        self.nombres_arbol = {
            k: v for i, (k, v) in enumerate(self.nombres_arbol_viejo.items()) if i != 0
        }

        self.datos_arbol = leer_config("val_treeview")
        self.col_cals = leer_config("val_col_treeview")

        self.lista_nombres = (
            "nombre",
            "apellido",
            "contacto",
        )
        self.lista_urls = ["sitio_web", "otro_perfil"]
        self.lista_correos = "correo_electronico"
        self.lista_telefonos = "telefono"
        self.marco_grande = FabricaWidgets.crear_widget(
            "marco",
            self.root,
            width=1320,
            height=750,
            borderwidth=1,
            **self.marco,
        )
        self.btn_login = FabricaWidgets.crear_widget(
            "boton",
            self.marco_grande,
            text="Explorar Archivo Excel",
            command=lambda: self.cargar_archivo_excel(),
            ancho=30,
        )
        self.btn_login.place(x=500, y=275, anchor="nw")

        Ventana.crear_arbol(
            self,
            self.marco_grande,
            self.marco,
            self.datos_arbol,
            self.nombres_arbol,
            self.col_cals,
            0.5,
            0.6,
            1300,
            750,
            barra=True,
        )
        self.marco_grande.place(
            relx=0.5,
            rely=0.15,
            anchor="center",
        )

    def seleccionar(self, event):
        pass

    def cargar_archivo_excel(self):

        file_path = filedialog.askopenfilename(
            title="Seleccionar archivo Excel",
            filetypes=[("Archivos Excel", "*.xlsx *.xls")],
            initialdir=self.inicial,
        )
        if not file_path:
            return
        try:
            df = pd.read_excel(file_path, dtype={"telefono": str})
            self.mostrar_datos_en_treeview(df, self.arbol_vista)
            self.validar_datos(df)

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo:\n{e}")

    def mostrar_datos_en_treeview(self, df, tree):
        # Limpiar el Treeview
        tree.delete(*tree.get_children())
        for _, row in df.iterrows():
            tree.insert("", "end", values=list(row))
        # Configurar las columnas del Treeview

        # Insertar filas en el Treeview

    def validar_datos(self, df):

        self.errores = []

        for i, fila in df.iterrows():
            for col in df.columns:
                # Inicializar error como None
                self.error = True
                valor = fila[col]

                # Determinar tipo de validación según la categoría de la columna
                if col in self.categorias_validacion["nombre"]:
                    self.error = self.validador.validar_nombres(valor)
                    if not self.error:
                        self.errores.append({i + 1: col})
                elif col in self.categorias_validacion["sitio_web"]:
                    self.error = self.validador.sitios_web(valor, col)
                    if not self.error:
                        self.errores.append({i + 1: col})
                elif col == "correo_electronico":
                    self.error = self.validador.validar_correo(valor)
                    if not self.error:
                        self.errores.append({i + 1: col})
                elif col == "telefono":
                    self.error = self.validador.validar_telefono(valor)
                    if not self.error:
                        self.errores.append({i + 1: col})

                # Agregar error con posición si existe

        # Mostrar errores en formato amigable
        if self.errores:
            collected_values = defaultdict(list)
            for d in self.errores:
                for key, value in d.items():
                    collected_values[key].append(value)
            diccionario = {k: ", ".join(v) for k, v in collected_values.items()}

        print(diccionario)


root = tk.Tk()
app = ExcelLoaderApp(root)
root.mainloop()
