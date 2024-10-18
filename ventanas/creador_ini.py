import configparser


def crear_config():
    config = configparser.ConfigParser()
    config["imagenes"] = {
        "favicon_icon": "imagenes/favicon.ico",
        "imag_pinky": "imagenes/Pinky_011.png",
        "bloqueado_icon": "imagenes/locked.png",
        "usuario": "imagenes/user_icon.png",
        "password": "ventanas/imagenes/password.png",
    }
    config["bd_clientes"] = {"nombre": "clientes_nuevo.db", "tabla": "personas",}
    config["bd_usuarios"] = {"nombre": "clientes_nuevo.db", "tabla": "usuarios",}
    config["marco"] = {
        "bg": "#35374B",
        "padx": 5,
        "pady": 5,
    }
    config["titulo"] = {
        "texto": "Administración de Clientes",
        "bg": "#78A083",
        "fuente": "Helvetica 16 bold",
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
        "background": "white",
        "fg": "#35374B",
        "width": 25,
    }
    # backound campos estrada:"#35374B"
    config["texto_login"] = {
        "usuario": "Nombre de Usuario",
        "contraseña": "Contraseña",
        "boton": "Iniciar Sesión",
    }
    config["botones"] = {
        "font": "Helvetica 11 bold",
        "background": "#78A083",
        "fg": "white",
        "padx": 1,
        "pady": 1,
    }
    config["treeview"] = {
        "background_headings": "#78A083",
        "foreground_headings": "white",
        "fuente_headings": "Helvetica 11 bold",
        "fieldbackground": "#D3D3D3",
        "fuente_treeview": "Helvetica 11",
        "fore_treeview": "#bababa",
        "fondo_treeview": "#4E5275",
        "selected": "#35374B",
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
        "Nombre": 150,
        "Apellido": 150,
        "Contacto": 150,
        "Correo": 150,
        "Tel": 150,
        "Sitio": 150,
        "Perfil": 150,
    }
    config["texto_botones"] = {
        "agregar": "Agregar",
        "vaciar": "Vaciar Entradas",
        "borrar": "Borrar",
        "modificar": "Modificar",
        "importar": "Importar Datos",
        "salir": "Salir",
    }

    with open("../referencia/config.ini", "w", encoding="utf-8") as config_file:
        config.write(config_file)


def leer_config(diccionario):
    dato = {}
    config = configparser.ConfigParser()
    config.read("../referencia/config.ini", encoding="utf-8")

    config.sections()
    for key in config[diccionario]:
        dato.update({key: config[diccionario][key]})  # config[diccionario][key]
    return dato


if __name__ == "__main__":
    #crear_config()

    imagenes = leer_config("imagenes")
    base_clientes = leer_config("bd_clientes")
    base_usuarios = leer_config("bd_usuarios")
    marco = leer_config("marco")
    titulo = leer_config("titulo")
    campos_etiquetas = leer_config("campos_etiquetas")
    campos_entradas = leer_config("campos_entradas")
    botones = leer_config("botones")
    treeview = leer_config("treeview")
    col_treeview = leer_config("col_treeview")
    val_col_treeview = leer_config("val_col_treeview")
    texto_botones = leer_config("texto_botones")  
    


