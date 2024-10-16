"""Módulo principal del programa."""

from tkinter import Tk
import vista
from observador import Observer


__author__ = "Germán González"
__maintainer__ = "Germán González"
__email__ = "gandresgonzalez@gmail.com"
__copyright__ = "Copyright 2024"
__version__ = "0.1"


class Controlador:
    """Controlador de la vista principal."""

    def __init__(self, _root):
        # self.controlador_root = root
        self.objeto_vista = vista.Ventana(_root)
        # self.observador_app = observador.ConcreteObserverA(self.objeto_vista.objeto_acciones)
        # self.observador = Observer.ConcreteObserverA(self.objeto_vista.objeto_acciones)


if __name__ == "__main__":

    MI_ID = 0
    root = Tk()
    aplicacion = Controlador(root)
    obser = Observer(aplicacion.objeto_vista.objeto_acciones)
    # observador = Observer(aplicacion.objeto_vista)

    root.mainloop()

    # aplicacion.objeto_vista.actualizar()
