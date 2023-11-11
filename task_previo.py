""" --------------------------------------------------------- TASK   | main 

Aplicacion de lista de tareas
    - Crear tareas
    - Editar las tareas
    - Marcar como completadas
    - Eliminar las tareas

import sqlite3
from tkinter import *
from bbdd import *

# -------------------------------------------------- Variables Globales de Color
FOREGROUND : str = "#473815"
BACKGROUND : str = "#FFC94D"      # window color
BUTTONS : str = "#FF5F00"       # Buttons color
COMPLETADO: str = ""


root = Tk()


class Interface():
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("TASK")
        self.ventana.geometry("560x500")
        self.ventana.config(bg=BACKGROUND)

        self.ui_tarea = Label(root, text='Tarea >', padx=3, bg=BACKGROUND, fg=FOREGROUND)
        self.ui_tarea.grid(row=0, column=0, padx=3, pady=3)

        self.ui_descripcion = Entry(root, width=64, bd=0, bg=BACKGROUND)
        self.ui_descripcion.grid(row=0, column=1, padx=3, pady=3)

        self.ui_boton = Button(root, text='  ✚  ', bg=BUTTONS, fg='#ffffff', bd=0, padx=3, command=lambda:nueva_tarea(self))
        self.ui_boton.grid(row=0, column=2, padx=5, pady=3)

        self.ui_lista_tareas = LabelFrame(root, text='Mis tareas', pady=5, padx=5, bg=BACKGROUND)
        self.ui_lista_tareas.grid(row=1, column=0, columnspan=3, sticky='nswe', padx=5)

        self.ui_descripcion.focus()
        

        
        # agregar nueva tarea ----- add a new task -----
        def nueva_tarea(self):
            tarea = self.ui_descripcion.get()
            if tarea:
                cursor.execute('''
                    INSERT INTO tabla_tareas (DESCRIPCION, STATUS) VALUES (?,?)''', (tarea, "pendiente"))
                conexion.commit()
                self.ui_descripcion.delete(0, END)
                renderizar()
            else:
                pass

        
        def check(self, ID):
            def marcado():
                tarea = cursor.execute("SELECT * FROM tabla_tareas WHERE ID = ?", (ID,)).fetchone()
                cursor.execute("UPDATE tabla_tareas SET STATUS = ? WHERE ID = ?", ("completado", ID))
                conexion.commit()
                renderizar()
            return marcado

def renderizar(self):
    global COMPLETADO
    rows = cursor.execute("SELECT * FROM tabla_tareas").fetchall()

    for widget in self.ui_lista_tareas.winfo_children():
                widget.destroy()
            
    for i in range(0, len(rows)):
        rows_id = rows[i][0]
        rows_descripcion = rows[i][1]
        rows_status = rows[i][2]
        color = FOREGROUND if COMPLETADO else "#000000"

        self.ui_row_tarea = Checkbutton(
            self.ui_lista_tareas, 
            text=rows_descripcion, 
            width=67, 
            anchor='w', 
            fg=color,
            bg=BACKGROUND,
            command=check(self, rows_id))
        self.ui_row_tarea.grid(row=i, column=0, sticky='w')
                
        self.ui_boton_borrar = Button(
            self.ui_lista_tareas, 
            text='⌫', 
            padx=5,
            bd=0,
            bg=BACKGROUND)
        self.ui_boton_borrar.grid(row=i, column=1)
                
        self.ui_row_tarea.select() if COMPLETADO else self.ui_row_tarea.deselect()        

        



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
    
    main()
    renderizar(iu)
    root.mainloop()

"""