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

    def __init__(
        self, linea, modulo, fecha, usuario=None, mensaje=None, *args, **kwargs
    ):
        self.mensaje = ""
        self.linea = str(linea)
        self.modulo = str(modulo)
        self.fecha = str(fecha)
        self.varios = args if args else None
        self.usuario = usuario if usuario else None
        self.mensaje = mensaje if mensaje else None

    def enviar_datos(
        self,
    ):
        try:

            self.mensaje = f"Linea: {self.linea}, Módulo: {self.modulo}, Fecha: {self.fecha}, Usuario: {self.usuario} {self.mensaje if self.mensaje else None} ,"
            HOST, PORT = "localhost", 8080
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((HOST, PORT))

            # mensaje = "Login incorrecto"
            client_socket.send(self.mensaje.encode("utf-8"))

            respuesta = client_socket.recv(1024).decode("utf-8")
            print(f"Respuesta del servidor: {respuesta}")
            client_socket.close()

        except Exception as e:
            print(f"Error al conectar con el servidor: {e}")


class RegistroLogError(Exception):
    """Registro de errores."""

    BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
    ruta = BASE_DIR + ("/datos/") + ("registro_app.log")

    def __init__(
        self,
        linea,
        modulo,
        fecha,
        usuario=None,
        mensaje=None,
        *args,
        **kwargs,
    ):
        self.linea = str(linea)
        self.modulo = modulo
        self.fecha = fecha
        self.varios = args if args else None
        self.usuario = usuario if usuario else None
        self.varios = " ".join(map(str, args)) if args else None
        self.usuario = usuario if usuario else None
        self.mensaje = mensaje if mensaje else None
        # --
        print(self.usuario)
        # --

    def registrar(self):
        """Guarda los datos en el archivo de log."""
        datos = [
            self.fecha,
            self.linea,
            self.modulo,
            self.varios,
            self.usuario,
        ]  #

        log = open(self.ruta, "a", encoding="utf8")
        print(
            f"Acción registrada: Línea: {self.linea}, Módulo: {self.modulo}, Fecha: {self.fecha}, Usuario: {self.usuario} {self.mensaje if self.mensaje else None} ,",
            file=log,
        )
        # f"Linea: {self.linea},Módulo: {self.modulo},Fecha: {self.fecha},Usuario: {self.usuario} {self.mensaje if self.mensaje else None} ,"
        self.cliente = ClienteServidor(
            self.linea,
            self.modulo,
            self.fecha,
            self.usuario,
            self.mensaje if self.mensaje else None,
        )
        # self, linea, modulo, fecha, usuario=None, *args
        self.cliente.enviar_datos()  # self.cliente(mensaje)


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
