import tkinter as tk
import configparser
from PIL import ImageTk, Image
import sqlite3


def leer_config(diccionario):
    dato = {}
    config = configparser.ConfigParser()
    config.read("../referencia/config.ini", encoding="utf-8")

    config.sections()
    for key in config[diccionario]:
        dato.update({key: config[diccionario][key]})  # config[diccionario][key]
    return dato


class WidgetFactory:
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
        else:
            raise ValueError(f"Tipo de widget desconocido: {tipo_widget}")


imagenes = leer_config("imagenes")
marco = leer_config("marco")
titulo = leer_config("titulo")
campos_etiquetas = leer_config("campos_etiquetas")
nombre_campos = leer_config("nombre_campos_entradas")
campos_entradas = leer_config("campos_entradas")
botones = leer_config("botones")
txt_login = leer_config("texto_login")
texto_botones = leer_config("texto_botones")

print("\n", marco, "\n",)

root = tk.Tk()
root.title("Pantalla de login")
root.geometry("700x350")
root.iconbitmap(imagenes["favicon_icon"])
root.resizable(0, 0)

marco_mayor = WidgetFactory.crear_widget("marco", root, width=700, height=350, **marco)
marco_izq = WidgetFactory.crear_widget(
    "marco", marco_mayor, width=300, height=345, borderwidth=1, **marco
)
pinky = ImageTk.PhotoImage(Image.open(imagenes["imag_pinky"]))
imagen_pinky = WidgetFactory.crear_widget(
    "etiqueta", marco_izq, image=pinky, anchor="center", **campos_etiquetas
)

imagen_pinky.place(x=50, y=10)

marco_izq.place(x=0, y=0)
marco_der = WidgetFactory.crear_widget(
    "marco", marco_mayor, width=395, height=345, **marco
)


eti_usuario = WidgetFactory.crear_widget(
    "etiqueta", marco_der, text=txt_login["usuario"], **campos_etiquetas
)
eti_usuario.place(x=40, y=10, anchor=tk.NW)


entrada_usuario = WidgetFactory.crear_widget("entrada", marco_der, **campos_entradas)
entrada_usuario.place(x=20, y=50)


eti_pass = WidgetFactory.crear_widget(
    "etiqueta", marco_der, text=txt_login["contraseña"], **campos_etiquetas
)
eti_pass.place(
    x=40,
    y=80,
    anchor=tk.NW,
)


entrada_pass = WidgetFactory.crear_widget(
    "entrada", marco_der, show="*", **campos_entradas
)
entrada_pass.place(x=20, y=120)


btn_salir = WidgetFactory.crear_widget(
    "boton",
    marco_der,
    text=txt_login["boton"],
    command=lambda: root.destroy(),
    width=15,
    **botones,
)
btn_salir.place(x=20, y=200)


btn_salir = WidgetFactory.crear_widget(
    "boton",
    marco_der,
    text=texto_botones["salir"],
    command=lambda: root.destroy(),
    width=15,
    **botones,
)
btn_salir.place(x=180, y=200)


marco_der.place(x=301, y=0)
marco_mayor.place(x=0, y=0)
root.mainloop()
