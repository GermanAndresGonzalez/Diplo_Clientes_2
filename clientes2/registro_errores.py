"""Clase para registrar los errores de la aplicación

    Raises:
        RegistroLogError: error
      
    La clase registra errores durante la ejecución.
    Esto se hace visible cuando se hace clic en "Teléfono" en el treeview.
    Se genera un error que se registra en 'registro_errores.txt'.
    El archivo 'programa_errores.txt' es el archivo de log de la aplicación.   
"""

import os
import datetime


class RegistroLogError(Exception):
    """Registro de errores."""

    BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
    ruta = os.path.join(BASE_DIR, "registro_errores.txt")
    # print(ruta)

    def __init__(self, linea, modulo, fecha, *args):
        self.linea = linea
        self.modulo = modulo
        self.fecha = fecha
        self.varios = args

    def registrar_error(self):
        """Guarda los datos en el archivo de log."""

        log = open(self.ruta, "a", encoding="utf8")
        print(
            "Se produjo un error:",
            self.modulo,
            self.linea,
            self.varios,
            self.fecha,
            file=log,
        )


def registrar():
    """Solo para testing."""
    raise RegistroLogError(7, "Validacion", datetime.datetime.now(), "Correo")


if __name__ == "__main__":

    try:
        registrar()
    except RegistroLogError as log:
        log.registrar_error()
