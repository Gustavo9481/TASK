""" ------------------------------------------------- TASK   |  Clase Tarea """
"""
Clase creadora de Tareas
"""


class Tarea:
    def __init__(self, descripcion, status="pendiente"):
        self.descripcion = descripcion
        self.status = status


    def __str__(self):
        return f"{self.descripcion} => {self.status}"


    def editar_descripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion


    def editar_status(self):
        self.status = "completada"