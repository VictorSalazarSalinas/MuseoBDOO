from persistent import Persistent


class Obra(Persistent):

    def __init__(
        self,
        id_obra,
        titulo,
        anio,
        tipo,
        descripcion,
        estado="Disponible",
        artista=None,
        coleccion=None,
        sala=None
    ):
        self.id_obra = id_obra
        self.titulo = titulo
        self.anio = anio
        self.tipo = tipo
        self.descripcion = descripcion
        self.estado = estado

        self.artista = artista
        self.coleccion = coleccion
        self.sala = sala

    def cambiar_ubicacion(self, nueva_sala):
        self.sala = nueva_sala

    def prestar(self):
        if self.estado == "Disponible":
            self.estado = "Prestada"
            return True
        return False

    def devolver(self):
        self.estado = "Disponible"

    def esta_disponible(self):
        return self.estado == "Disponible"

    def __str__(self):
        return f"{self.id_obra} - {self.titulo} - {self.estado}"