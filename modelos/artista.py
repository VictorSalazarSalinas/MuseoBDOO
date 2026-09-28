class Artista:

    def __init__(self, id_artista, nombre, nacionalidad, anio_nacimiento):
        self.id_artista = id_artista
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.anio_nacimiento = anio_nacimiento

    def __str__(self):
        return f"{self.nombre} ({self.nacionalidad})"