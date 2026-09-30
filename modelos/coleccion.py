from persistent import Persistent


class Coleccion(Persistent):

    def __init__(self, id_coleccion, nombre, descripcion):
        self.id_coleccion = id_coleccion
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return f"{self.id_coleccion} - {self.nombre}"