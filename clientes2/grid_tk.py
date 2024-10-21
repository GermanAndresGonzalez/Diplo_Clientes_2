import tkinter as tk
from tkinter import ttk, LabelFrame, Label, Entry, Button
from librerias.creador_ini import leer_config


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
        acciones=None,
        **kwargs,
    ):
        widgets = []
        for i, (key, texto) in enumerate(textos.items()):
            row = inicio_x + i if vertical else inicio_x
            col = inicio_y if vertical else inicio_y + i

            # Extraer el comando del diccionario de acciones, si existe
            if acciones and key in acciones:
                kwargs["command"] = acciones[key]

            widget = FabricaWidgets.crear_widget(
                tipo_widget, master, text=texto, **kwargs
            )
            widget.grid(row=row, column=col, padx=1, pady=1)
            widgets.append(widget)

        return widgets


root = tk.Tk()
root.title("Factory Pattern with Multiple Widgets Example")

# Diccionario con los textos para los widgets
textos_widgets = {
    "boton1": "Click me 1",
    "boton2": "Click me 2",
    "boton3": "Click me 3",
}

# Diccionario con las acciones para los botones
acciones_widgets = {
    "boton1": lambda: print("Botón 1 presionado"),
    "boton2": lambda: print("Botón 2 presionado"),
    "boton3": lambda: print("Botón 3 presionado"),
}

# Crear múltiples botones comenzando en la posición (1, 1)
botones = CreadorMultiple.crear_multiples_widgets(
    "boton", root, 1, 1, textos_widgets, acciones=acciones_widgets
)

root.mainloop()
