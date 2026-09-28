from persistent import Persistent

class Visitante(Persistent):

    def __init__(self, id_visitante, nombre, institucion, contacto):
        self.id_visitante = id_visitante
        self.nombre = nombre
        self.institucion = institucion
        self.contacto = contacto

    def __str__(self):
        return f"Visitante: {self.nombre} ({self.institucion})"