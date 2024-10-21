import tkinter as tk
from tkinter import ttk, LabelFrame, Label, Entry, Button


class FabricaWidgets:
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
        elif tipo_widget == "arbol":
            return ttk.Treeview(master, **kwargs)
        else:
            raise ValueError(f"Tipo de widget desconocido: {tipo_widget}")

    def colocarwidgets(self, master, **kwargs):
        for index, (key, value) in enumerate(self.nombre_campos.items()):
            self.etiqueta = FabricaWidgets.crear_widget(
                "etiqueta",
                self.contenedor,
                text=value,
                **self.campos_etiquetas,
            )
            self.etiqueta.grid(row=index, column=0, padx=1, pady=1)


if __name__ == "__main__":
    pass