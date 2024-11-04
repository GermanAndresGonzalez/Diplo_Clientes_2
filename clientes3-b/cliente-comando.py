"""
Cliente que se conecta al servidor y realiza una búsqueda.
Necesita un argumento por línea de comandos.
El servidor realiza una busqueda en el archivo de registros de la aplicación.
A la vez, el servidor registra la consulta realizada en un archivo separado.

"""

import socket
import sys


def cliente():
    encabezado = "Busqueda_cliente"
    ingreso = encabezado + " " + sys.argv[1]

    print(ingreso)
    HOST, PORT = "localhost", 9999
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # mensaje = "Login incorrecto"
    client_socket.send(ingreso.encode("utf-8"))

    respuesta = client_socket.recv(1024).decode("utf-8")
    print(f"Respuesta del servidor: {respuesta}")

    client_socket.close()


if __name__ == "__main__":
    cliente()
