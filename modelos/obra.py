class Obra:

    def __init__(
        self,
        id_obra,
        titulo,
        anio,
        tipo,
        tecnica,
        artista=None
    ):
        self.id_obra = id_obra
        self.titulo = titulo
        self.anio = anio
        self.tipo = tipo
        self.tecnica = tecnica
        self.artista = artista
        self.estado = "Disponible"
        self.ubicacion = None

    def cambiar_ubicacion(self, nueva_ubicacion):
        self.ubicacion = nueva_ubicacion

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