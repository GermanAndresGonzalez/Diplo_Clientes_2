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

        # Configuración inicial
        self.inicial = obtAnterior("datos")
        self.validador = ValidacionCampos()
        self.errores = []

        # Diccionario de listas para simplificar validaciones
        self.categorias_validacion = {
            "nombre": ("nombre", "apellido", "contacto"),
            "sitio_web": ("sitio_web", "otro_perfil"),
            "correo_electronico": ("correo_electronico",),
            "telefono": ("telefono",),
        }

        # Botón para explorar archivo
        self.boton_explorar = ttk.Button(
            root, text="Explorar Archivo Excel", command=self.cargar_archivo_excel
        )
        self.boton_explorar.pack(pady=10)

        # Treeview para mostrar datos
        self.tree = ttk.Treeview(root)
        self.tree.pack(expand=True, fill="both", padx=10, pady=10)

    def cargar_archivo_excel(self):
        # Abre el diálogo de selección de archivo
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
        # Configuración del Treeview y carga de datos
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = list(df.columns)
        self.tree["show"] = "headings"
        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="w")
        for _, row in df.iterrows():
            self.tree.insert("", "end", values=list(row))

    def validar_datos(self, df):
        # Limpia errores previos
        self.errores.clear()

        for i, fila in df.iterrows():
            for col in df.columns:
                # Inicializar error como None
                error = True
                valor = fila[col]

                # Determinar tipo de validación según la categoría de la columna
                if col in self.categorias_validacion["nombre"]:
                    error = self.validador.validar_nombres(valor)
                    if not error:
                        self.errores.append(
                            {"fila": i + 1, "columna": col, "error": error}
                        )
                elif col in self.categorias_validacion["sitio_web"]:
                    error = self.validador.sitios_web(valor, col)
                    if not error:
                        self.errores.append(
                            {"fila": i + 1, "columna": col, "error": error}
                        )
                elif col == "correo_electronico":
                    error = self.validador.validar_correo(valor)
                    if not error:
                        self.errores.append(
                            {"fila": i + 1, "columna": col, "error": error}
                        )
                elif col == "telefono":
                    error = self.validador.validar_telefono(valor)
                    if not error:
                        self.errores.append(
                            {"fila": i + 1, "columna": col, "error": error}
                        )

                # Agregar error con posición si existe

        # Mostrar errores en formato amigable
        if self.errores:
            errores_texto = "\n".join(
                [
                    f"Fila {err['fila']}, Columna {err['columna']}: {err['error']}"
                    for err in self.errores
                ]
            )
            messagebox.showwarning(
                "Errores de Validación", f"Se encontraron errores:\n{errores_texto}"
            )
        else:
            messagebox.showinfo("Validación Completa", "Todos los datos son válidos.")


# Configuración de la ventana principal
root = tk.Tk()
app = ExcelLoaderApp(root)
root.mainloop()
