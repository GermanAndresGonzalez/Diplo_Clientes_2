"""Módulo para la validación de los valores de los campos."""

import re
from tkinter.messagebox import showinfo
from registro import RegistroLogError


class ValidacionCampos:
    """Valida los campos de widget de entrada."""

    def __init__(self) -> None:
        # self.reg_errores = RegistroLogError()
        self.criterio_correo = (
            "Formato de correo electrónico: xxx@xxxxx.xxx, xxx@xxxxx.xxx.xx"
        )
        self.criterio_campos = (
            "No se permiten campos vacíos o con espacios al inicio o al final"
        )
        self.criterio_sitio = "Sitio web/perfil sin 'http://' o 'https://'"
        self.criterio_perfil = "Otro perfil puede ser 'No' o una dirección web"
        self.criterio_telefono = (
            "El número de teléfono debe tener formato +xxxxxxxxxx (8-16 dígitos)"
        )

    def validar_nombres(self, campo_nombre):
        """Valida los nombres y contactos."""
        patron_nombre = r"^[A-Za-zñáéíóúÑÁÉÍÓÚ]+(?:[ _-][A-Za-zñáéíóúÑÁÉÍÓÚ]+)*$"
        if bool(re.match(patron_nombre, campo_nombre)):
            return True
        else:
            return False

    def validar_correo(self, var_correo_electronico):
        """Valida los correos electronicos.

        Args:
            var_correo_electronico (str): correo electrónico

        Devuelve:
            bool: valido o no
        """

        patron_correo = (
            r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2})?$"
        )
        if bool(re.match(patron_correo, var_correo_electronico)):
            return True
        else:
            return False

    def sitios_web(self, campo_sitio, nombre_campo):
        """Valida los campos de sitio web y perfil

        Args:
            campo_sitio (str): URL sitio web
            nombre_campo (str): Nombre del campo a validar

        Devuelve:
            bool: validado o no
        """
        try:
            sitio_bol = False
            patron_sitio = (
                r"^(www\.)?[\w-]+\.[a-z]{2,3}(?:\.[a-z]{2,3})?(\/profile\/\d+)?$"
            )
            if nombre_campo == "sitio":
                if bool(re.match(patron_sitio, campo_sitio)):
                    sitio_bol = True
                else:
                    sitio_bol = False
            else:
                if campo_sitio.capitalize() == "No":
                    campo_sitio = "No"
                    sitio_bol = True
                else:
                    if bool(re.match(patron_sitio, campo_sitio)):
                        sitio_bol = True
                    else:
                        sitio_bol = False
            return sitio_bol
        except Exception:
            self.reg_errores = RegistroLogError(
                80, "Validacion", datetime.datetime.now()
            )
            self.reg_errores.registrar()
            return False

    # def validar_sitio(self, sitio):

    def validar_telefono(self, telefono):
        """Valida el campo del teléfono

        Args:
            telefono (str): telefono

        Devuelve:
            bool: validado o no
        """
        try:
            patron_telefono = r"^\+\d{8,16}$"
            return bool(re.match(patron_telefono, telefono))
        except Exception:
            self.reg_errores = RegistroLogError(
                100, "Validacion", datetime.datetime.now()
            )
            self.reg_errores.registrar()
            return False

    def validar(
        self,
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
    ):
        """Validación de campos

        Args:
            accion (str): Origen de la acción
            var_indice (str): Indice
            var_nombre_cliente (str): Nombre cliente
            var_apellido_cliente (_str): Apellido cliente
            var_contacto (str): Persona de contacto
            var_correo_electronico (str): Correo electrónico
            var_telefono (str): Número de teléfono
            var_sitio (str): Sitio web
            var_perfil (str): Sitio web secundario
            tree (tree): Treeview

        Devuelve:
            bool: validado o no
        """

        id = var_indice

        nombre_cliente = " ".join(var_nombre_cliente.split())
        apellido_cliente = " ".join(var_apellido_cliente.split())
        contacto = " ".join(var_contacto.split())
        correo_electronico = " ".join(var_correo_electronico.split())
        telefono = " ".join(var_telefono.split())
        sitio_web = " ".join(var_sitio.split())
        otro_perfil = " ".join(var_perfil.split())
        # print(type(nombre_cliente), nombre_cliente)

        criterios_mensaje = f"{self.criterio_correo}.\n{self.criterio_campos}.\n{self.criterio_sitio}.\n{self.criterio_perfil}.\n{self.criterio_telefono}."

        diccionario_valido = {
            "nombre de cliente": self.validar_nombres(nombre_cliente),
            "apellido_cliente": self.validar_nombres(apellido_cliente),
            "nombre de contacto": self.validar_nombres(contacto),
            "correo electrónico": self.validar_correo(correo_electronico),
            "teléfono": self.validar_telefono(telefono),
            "sitio web": self.sitios_web(sitio_web, "sitio"),
            "otro perfil": self.sitios_web(otro_perfil, "perfil"),
        }
        try:
            if any(v is False for v in diccionario_valido.values()):
                claves_falsas = [
                    key for key, value in diccionario_valido.items() if value is False
                ]
                mensaje = ", ".join(claves_falsas)
                showinfo(
                    "¡Atención!",
                    f"Hay un problema, revise: {mensaje}.\nNo se {accion} los datos.",
                    detail=f"{criterios_mensaje}",
                )
                return False
            else:
                return True
        except Exception:
            self.reg_errores = RegistroLogError(
                170, "Validacion", datetime.datetime.now()
            )
            self.reg_errores.registrar()

            return False
