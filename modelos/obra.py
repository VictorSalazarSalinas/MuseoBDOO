from persistent import Persistent

class Obra(Persistent):

    def __init__(self, id_obra, titulo, anio, tipo, tecnica, descripcion="", artista=None, coleccion=None):
        self.id_obra = id_obra
        self.titulo = titulo
        self.anio = anio
        self.tipo = tipo
        self.tecnica = tecnica
        self.descripcion = descripcion
        self.artista = artista
        self.coleccion = coleccion
        self.estado = "Disponible"
        self.sala = None

    def cambiar_ubicacion(self, nueva_sala):
        self.sala = nueva_sala

    def prestar(self):
        if self.esta_disponible():
            self.estado = "Prestada"
            return True
        return False

    def devolver(self):
        self.estado = "Disponible"

    def esta_disponible(self):
        return self.estado == "Disponible"

    def __str__(self):
        return f"{self.titulo} - {self.tipo}"