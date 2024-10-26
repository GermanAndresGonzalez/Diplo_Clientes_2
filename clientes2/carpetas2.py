# Python program to illustrate the usage of
# treeview scrollbars using tkinter


import tkinter as tk
from tkinter import (
    ttk,
    LabelFrame,
    Label,
    IntVar,
    StringVar,
    Entry,
    Button,
    Scrollbar,
    Menu,
)
import datetime
import webbrowser
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image
from os import getcwd
import sqlite3
from librerias.creador_ini import leer_config
from modelo import Abmc
from functools import partial
from librerias.acercade import Acercade
from registro import RegistroLogError

# from vista import Ventana
# from observador import Observer

from fabrica3 import FabricaWidgets, CreadorMultiple, CreadorEntradasMultiples


def hola():
    print("hola")


def seleccionar():
    print("hola")


# Creating tkinter window
window = tk.Tk()
window.resizable(width=1, height=1)
window.geometry("1500x750")
imagenes = leer_config("imagenes")
marco = leer_config("marco")
txt_app = leer_config("aplicacion")
campos_etiquetas = leer_config("campos_etiquetas")
nombre_campos = leer_config("nombre_campos_entradas")
campos_entradas = leer_config("campos_entradas")
botones = leer_config("botones")
txt_login = leer_config("texto_login")
texto_botones = leer_config("texto_botones")
titulo = leer_config("titulo")
nombres_arbol = leer_config("col_treeview")
datos_arbol = leer_config("val_treeview")
col_cals = leer_config("val_col_treeview")
comandos = {
    "agregar": lambda: window.destroy(),
    "vaciar": lambda: hola(),
    "borrar": lambda: hola(),
    "modificar": lambda: hola(),
    "importar": lambda: hola(),
    "salir": lambda: window.destroy(),
}
estados = {
    0: "readonly",
    1: "normal",
    2: "normal",
    3: "normal",
    4: "normal",
    5: "normal",
    6: "normal",
    7: "normal",
}
icono = Image.open(imagenes["favicon_icon"])
foto = ImageTk.PhotoImage(icono)
window.wm_iconphoto(False, foto)
var_indice = IntVar()
var_nombre_cliente = StringVar()
var_apellido_cliente = StringVar()
var_contacto = StringVar()
var_telefono = StringVar()
var_sitio = StringVar()
var_perfil = StringVar()
var_correo_electronico = StringVar()


# Using treeview widget
marco_arbol = FabricaWidgets.crear_widget(
    "marco",
    window,
    borderwidth=1,
    relief="solid",
    highlightbackground="#78A083",
    highlightthickness=2,
    **marco,
)

estilo_arbol = ttk.Style()
estilo_arbol.theme_use("default")
estilo_arbol.configure(
    "Treeview",
    font=datos_arbol["fuente"],
    background=datos_arbol["background"],
    foreground=datos_arbol["foreground"],
    fieldbackground=datos_arbol["fieldbackground"],
)
estilo_arbol.configure(
    "Treeview.Heading",
    font=(datos_arbol["fuente_heading"]),
    background=datos_arbol["background_heading"],
    foreground=datos_arbol["foreground_heading"],
)
estilo_arbol.map(
    "Treeview",
    background=[("selected", datos_arbol["b_selected"])],
    foreground=[("selected", datos_arbol["f_selected"])],
)
cols = list(col_cals.values())
columnas = []
for index, (key, value) in enumerate(nombres_arbol.items()):
    columnas.append((value, cols[index], "w"))
arbol_vista = FabricaWidgets.crear_widget(
    "arbol",
    marco_arbol,
    columns=[col[0] for col in columnas],
    show="headings",
    style="Treeview",
    selectmode="browse",
)
for col, width, anchor in columnas:
    arbol_vista.column(
        col, width=width, minwidth=width, anchor=anchor if anchor else "w"
    )
    arbol_vista.heading(col, text=col)

barra_desplazamiento = Scrollbar(
    marco_arbol, orient="vertical", command=arbol_vista.yview
)
barra_desplazamiento.pack(side="right", fill="y")
arbol_vista.configure(yscrollcommand=barra_desplazamiento.set)
arbol_vista.bind("<ButtonRelease-1>", seleccionar)
arbol_vista.bind("<KeyRelease-Up>", seleccionar)
arbol_vista.bind("<KeyRelease-Down>", seleccionar)
marco_arbol.place(
    relx=0.5,
    rely=0.26,
    anchor="center",
)
arbol_vista.pack()  #

# Calling mainloop
window.mainloop()
