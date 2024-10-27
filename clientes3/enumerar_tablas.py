import sqlite3


def listar_tablas(nombre_bd):
    try:
        conexion = sqlite3.connect(nombre_bd)
        cursor = conexion.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tablas = cursor.fetchall()
        for tabla in tablas:
            print(tabla[0])
        conexion.close()
    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos: {e}")


nombre_bd = "datos/clientes_nuevo.db"
listar_tablas(nombre_bd)
