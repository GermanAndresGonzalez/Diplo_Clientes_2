import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import os, sys, inspect
from openpyxl import load_workbook
from carpetas import obtAnterior

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from validacion import ValidacionCampos


class ExcelLoaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cargar y Validar Archivo Excel")
        self.root.geometry("800x600")
        self.inicial = obtAnterior("datos")
        self.validador = ValidacionCampos()

        self.boton_explorar = ttk.Button(
            root, text="Explorar Archivo Excel", command=self.cargar_archivo_excel
        )
        self.boton_explorar.pack(pady=10)

        self.lista_nombres = (
            "nombre",
            "apellido",
            "contacto",
        )
        self.lista_urls = ["sitio_web", "otro_perfil"]
        self.lista_correos = "correo_electronico"
        self.lista_telefonos = "telefono"

        self.tree = ttk.Treeview(root)
        self.tree.pack(expand=True, fill="both", padx=10, pady=10)

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
            self.mostrar_datos_en_treeview(df)
            self.validar_datos(df)

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo:\n{e}")

    def mostrar_datos_en_treeview(self, df):
        # Limpiar el Treeview
        self.tree.delete(*self.tree.get_children())

        # Configurar las columnas del Treeview
        self.tree["columns"] = list(df.columns)
        self.tree["show"] = "headings"
        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="w")

        # Insertar filas en el Treeview
        for _, row in df.iterrows():
            self.tree.insert("", "end", values=list(row))

    def validar_datos(self, df):
        self.error = True
        self.errores = []
        for i, fila in df.iterrows():
            for col in df.columns:
                if col in self.lista_nombres:
                    error = self.validador.validar_nombres(fila[col])
                    print(error, fila[col])
                    if error == False:
                        self.errores.append((i + 1, error))
                if col in self.lista_urls:
                    error = self.validador.sitios_web(fila[col], col)
                    print(error, fila[col])
                    if error == False:
                        self.errores.append((i + 1, error))
                if col in self.lista_correos:
                    error = self.validador.validar_correo(fila[col])
                    print(error, fila[col])
                    if error == False:
                        self.errores.append((i + 1, error))
                if col in self.lista_telefonos:
                    error = self.validador.validar_telefono(fila[col])
                    print(error, fila[col])
                    if error == False:
                        self.errores.append((i + 1, error))

        if self.errores:
            print(self.errores)


root = tk.Tk()
app = ExcelLoaderApp(root)
root.mainloop()
