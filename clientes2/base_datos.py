"""Clase con funciones de CRUD con las base de datos.
Y otras funciones de conexión."""

import sqlite3
from tkinter.messagebox import showinfo
import datetime

from registro_errores import RegistroLogError


class ManejoBD:
    """Funciones para el manejo de la bases de datos de Clientes."""

    def __init__(self, nombre_bd=None):
        self.nombre_bd = nombre_bd
        self.conexion = None
        self.cursor = None

    def tiene_datos(self, nombre_tabla):
        """Busca si la tabla tiene datos."""
        if self.conexion:
            try:
                self.cursor.execute(f"SELECT COUNT(*) FROM {nombre_tabla}")
                count = self.cursor.fetchone()[0]
                return count > 0
            except sqlite3.Error as e:
                print(f"Error al buscar datos en la base de datos: {e}")
                self.reg_errores = RegistroLogError(
                    25, "ManejoBD", datetime.datetime.now(), e
                )
                self.reg_errores.registrar_error()
        else:
            RES = showinfo("No hay una base de datos conectada.")
        return False

    def crear_db(self, nombre_bd):
        """Crea una base de datos nueva."""
        try:

            self.nombre_bd = nombre_bd
            self.conexion = sqlite3.connect(self.nombre_bd)
            self.cursor = self.conexion.cursor()
            print(f"La base de datos '{nombre_bd}' se creo correctamente.")
        except sqlite3.Error as e:
            self.reg_errores = RegistroLogError(
                41, "ManejoBD", datetime.datetime.now(), e
            )
            self.reg_errores.registrar_error()

    def crear_tabla(self, nombre_tabla, esquema):
        """Crea una tabla."""
        if self.conexion:
            try:
                self.cursor.execute(
                    f"CREATE TABLE IF NOT EXISTS {nombre_tabla} ({esquema})"
                )

                self.conexion.commit()
                print(f"La tabla '{nombre_tabla}' se creó correctamente.")
            except sqlite3.Error as e:
                RES = showinfo(f"Error al crear la tabla: {e}")
                self.reg_errores = RegistroLogError(
                    51, "ManejoBD", datetime.datetime.now(), e
                )
                self.reg_errores.registrar_error()

        else:
            RES = showinfo("No se creo la base de datos.")

    def conectar_bd(self, nombre_bd):
        """Conecta a una base de datos."""
        try:
            self.conexion = sqlite3.connect(nombre_bd)
            self.cursor = self.conexion.cursor()
            print(f"Conexión exitosa a la base de datos '{nombre_bd}'.")
        except sqlite3.Error as e:
            RES = showinfo(f"Error de conexión con la base de datos: {e}")
            self.reg_errores = RegistroLogError(
                64, "ManejoBD", datetime.datetime.now(), e
            )
            self.reg_errores.registrar_error()

    def cerrar_db(self):
        """Cierra la conexión con la base de datos."""
        if self.conexion:
            self.conexion.close()
            print(f"Se cerró la base de datos '{self.nombre_bd}'.")
        else:
            RES = showinfo("No hay una base de datos conectada.")

    def existe_cliente(self, nombre_cliente, apellido_cliente):
        """Busca si existe un cliente."""
        if self.conexion:
            try:
                self.cursor.execute(
                    "SELECT 1 FROM personas WHERE nombre_cliente = ? AND apellido_cliente = ?",
                    (nombre_cliente, apellido_cliente),
                )
                return self.cursor.fetchone() is not None
            except sqlite3.Error as e:
                print(f"Error al buscar datos en la base de datos: {e}")
                self.reg_errores = RegistroLogError(
                    56, "ManejoBD", datetime.datetime.now(), e
                )
                self.reg_errores.registrar_error()
        else:
            RES = showinfo("No hay una base de datos conectada.")
            self.reg_errores = RegistroLogError(
                56, "ManejoBD", datetime.datetime.now(), e
            )
            self.reg_errores.registrar_error()

    def cargar_datos(self, solicitud):
        """Busca los datos de la base para usarlos."""
        if self.conexion:
            try:
                self.cursor.execute(solicitud)
                return self.cursor.fetchall()
            except sqlite3.Error as e:
                RES = showinfo(f"Error al buscar los datos: {e}")
                self.reg_errores = RegistroLogError(
                    82, "ManejoBD", datetime.datetime.now(), e
                )
                self.reg_errores.registrar_error()
        else:
            RES = showinfo("No hay conexión con la base de datos.")
        return []

    def agregar_datos(self, nombre_tabla, datos):
        """Agrega datos en la tabla."""
        print(datos, type(datos))
        if self.existe_cliente(datos["nombre_cliente"], datos["apellido_cliente"]):
            RES = showinfo(
                "Error",
                f"El cliente {datos['nombre_cliente']} {datos['apellido_cliente']} ya existe",
            )
        else:
            if self.conexion:
                try:
                    columnas = ", ".join(datos.keys())
                    lugares = ", ".join("?" for _ in datos)
                    sql = f"INSERT INTO {nombre_tabla} ({columnas}) VALUES ({lugares})"
                    self.cursor.execute(sql, tuple(datos.values()))
                    self.conexion.commit()
                    print(f"Datos agregada a la tabla '{nombre_tabla}' correctamente.")
                except sqlite3.Error as e:
                    print(f"Error al agregar datos: {e}")
                    self.reg_errores = RegistroLogError(
                        117, "ManejoBD", datetime.datetime.now(), e
                    )
                    self.reg_errores.registrar_error()
            else:
                print("No hay conexión con la base de datos.")

    def borrar_datos(self, nombre_tabla, condicion):
        """Borra datos desde la tabla especificada."""
        if self.conexion:
            try:
                sql = f"DELETE FROM {nombre_tabla} WHERE id = ?"
                self.cursor.execute(sql, (condicion,))
                self.conexion.commit()
                print("¡Atención!", "Se borró la infomación de la manera correcta.")
            except sqlite3.Error as e:
                RES = showinfo("Error", f"Error en el borrado de datos: {e}")
                self.reg_errores = RegistroLogError(
                    134, "ManejoBD", datetime.datetime.now(), e
                )
                self.reg_errores.registrar_error()
        else:
            print("No hay una base conectada.")

    def actualizar_datos(self, nombre_tabla, datos, condicion):
        """Actualiza datos en la tabla."""
        if self.conexion:
            try:
                actualizado = ", ".join(f"{col} = ?" for col in datos.keys())
                sql = f"UPDATE {nombre_tabla} SET {actualizado} WHERE {condicion}"
                self.cursor.execute(sql, tuple(datos.values()))
                self.conexion.commit()
                print(
                    f"Los datos de la tabla '{nombre_tabla}' se actualizaron correctamente."
                )
            except sqlite3.Error as e:
                print(f"Error en la actualización de datos: {e}")
                self.reg_errores = RegistroLogError(
                    138, "ManejoBD", datetime.datetime.now(), e
                )
                self.reg_errores.registrar_error()

        else:
            print("No hay base conectadada.")
