"""Módulo principal del programa."""

from tkinter import Tk
import vista

__author__ = "Germán González"
__maintainer__ = "Germán González"
__email__ = "gandresgonzalez@gmail.com"
__copyright__ = "Copyright 2024"
__version__ = "0.1"


class Controlador:
    """Controlador de la vista principal."""

    def __init__(self, root):
        self.controlador_root = root
        self.objeto_vista = vista.Ventana(self.controlador_root)


if __name__ == "__main__":

    MI_ID = 0
    root = Tk()
    aplicacion = Controlador(root)
    root.mainloop()
