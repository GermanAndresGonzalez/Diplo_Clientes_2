referencia_tree = {
    "nombre_columnas": {
        "#0": "ID",
        "NOMBRES": "NOMBRES",
        "APELLIDOS": "APELLIDOS",
        "CONTACTO": "CONTACTO",
        "CORREO": "CORREO",
        "TELEFONO": "TELEFONO",
        "SITIO WEB": "SITIO WEB",
        "PERFIL": "PERFIL",
    },
    "texto_etiquetas": "Los sitios web no deben incluir: 'http://',\n'https://' o una '/' al final de la URL.",
}

if __name__ == "__main__":

    # print(list(referencia_tree["nombre_columnas"]))
    # print(list(referencia_tree["nombre_columnas"])[0])

    claves = list(referencia_tree["nombre_columnas"].keys())
    for i, clave in enumerate(claves):
        print(clave)
