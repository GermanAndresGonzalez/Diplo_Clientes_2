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
import socket
import sys
import binascii


class RegistroLogError(Exception):
    """Registro de errores."""

    BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
    ruta = BASE_DIR + ("/datos/") + ("registro.txt")
    HOST, PORT = "localhost", 9999
    data = " ".join(sys.argv[1:])
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # print(ruta)

    def __init__(self, linea, modulo, fecha, usuario=None, *args):
        self.linea = str(linea)
        self.modulo = modulo
        self.fecha = fecha
        self.varios = args if args else None
        self.usuario = usuario if usuario else None
        self.varios = " ".join(map(str, args)) if args else None
        self.usuario = usuario if usuario else None

    def registrar(self):
        """Guarda los datos en el archivo de log."""
        datos = [
            self.fecha,
            self.linea,
            self.modulo,
            self.varios,
            self.usuario if self.usuario else "",
        ]  #
        mensaje = (str(" ".join(map(str, datos))).encode("utf-8")).strip()
        print(mensaje)
        self.sock.sendto((mensaje), (self.HOST, self.PORT))
        recibido = self.sock.recv(1024)
        recibido = recibido.strip()
        recibido = recibido.decode("utf-8")
        # .decode("utf-8")
        print(recibido)

        log = open(self.ruta, "a", encoding="utf8")
        print(
            "Acción registrada:",
            self.fecha,
            self.usuario if self.usuario else "",
            self.modulo,
            self.linea,
            self.varios,
            file=log,
        )


def registrar_fuera():
    """Solo para testing."""
    raise RegistroLogError(7, "Validacion", datetime.datetime.now(), "Correo")


if __name__ == "__main__":

    try:
        registrar_fuera()
    except RegistroLogError as log:
        log.registrar()
