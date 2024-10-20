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


if __name__ == "__main__":
    pass
