"""
Servidor que busca cadenas de texto en un archivo de registros de una aplicación
Además registra las consultas realizadas en un archivo separado.

Si la solicitud tiene un encabezado, se realiza una búsqueda en el archivo de registros y se guarda la consulta.
De lo contrario, se guarda la info en el archivo de registros de la app.

"""

import socketserver

# Si tiene encabezado, significa que la solicitud proviene de un cliente.
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
        datos_rec = self.request.recv(1024).decode("utf-8")
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


# server = socketserver.TCPServer(("localhost", 8080), MiHandler)
# print("Servidor en espera de conexiones...")
# server.serve_forever()

if __name__ == "__main__":
    server = socketserver.TCPServer(("localhost", 8080), MiHandler)
    print("Servidor en espera de conexiones...")
    server.serve_forever()
