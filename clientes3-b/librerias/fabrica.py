import tkinter as tk
from tkinter import ttk, LabelFrame, Label, Entry, Button
from librerias.creador_ini import leer_config


class FabricaWidgets:
    @staticmethod
    def crear_widget(tipo_widget, master, ancho=None, alto=None, **kwargs):
        if ancho in kwargs:
            kwargs["width"] = ancho
        if alto in kwargs:
            kwargs["height"] = alto

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
        ancho=None,
        **kwargs,
    ):
        widgets = []
        for i, (key, texto) in enumerate(textos.items()):
            row = inicio_x + i if vertical else inicio_x
            col = inicio_y if vertical else inicio_y + i

            # Extraer el comando del diccionario de acciones, si existe
            if acciones and key in acciones:
                kwargs["command"] = acciones[key]
            if ancho:
                kwargs["width"] = ancho
            widget = FabricaWidgets.crear_widget(
                tipo_widget, master, text=texto, **kwargs
            )
            widget.grid(row=row, column=col, padx=1, pady=1)
            widgets.append(widget)

        return widgets


class CreadorEntradasMultiples:
    @staticmethod
    def crear_multiples_widgets(
        tipo_widget,
        master,
        inicio_x,
        inicio_y,
        nombres,
        estado,
        textvariables=None,
        vertical=True,
        **kwargs,
    ):
        widgets = {}
        for i, (nombre, texto) in enumerate(nombres.items()):
            row = inicio_x + i if vertical else inicio_x
            col = inicio_y if vertical else inicio_y + i

            widget_kwargs = kwargs.copy()
            widget_kwargs["state"] = estado[i]
            if textvariables:
                widget_kwargs["textvariable"] = textvariables[i]

            widget = FabricaWidgets.crear_widget(tipo_widget, master, **widget_kwargs)
            widget.grid(row=row, column=col, padx=5, pady=5)
            widgets[nombre] = widget
        return widgets


def hola():
    print("hola")


if __name__ == "__main__":
    nombre_campos = leer_config("nombre_campos_entradas")
    campos_etiquetas = leer_config("campos_etiquetas")
    estado = ["disabled", "normal", "normal"]
    texto_botones = leer_config("texto_botones")
    botones = leer_config("botones")
    campos_entradas = leer_config("campos_entradas")

    root = tk.Tk()
    root.title("Factory Pattern with Named Widgets Example")

    # Diccionario con los nombres y valores para las entradas
    nombres_entradas = {
        "entrada1": "Valor 1",
        "entrada2": "Valor 2",
        "entrada3": "Valor 3",
    }
    comandos = {
        "agregar": lambda: root.destroy(),
        "vaciar": lambda: hola(),
        "borrar": lambda: hola(),
        "modificar": lambda: hola(),
        "importar": lambda: hola(),
        "salir": lambda: root.destroy(),
    }
    estados = {
        "entrada1": "disabled",
        "entrada2": "normal",
        "entrada3": "normal",
    }

    for i, (nombre, texto) in enumerate(comandos.items()):
        print(nombre, texto)
    # print(acciones[0][])
    # Crear múltiples entradas comenzando en la posición (1, 1)

    # Acceder a una entrada específica por su nombre
    # entradas["entrada1"].insert(0, "Nuevo Valor 1")
    botones = CreadorMultiple.crear_multiples_widgets(
        "boton",
        root,
        2,
        1,
        textos=texto_botones,
        vertical=True,
        acciones=comandos,
        **botones,
    )

    entradas = CreadorEntradasMultiples.crear_multiples_widgets(
        "entrada", root, 1, 1, nombres_entradas, estado, False, **campos_entradas
    )
    etiquetas = CreadorMultiple.crear_multiples_widgets(
        "etiqueta",
        root,
        2,
        2,
        nombres_entradas,
        True,
        **campos_etiquetas,
    )

    entradas["entrada2"].insert(0, "Nuevo Valor 1")

    root.mainloop()
