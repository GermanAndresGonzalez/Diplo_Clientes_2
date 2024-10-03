"""Modelo CRUD de la base de datos."""

import sqlite3

import shelve
import datetime
from tkinter.messagebox import showinfo, askquestion
from validacion import ValidacionCampos
from base_datos import ManejoBD
from referencia.diccionario import diccionario
from registro_errores import RegistroLogError


class Abmc:
    """Crea Altas, Bajas, Modificaciones de datos."""

    def __init__(self, ventana):
        self.ventana = ventana
        self.esquema = "id integer PRIMARY KEY AUTOINCREMENT, nombre_cliente text NOT NULL, apellido_cliente text NOT NULL, contacto text NOT NULL, correo_electronico text NOT NULL, telefono text NOT NULL, sitio_web text NOT NULL, otro_perfil text NOT NULL"
        self.nombre_bd = "clientes_nuevo.db"
        self.nombre_tabla = "personas"
        self.validar = ValidacionCampos()
        self.base_datos = ManejoBD()
        self.base_datos.crear_db(self.nombre_bd)
        self.base_datos.crear_tabla(self.nombre_tabla, self.esquema)
        # print(self.nombre_bd)
        # print(self.esquema)
        if not self.base_datos.tiene_datos(self.nombre_tabla):
            self.base_datos.conectar_bd(self.nombre_bd)
            self.agregar_cliente_diccionario(diccionario)

    def importar_datos(self, tree):
        """Usado para importar datos desde un archivo shelve."""

        diccionario2 = ""
        try:
            db = shelve.open("referencia\\diccionario_nombre_apellido_cl3")
            diccionario2 = db["diccionario"]
            db.close()
        except Exception as e:
            res = showinfo("Error", f"No se pudo abrir el archivo shelve {e}")
            self.reg_errores = RegistroLogError(42, "Modelo", datetime.datetime.now())
            self.reg_errores.registrar_error()

        try:
            self.base_datos.conectar_bd(self.nombre_bd)
            for i, datos in enumerate(diccionario2.values()):
                # valores = datos
                # for i in range(len(diccionario2)):
                #    datos = diccionario2[i]
                self.base_datos.agregar_datos("personas", datos)
            self.base_datos.cerrar_db()
            self.cargar_treeview(tree)
        except sqlite3.Error as e:
            res = showinfo("Error", "No se pudo modificar el cliente: " + str(e))
            self.reg_errores = RegistroLogError(55, "Modelo", datetime.datetime.now())
            self.reg_errores.registrar_error()

    def agregar_cliente_diccionario(self, diccionario):
        """Usado para agregar datos a la base de datos cuando está vacía."""
        for i, datos in enumerate(diccionario.values()):
            self.base_datos.agregar_datos("personas", datos)

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
                    self.cargar_treeview(tree)
                    self.vaciar_todo(tree)
                except sqlite3.Error as e:
                    res = showinfo(
                        "Error", "No se pudo modificar el cliente: " + str(e)
                    )
                    self.reg_errores = RegistroLogError(
                        113, "Modelo", datetime.datetime.now()
                    )
                    self.reg_errores.registrar_error()

            else:
                res = showinfo("¡Atención!", "No se agregó el cliente")

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
                    self.base_datos.cerrar_db()
                    self.cargar_treeview(tree)
            except Exception:
                self.reg_errores = RegistroLogError(
                    139, "Modelo", datetime.datetime.now()
                )
                self.reg_errores.registrar_error()

        else:
            res = showinfo("¡Atención!", "No se borró el cliente")

        self.vaciar_todo(tree)

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
        # print(valor)
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
                    self.cargar_treeview(tree)
                    self.vaciar_todo(tree)

                except sqlite3.Error as e:
                    res = showinfo(
                        "Error", "No se pudo modificar el cliente: " + str(e)
                    )
                    self.reg_errores = RegistroLogError(
                        201, "Modelo", datetime.datetime.now()
                    )
                    self.reg_errores.registrar_error()

            else:
                res = showinfo(
                    "¡Atención!", "No se realizó la modificación del cliente."
                )
            # cargar_treeview(tree)

    def cargar_treeview(self, tree):
        """Llena el Treeview con los datos de la base de datos."""

        # global indice
        self.base_datos.conectar_bd(self.nombre_bd)
        tree.delete(*tree.get_children())
        for row in self.base_datos.cargar_datos("SELECT * FROM personas"):
            tree.insert("", "end", values=row)
        self.base_datos.cerrar_db()

    def vaciar_todo(
        self,
        tree,
    ):
        """Vacía los datos de los widget de entrada."""

        self.ventana.vaciar()
        # self.entry.delete(0, "end")
        self.cargar_treeview(tree)
