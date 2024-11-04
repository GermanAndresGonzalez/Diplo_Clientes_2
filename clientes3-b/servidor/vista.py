"""
Vista de una aplicación que enciende y apaga el servidor. 
Solo tiene dos botones.
"""

from tkinter import Button


import os
import sys

# ===========================================================

from servidor_handler import MiHandler, ServidorThread

theproc = ""
encabezado = "Busqueda_cliente "
registro_app = "registro_app.log"
registro_servidor = "registro_servidor.log"


class Ventanita:
    """Ventanita de la aplicación"""

    def __init__(self, window):
        self.servidor_thread = None
        self.root = window
        self.root.title("Control del Servidor")
        self.root.geometry("300x200")

        self.btn_iniciar = Button(
            self.root, text="Iniciar Servidor", command=lambda: self.iniciar_servidor()
        )
        self.btn_iniciar.pack(pady=10)

        self.btn_detener = Button(
            self.root, text="Detener Servidor", command=lambda: self.detener_servidor()
        )
        self.btn_detener.pack(pady=10)

    def iniciar_servidor(self):
        """Iniciar el hilo del servidor"""
        # global servidor_thread
        if self.servidor_thread is None or not self.servidor_thread.is_alive():
            # Crear e iniciar el hilo del servidor solo al presionar el botón
            self.servidor_thread = ServidorThread()
            self.servidor_thread.start()
            print("Servidor iniciado.")

    def detener_servidor(self):
        """Detiene el hilo del servidor"""
        # global self.servidor_thread
        if self.servidor_thread and self.servidor_thread.is_alive():
            self.servidor_thread.detener()
            self.servidor_thread.join()  # Espera a que el hilo termine
            print("Servidor detenido.")
