""" ------------------------------------------------- TASK  | base de datos """

import sqlite3


# ---------------------------------------------------------------- crear_tabla()
# Si no existe, crea la tabla_tareas, anuncia error en caso de haberlo
# esquema de la tabla:
# |  ID  |  DESCRIPCION  | STATUS  |

def crear_tabla(conexion):
    consulta = """
    CREATE TABLE IF NOT EXISTS tabla_tareas (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        DESCRIPCION VARCHAR(100),
        STATUS VARCHAR(10)
    )
    """
    try:
        cursor = conexion.cursor()
        cursor.execute(consulta)
    except sqlite3.Error as e:
        print(f"Ocurrió un error al ejecutar la consulta: {e}")
        return False
    return True