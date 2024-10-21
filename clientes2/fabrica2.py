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


class CreadorMultiple:
    @staticmethod
    def crear_multiples_widgets(
        tipo_widget,
        master,
        inicio_x,
        inicio_y,
        textos,
        vertical=True,
        **kwargs,
    ):

        widgets = []
        for i, (key, texto) in enumerate(textos.items()):
            row = inicio_x + i if vertical else inicio_x
            col = inicio_y if vertical else inicio_y + i

            widget = FabricaWidgets.crear_widget(
                tipo_widget,
                master,
                text=texto,
                **kwargs,
            )
            widget.grid(row=row, column=col, padx=1, pady=1)
            widgets.append(widget)
        return widgets


class CreadorEntradasMultiples:
    @staticmethod
    def crear_multiples_widgets(
        tipo_widget, master, start_x, start_y, nombres, vertical=True, **kwargs
    ):
        widgets = {}
        for i, (nombre, texto) in enumerate(nombres.items()):
            row = start_x + i if vertical else start_x
            col = start_y if vertical else start_y + i

            widget = FabricaWidgets.crear_widget(tipo_widget, master, **kwargs)
            widget.grid(row=row, column=col, padx=5, pady=5)
            widgets[nombre] = widget

        return widgets


if __name__ == "__main__":
    pass