""" --------------------------------------------------------- TASK   | main """
"""
Aplicacion de lista de tareas
    - Crear tareas
    - Editar las tareas
    - Marcar como completadas
    - Eliminar las tareas
"""
import sqlite3
from tkinter import *
from tkinter import messagebox as mss
from dataclasses import dataclass
from bbdd import crear_tabla

# -------------------------------------------------- Variables Globales de Color

FOREGROUND : str = "#212529"    # font color, screens and buttons
BACKGROUND : str = "#dee2e6"    # window color
BUTTONS : str = "#ced4da"       # Buttons color

root = Tk()


# ------------------------------------------------------------------------ Tarea
# Clase creadora de tareas
# descripcion: contenido de la tarea
# status: condicion de la tarea, pendiente (defaut) o completada

@dataclass
class Tarea:
    descripcion: str
    status: str = "pendiente"
    
    def __str__(self):
        return f"tarea: {self.descripcion} | status: {self.status}"
    
    # metd editar: cambiar contenido de la tarea    
    def editar(self, nueva_descripcion):
        self.descripcion = nueva_descripcion
    
    # metd check: cambiar status de la tarea
    def check(self):
        self.status = "completada"
    
    # metd eliminar: eliminar la tarea        
    def eliminar():
        pass


@dataclass
class Interface():
    def __init__(self, window):
        self.window = window
        self.window.title("TASK")
        self.window.config(bg=BACKGROUND)
        

# ----------------------------------------------------------------------- main()
def main():
    try:
        with sqlite3.connect("tareas_bd") as conexion:
            if crear_tabla(conexion):
                print("La tabla 'tabla_tareas' se creó con éxito.")
            else:
                print("No se pudo crear la tabla 'tabla_tareas'.")
    except sqlite3.Error as e:
        print(f"Ocurrió un error al conectar a la base de datos: {e}")


iu = Interface(root)

if __name__ == "__main__":
    
    root.mainloop()
    main()
    # tareas 
    t_prueba = Tarea("Hacer la aplicacion")
    print(t_prueba)