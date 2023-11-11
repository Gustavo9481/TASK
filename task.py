""" --------------------------------------------------------- TASK   | main """
"""
Aplicacion de lista de tareas
    - Crear tareas
    - Editar las tareas
    - Marcar como completadas
    - Eliminar las tareas
"""
import sqlite3
import tkinter as tk
from tarea import Tarea
from bbdd import *

BACKGROUND = "#e3d664"
FOREGROUND = "#5f5711"
BOTON = "#e8a15e"

root = tk.Tk()




def main():
    try:
        conexion = sqlite3.connect("task.bd")
        if crear_tabla(conexion):
            print("La tabla 'tabla_task' se creó con éxito.")
        else:
            print("No se pudo crear la tabla 'tabla_task'.")
    except sqlite3.Error as e:
        print(f"Ocurrió un error al conectar a la base de datos: {e}")



def mostrar():
  cursor = conexion.cursor()
  rows = cursor.execute("SELECT * FROM tabla_task").fetchall()
  for widget in lista_tareas.winfo_children():  # elimina los elementos de la pantalla 
    widget.destroy()
  for i in range(0, len(rows)):
    n = int(rows[i][0])
    descripcion = rows[i][1]
    status = str(rows[i][2]) 

    btn = "󰄲" if status=="completado" else "󰄱"

    linea_tarea = tk.Label(lista_tareas, bg=BACKGROUND, text=descripcion, width=45, anchor='w')
    boton_status = tk.Button(lista_tareas, text=btn, font=("", 15), bg=BACKGROUND, fg=FOREGROUND, bd=0, padx=5, command=check(n))
    boton_borrar = tk.Button(lista_tareas, text='', bg=BACKGROUND, fg=FOREGROUND,  bd=0, padx=5)
    
    linea_tarea.grid(row=i, column=0, sticky='w')
    boton_status.grid(row=i, column=1)
    boton_borrar.grid(row=i, column=2)
    
    

    


 
def nueva_tarea():
    tarea = Tarea(registro_tarea.get())
    t_descripcion = str(tarea.descripcion)
    t_status = str(tarea.status) 
    if tarea:
        try:
            cursor = conexion.cursor()
            cursor.execute("""
                    INSERT INTO tabla_task (DESCRIPCION, STATUS) VALUES (?,?)""", (t_descripcion, t_status)
                )
            conexion.commit()
            registro_tarea.delete(0, tk.END)
            mostrar()
            print(type(t_descripcion))
        except Exception as e:
            print(f"Ocurrió un error al intentar insertar la tarea: {e}")
    else:
        pass




def check(id):
    n_status = ""
    def marcar():
        cursor = conexion.cursor()
        tarea = cursor.execute("SELECT * FROM tabla_task WHERE ID = ?", (id,)).fetchone()
        n_status = "completado" if tarea[2]=="pendiente" else "pendiente"
        cursor.execute("UPDATE tabla_task SET STATUS = ? WHERE ID = ?", (n_status, id))
        conexion.commit()
        mostrar()
    return marcar



# interface
root.geometry("400x500")
root.title("TASK")
root.config(bg=BACKGROUND)

# título de la aplicación
titulo = tk.Label(root, text="TASK  ", bg=BACKGROUND, fg=FOREGROUND, justify=tk.CENTER)
    
# fila de registro de tarea
etiqueta_tarea = tk.Label(root, text='  Tarea >', bg=BACKGROUND, fg=FOREGROUND, padx=3)
registro_tarea = tk.Entry(root, width=40, bg=BACKGROUND, bd=0)
boton_nueva_tarea = tk.Button(root, text='  ✚  ', bg=BOTON, fg=FOREGROUND, bd=0, padx=3, command=lambda:nueva_tarea())

# frame de lista de tareas
lista_tareas = tk.LabelFrame(root, bg=BACKGROUND, bd=0, pady=5, padx=5)

titulo.grid(row=0, columnspan=3, padx=3, pady=3)
etiqueta_tarea.grid(row=1, column=0, padx=3, pady=3)
registro_tarea.grid(row=1, column=1, padx=3, pady=3)
boton_nueva_tarea.grid(row=1, column=2, padx=3, pady=3)
lista_tareas.grid(row=2, column=0, columnspan=3, sticky='nswe', padx=5)



if __name__ == "__main__":
    
    main()
    mostrar()
    root.mainloop()
