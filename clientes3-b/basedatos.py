"""
Clase con funciones de la tabla Usuarios para Usuarios y Contraseñas de inicio de sesión.
"""

import sqlite3

conn = sqlite3.connect("datos/clientes_nuevo.db")
cursor = conn.cursor()
cursor.execute(
    """CREATE TABLE IF NOT EXISTS usuarios (nombre_usuario TEXT PRIMARY KEY, contrasena TEXT NOT NULL, correo_electronico TEXT NOT NULL, nombre TEXT NOT NULL)"""
)

cursor.execute(
    """INSERT INTO usuarios (nombre_usuario, contrasena, correo_electronico, nombre) VALUES ('admin', 'admin', 'admin@yahoo.com', 'admin')"""
)
cursor.execute(
    """INSERT INTO usuarios (nombre_usuario, contrasena, correo_electronico, nombre) VALUES ('root', '1234', 'root@yahoo.com', 'root')"""
)
cursor.execute(
    """INSERT INTO usuarios (nombre_usuario, contrasena, correo_electronico, nombre) VALUES ('invitado', 'invitado', 'invitado@yahoo.com', 'invitado')"""
)


conn.commit()
conn.close()
