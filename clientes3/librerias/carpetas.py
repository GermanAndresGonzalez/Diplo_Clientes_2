import os


def obtAnterior(path: str, levels=1) -> str:
    """
    @param path: starts without /
    @return: Parent path at the specified levels above.
    """
    current_directory = os.path.dirname(__file__)

    parent_directory = current_directory
    for i in range(0, levels):
        parent_directory = os.path.split(parent_directory)[0]

    file_path = os.path.join(parent_directory, path)
    return file_path


if __name__ == "__main__":
    prueba = obtAnterior("imagenes")
    ima = prueba + "\\favicon.ico"
    print(ima)
