"""
Usado para obtener la ruta de carpetas anterior a la actual.
"""

import os


def obt_anterior(path: str, levels=1) -> str:
    """
    ruta @param: comienza sin /
    @return: ruta principal solo en los niveles especificados.
    """
    directorio_actual = os.path.dirname(__file__)

    # Obtener ruta de directorio principal
    directorio_principal = directorio_actual
    for i in range(0, levels):
        directorio_principal = os.path.split(directorio_principal)[0]

    file_path = os.path.join(directorio_principal, path)
    return file_path


if __name__ == "__main__":
    prueba = obt_anterior("imagenes")
    ima = prueba + "\\favicon.ico"
    print(ima)
