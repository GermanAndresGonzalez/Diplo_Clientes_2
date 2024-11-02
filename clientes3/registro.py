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


# import sys
# import binascii
class ClienteServidor:

    def __init__(self):
        self.mensaje = ""

    def enviar_datos(
        self, linea=None, modulo=None, fecha=None, usuario=None, *args, **kwargs
    ):
        self.mensaje = f"Linea: {linea},Módulo: {modulo},Fecha: {fecha},Usuario: {usuario},{args},{kwargs}"
        HOST, PORT = "localhost", 8080
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))

        # mensaje = "Login incorrecto"
        client_socket.send(self.mensaje.encode("utf-8"))

        respuesta = client_socket.recv(1024).decode("utf-8")
        print(f"Respuesta del servidor: {respuesta}")
        client_socket.close()


class RegistroLogError(Exception):
    """Registro de errores."""

    BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
    ruta = BASE_DIR + ("/datos/") + ("registro_app.log")
    cliente = ClienteServidor()

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
        # self, linea, modulo, fecha, usuario=None, *args
        self.cliente.enviar_datos(
            self,
            self.linea,
            self.modulo,
            self.fecha,
            self.usuario if self.usuario else "",
        )  # self.cliente(mensaje)


"""def registrar_fuera():
    Solo para testing.
    raise RegistroLogError(7, "Validacion", datetime.datetime.now(), "Correo")
"""

if __name__ == "__main__":
    pass
    """try:
        registrar_fuera()
    except RegistroLogError as log:
        log.registrar()"""
