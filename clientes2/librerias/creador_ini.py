import configparser


def crear_config():
    config = configparser.ConfigParser()
    config["aplicacion"] = {
        "Nombre": "Administración de Clientes",
        "github": "https://github.com/GermanAndresGonzalez",
        "correo": "gandresgonzalez@gmail.com",
        "acerca": "Información de Clientes.\nVersión 1.00\nPráctica del Curso de Diplomatura en Python de la UTN.\nCreado por Germán Andrés González.\n",
        "version": "v1.00",
        "titulo_p": "Clientes v1.00",
        "geometria": "1320x750",
        "titulo": "Acerca de Clientes v1.00",
    }
    config["imagenes"] = {
        "favicon_icon": "imagenes/favicon.ico",
        "imag_pinky": "imagenes/Pinky_011.png",
        "bloqueado_icon": "imagenes/locked.png",
        "usuario": "imagenes/user_icon.png",
        "password": "ventanas/imagenes/password.png",
    }
    config["bd_clientes"] = {
        "nombre": "clientes_nuevo.db",
        "tabla": "personas",
    }
    config["bd_usuarios"] = {
        "nombre": "clientes_nuevo.db",
        "tabla": "usuarios",
    }
    config["marco"] = {
        "bg": "#35374B",
        "padx": 5,
        "pady": 5,
    }
    config["titulo"] = {
        "text": "Administración de Clientes",
        "bg": "#78A083",
        "fg": "black",
        "font": "Helvetica 16 bold",
        "width": 60,
        "height": 1,
    }
    config["campos_etiquetas"] = {
        "font": "Helvetica 12",
        "background": "#35374B",
        "fg": "white",
        "padx": 5,
        "pady": 5,
    }
    config["nombre_campos_entradas"] = {
        "indice": "Indice",
        "nombre": "Nombre",
        "apellido": "Apellido",
        "contacto": "Persona de contacto",
        "email": "Correo electrónico",
        "telefono": "Número de telefono",
        "sitio": "Sitio web",
        "perfil": "Otro Perfil",
    }
    config["campos_entradas"] = {
        "font": "Helvetica 11 bold",
        "background": "#78A083",
        "fg": "#35374B",
        "width": 40,
        "readonlybackground": "#78A083",
    }
    # backound campos estrada:"#35374B"
    config["texto_login"] = {
        "usuario": "Nombre de Usuario",
        "contraseña": "Contraseña",
        "boton": "Iniciar Sesión",
    }
    config["texto_botones"] = {
        "agregar": "Agregar",
        "vaciar": "Vaciar Entradas",
        "borrar": "Borrar",
        "modificar": "Modificar",
        "importar": "Importar Datos",
        "salir": "Salir",
    }
    config["botones"] = {
        "font": "Helvetica 11 bold",
        "background": "#78A083",
        "fg": "black",
        "padx": 1,
        "pady": 1,
        "width": "30",
    }
    config["val_treeview"] = {
        "fuente": "Helvetica 11",
        "fuente_tree": "Helvetica 11",
        "background": "#4E5275",
        "foreground": "#bababa",
        "fieldbackground": "#D3D3D3",
        "fuente_heading": "Helvetica 11 bold",
        "background_heading": "#78A083",
        "foreground_heading": "white",
        "b_selected": "#78A083",
        "f_selected": "white",
    }

    config["col_treeview"] = {
        "ID": "ID",
        "Nombre": "Nombre",
        "Apellido": "Apellido",
        "Contacto": "Contacto",
        "Correo": "Correo-E",
        "Tel": "Teléfono",
        "Sitio": "Sitio Web",
        "Perfil": "Perfil",
    }
    config["val_col_treeview"] = {
        "ID": 60,
        "Nombre": 100,
        "Apellido": 100,
        "Contacto": 150,
        "Correo": 160,
        "Tel": 150,
        "Sitio": 150,
        "Perfil": 150,
    }

    with open("datos/config.ini", "w", encoding="utf-8") as config_file:
        config.write(config_file)


def leer_config(diccionario):
    dato = {}
    config = configparser.ConfigParser()
    config.read("datos/config.ini", encoding="utf-8")

    config.sections()
    for key in config[diccionario]:
        dato.update({key: config[diccionario][key]})  # config[diccionario][key]
    return dato


if __name__ == "__main__":
    crear_config()
