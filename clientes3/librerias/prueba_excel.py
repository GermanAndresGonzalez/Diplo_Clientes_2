import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import os, sys, inspect
from openpyxl import load_workbook
from carpetas import obtAnterior
from creador_ini import leer_config
from fabrica1 import FabricaWidgets, CreadorMultiple, CreadorEntradasMultiples

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
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

        self.nombres_arbol_viejo = leer_config("col_treeview")
        self.nombres_arbol = {
            k: v for i, (k, v) in enumerate(self.nombres_arbol_viejo.items()) if i != 0
        }
        self.nombres_arbol["Error"] = "Error"
        self.datos_arbol = leer_config("val_treeview")
        self.col_cals = leer_config("val_col_treeview")
        print(self.nombre_campos)
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
            width=1400,
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
            marco_contenedor=self.marco_grande,
            marco=self.marco,
            datos_arbol=self.datos_arbol,
            nombres_arbol=self.nombres_arbol,
            col_cals=self.col_cals,
            x=0.5,
            y=0.6,
            marcox=1370,
            marcoy=530,
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
            df = pd.read_excel(file_path)
            self.mostrar_datos_en_treeview(df, self.arbol_vista)
            self.validar_datos(df, self.arbol_vista)

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo:\n{e}")

    def mostrar_datos_en_treeview(self, df, tree):
        # Limpiar el Treeview
        tree.delete(*tree.get_children())
        for _, row in df.iterrows():
            tree.insert("", "end", values=list(row))
        # Configurar las columnas del Treeview

        # Insertar filas en el Treeview

    def validar_datos(self, df, tree):
        self.error = True
        self.errores = []
        for i, fila in df.iterrows():
            for col in df.columns:
                if col in self.lista_nombres:
                    error = self.validador.validar_nombres(fila[col])
                    print(error, fila[col])
                    if error == False:
                        sself.errores.append((i, error, col, fila[col]))

                if col in self.lista_urls:
                    error = self.validador.sitios_web(fila[col], col)
                    print(error, fila[col])
                    if error == False:
                        self.errores.append((i, error, col, fila[col]))
                if col in self.lista_correos:
                    error = self.validador.validar_correo(fila[col])
                    print(error, fila[col])
                    if error == False:
                        self.errores.append((i, error, col, fila[col]))
                if col in self.lista_telefonos:
                    error = self.validador.validar_telefono(fila[col])
                    print(error, fila[col])
                    if error == False:
                        self.errores.append((i, error, col, fila[col]))

        if self.errores:
            print(self.errores)
            # tree.insert("", "end", values="Error")
            for i, error, col, fila in self.errores:
                # tree.set(f"{i-1}", "Error", f"{error}")
                print(tree.get_children(f"{i}"))


root = tk.Tk()
app = ExcelLoaderApp(root)
root.mainloop()
