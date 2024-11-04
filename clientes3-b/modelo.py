"""Modelo CRUD de la base de datos."""

import sqlite3

import shelve
import datetime
from tkinter.messagebox import showinfo, askquestion
from validacion import ValidacionCampos
from base_datos import ManejoBD
from librerias.diccionario import diccionario
from registro import RegistroLogError
from observador import Sujeto
from registro import ClienteServidor

# ------- UDP ------
import socket
import sys
import binascii


def registro(funcion):
    def envoltura(*args, **kwargs):
        funcion(*args, **kwargs)

        print("Se ejecutó:", funcion.__name__, *args, **kwargs)

    return envoltura


class Abmc(Sujeto):
    """Crea Altas, Bajas, Modificaciones de datos."""

    def __init__(self, ventana, usuario=None):
        self.usuario = usuario if usuario else None
        self.ventana = ventana
        self.esquema = "id integer PRIMARY KEY AUTOINCREMENT, nombre_cliente text NOT NULL, apellido_cliente text NOT NULL, contacto text NOT NULL, correo_electronico text NOT NULL, telefono text NOT NULL, sitio_web text NOT NULL, otro_perfil text NOT NULL"
        self.nombre_bd = "datos/clientes_nuevo.db"
        self.nombre_tabla = "personas"
        # self.cliente = ClienteServidor()
        self.validar = ValidacionCampos()
        self.base_datos = ManejoBD()
        self.base_datos.crear_db(self.nombre_bd)
        self.base_datos.crear_tabla(self.nombre_tabla, self.esquema)
        # print(self.nombre_bd)
        # print(self.esquema)
        # --
        print(self.usuario)
        # --
        if not self.base_datos.tiene_datos(self.nombre_tabla):
            self.base_datos.conectar_bd(self.nombre_bd)
            self.agregar_cliente_diccionario(diccionario)

    @registro
    def importar_datos(self, tree):
        """Usado para importar datos desde un archivo shelve."""

        diccionario2 = ""
        try:
            db = shelve.open("referencia\\diccionario_nombre_apellido_cl3")
            diccionario2 = db["diccionario"]
            db.close()
        except Exception as e:
            res = showinfo("Error", f"No se pudo abrir el archivo shelve {e}")
            self.reg_errores = RegistroLogError(
                42, "Modelo", datetime.datetime.now(), self.usuario
            )
            # self.reg_errores.clientes(42, "Modelo", datetime.datetime.now(), self.usuario)
            # self.reg_errores.registrar()

        try:
            self.base_datos.conectar_bd(self.nombre_bd)
            for i, datos in enumerate(diccionario2.values()):
                # valores = datos
                # for i in range(len(diccionario2)):
                #    datos = diccionario2[i]
                self.base_datos.agregar_datos("personas", datos)
            self.base_datos.cerrar_db()
            self.cargar_treeview(
                tree, nombre_bd=self.nombre_bd, nombre_tabla=self.nombre_tabla
            )
        except sqlite3.Error as e:
            res = showinfo("Error", "No se pudo modificar el cliente: " + str(e))
            self.reg_errores = RegistroLogError(
                55, "Modelo", datetime.datetime.now(), self.usuario
            )
            self.reg_errores.registrar()

    def agregar_cliente_diccionario(self, diccionario):
        """Usado para agregar datos a la base de datos cuando está vacía."""
        for i, datos in enumerate(diccionario.values()):
            self.base_datos.agregar_datos("personas", datos)

    @registro
    def alta_cliente(
        self,
        tree,
        var_indice,
        var_nombre_cliente,
        var_apellido_cliente,
        var_contacto,
        var_correo_electronico,
        var_telefono,
        var_sitio,
        var_perfil,
    ):
        """Alta de clientes en la base de datos."""
        print(
            var_indice,
            var_nombre_cliente,
            var_apellido_cliente,
            var_contacto,
            var_correo_electronico,
            var_telefono,
            var_sitio,
            var_perfil,
        )
        accion = "agregaron"

        valor = self.validar.validar(
            accion,
            var_indice,
            var_nombre_cliente,
            var_apellido_cliente,
            var_contacto,
            var_correo_electronico,
            var_telefono,
            var_sitio,
            var_perfil,
            tree,
        )

        if valor is True:
            res = askquestion("¡Atención!", "¿Desea agregar el cliente?")
            if res == "yes":
                try:
                    datos = {
                        "nombre_cliente": var_nombre_cliente,
                        "apellido_cliente": var_apellido_cliente,
                        "contacto": var_contacto,
                        "correo_electronico": var_correo_electronico,
                        "telefono": var_telefono,
                        "sitio_web": var_sitio,
                        "otro_perfil": var_perfil,
                    }
                    self.base_datos.conectar_bd(self.nombre_bd)
                    self.base_datos.agregar_datos("personas", datos)
                    self.base_datos.cerrar_db()
                    self.notificar("Alta:", datos)
                    self.cargar_treeview(
                        tree, nombre_bd=self.nombre_bd, nombre_tabla=self.nombre_tabla
                    )
                    self.reg_errores = RegistroLogError(
                        142, "Alta", datetime.datetime.now(), self.usuario
                    )
                    self.reg_errores.registrar()
                    self.vaciar_todo(tree)
                except sqlite3.Error as e:
                    res = showinfo(
                        "Error", "No se pudo modificar el cliente: " + str(e)
                    )
                    self.reg_errores = RegistroLogError(
                        113, "Modelo", datetime.datetime.now(), self.usuario
                    )
                    # self.cliente.enviar_datos(113, "Modelo", datetime.datetime.now(), self.usuario)
                    self.reg_errores.registrar()

            else:
                res = showinfo("¡Atención!", "No se agregó el cliente")

    @registro
    def borrar(self, tree):
        """Borra cliente de la base de datos."""

        item = tree.focus()
        val_seleccionados = tree.selection()
        res = askquestion(
            "¡Atención!", "¿Desea borrar el cliente o los clientes seleccionados?"
        )
        # valores = tree.item(item, "values")

        if res == "yes":
            try:
                self.base_datos.conectar_bd(self.nombre_bd)
                for item in val_seleccionados:
                    valor2 = tree.item(item, "values")
                    self.base_datos.borrar_datos(self.nombre_tabla, (str(valor2[0])))
                    self.notificar("Baja:", valor2)
                self.base_datos.cerrar_db()
                self.cargar_treeview(
                    tree,
                    nombre_bd=self.nombre_bd,
                    nombre_tabla=self.nombre_tabla,
                )
                self.reg_errores = RegistroLogError(
                    184, "Baja", datetime.datetime.now(), self.usuario
                )
                self.reg_errores.registrar()
            except Exception:
                self.reg_errores = RegistroLogError(
                    139,
                    "Modelo",
                    datetime.datetime.now(),
                    self.usuario,
                )
                self.reg_errores.registrar()
        else:
            res = showinfo("¡Atención!", "No se borró el cliente")

        self.vaciar_todo(tree)

    @registro
    def actualizar(
        self,
        tree,
        var_indice,
        var_nombre_cliente,
        var_apellido_cliente,
        var_contacto,
        var_correo_electronico,
        var_telefono,
        var_sitio,
        var_perfil,
    ):
        """Modifica los datos de un cliente específico."""

        item = tree.focus()
        valor = tree.selection()
        accion = "modificaron"
        print(item, valor, accion)
        valor = self.validar.validar(
            accion,
            var_indice,
            var_nombre_cliente,
            var_apellido_cliente,
            var_contacto,
            var_correo_electronico,
            var_telefono,
            var_sitio,
            var_perfil,
            tree,
        )

        if valor is True:
            res = askquestion("¡Atención!", "¿Desea modificar el cliente?")
            if res == "yes":
                try:
                    datos = {
                        "nombre_cliente": var_nombre_cliente,
                        "apellido_cliente": var_apellido_cliente,
                        "contacto": var_contacto,
                        "correo_electronico": var_correo_electronico,
                        "telefono": var_telefono,
                        "sitio_web": var_sitio,
                        "otro_perfil": var_perfil,
                    }
                    self.base_datos.conectar_bd(self.nombre_bd)
                    self.base_datos.actualizar_datos(
                        "personas", datos, f"id = {var_indice}"
                    )
                    self.base_datos.cerrar_db()
                    self.notificar("Modificación:", datos)
                    self.cargar_treeview(
                        tree, nombre_bd=self.nombre_bd, nombre_tabla=self.nombre_tabla
                    )
                    self.vaciar_todo(tree)
                    self.reg_errores = RegistroLogError(
                        252, "Modificación", datetime.datetime.now()
                    )
                    self.reg_errores.registrar()

                except sqlite3.Error as e:
                    res = showinfo(
                        "Error", "No se pudo modificar el cliente: " + str(e)
                    )
                    self.reg_errores = RegistroLogError(
                        201, "Modelo", datetime.datetime.now(), self.usuario
                    )
                    self.reg_errores.registrar()

            else:
                res = showinfo(
                    "¡Atención!", "No se realizó la modificación del cliente."
                )

    def cargar_treeview(self, tree, nombre_bd, nombre_tabla):
        """Llena el Treeview con los datos de la base de datos."""
        # nombre_tabla = "personas"

        self.base_datos.conectar_bd(nombre_bd)
        tree.delete(*tree.get_children())
        for row in self.base_datos.cargar_datos(f"SELECT * FROM {nombre_tabla}"):
            tree.insert("", "end", values=row)
        self.base_datos.cerrar_db()
        # global indice

    def vaciar_todo(
        self,
        tree,
    ):
        """Vacía los datos de los widget de entrada."""

        self.ventana.vaciar()
        # self.entry.delete(0, "end")
        self.cargar_treeview(
            tree, nombre_bd=self.nombre_bd, nombre_tabla=self.nombre_tabla
        )
