"""
Servidor que busca cadenas de texto en un archivo de registros de una aplicación
Además registra las consultas realizadas en un archivo separado.

Si la solicitud tiene un encabezado, se realiza una búsqueda en el archivo de registros y se guarda la consulta.
De lo contrario, se guarda la info en el archivo de registros de la app.

"""

import socketserver
import threading
import time
import tkinter as tk
import pickle

encabezado = "Busqueda_cliente "
registro_app = "registro_app.log"
registro_servidor = "registro_servidor.log"


class MiHandler(socketserver.BaseRequestHandler):
    def buscar_cadena_registro(self, archivo, cadena):
        lineas = []
        with open(archivo, "r", encoding="utf-8") as file:
            for numero_linea, linea in enumerate(file, start=1):
                if cadena in linea:
                    # linea_ag = linea.strip()
                    lineas.append(linea)
        return lineas

    def registrar_consulta(self, datos_rec, registro_app=None):
        if not registro_app:
            registro = f"Consulta registrada: {datos_rec}, {self.client_address}"
            with open("registro_servidor.log", "a", encoding="utf-8") as file:
                file.write(f"{registro}\n")
        else:
            registro = f"Cliente: {datos_rec}, {self.client_address}"
            with open(registro_app, "a", encoding="utf-8") as file:
                file.write(f"{registro}\n")

    def buscar_encabezado(self, dato):
        if encabezado in dato:
            dato = dato.replace(encabezado, "")
            return dato

    def handle(self):
        print(f"Conexión establecida con {self.client_address}")
        datos_rec = self.request.recv(40960).decode("utf-8")
        print(f"Mensaje recibido: {datos_rec}")

        resultado_busqueda = self.buscar_encabezado(datos_rec)

        if resultado_busqueda:
            datos = self.buscar_cadena_registro("registro_app.log", resultado_busqueda)
            self.registrar_consulta(datos_rec)
            self.request.sendall("".join(datos).encode("utf-8"))
        else:
            self.registrar_consulta(datos_rec, registro_app)
            # datos = self.buscar_cadena_registro("registro_app.log", datos_rec)

        # self.request.sendall("".join(datos).encode("utf-8"))
        self.request.sendall("Mensaje recibido y guardado".encode("utf-8"))


class ServidorThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.server = socketserver.TCPServer(("localhost", 9999), MiHandler)
        # Permite reutilizar el socket
        self.server.allow_reuse_address = True
        self.running = False
        self.daemon = True  # Cerrar el hilo al cerrar la aplicación

    def run(self):
        self.running = True
        print("Servidor en espera de conexiones...")
        while self.running:
            # Procesa una sola solicitud y luego continúa
            self.server.handle_request()
            time.sleep(0.1)  # Evita que el bucle consuma demasiados recursos

    def detener(self):
        self.running = False
        self.server.server_close()
        print("Servidor detenido.")


# Funciones de control del servidor
def iniciar_servidor():
    global servidor_thread
    if servidor_thread is None or not servidor_thread.is_alive():
        # Crear e iniciar el hilo del servidor solo al presionar el botón
        servidor_thread = ServidorThread()
        servidor_thread.start()
        print("Servidor iniciado.")


def detener_servidor():
    global servidor_thread
    if servidor_thread and servidor_thread.is_alive():
        servidor_thread.detener()
        servidor_thread.join()  # Espera a que el hilo termine
        print("Servidor detenido.")


servidor_thread = None


def iniciar_interfaz():
    root = tk.Tk()
    root.title("Control del Servidor")
    root.geometry("300x200")

    btn_iniciar = tk.Button(root, text="Iniciar Servidor", command=iniciar_servidor)
    btn_iniciar.pack(pady=10)

    btn_detener = tk.Button(root, text="Detener Servidor", command=detener_servidor)
    btn_detener.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    iniciar_interfaz()
