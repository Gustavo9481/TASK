""" ----------------------------------------------- TASK   |  base de datos """
"""
Conexión a base de datos 'task.db'
Creación de 'tabla_task' que contiene las tareas
"""

import sqlite3


# ---------------------------------------------------------------- crear_tabla()
# Si no existe, crea la tabla_tareas, anuncia error en caso de haberlo
# esquema de la tabla:
# |  ID  |  DESCRIPCION  | STATUS  |

conexion = sqlite3.connect("task.db") 

def crear_tabla(conexion):
    cursor = conexion.cursor()
    consulta = """
    CREATE TABLE IF NOT EXISTS tabla_task (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        DESCRIPCION VARCHAR(100),
        STATUS VARCHAR(10)
    )
    """
    try:
        cursor.execute(consulta)
    except sqlite3.Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        return False
    return True



