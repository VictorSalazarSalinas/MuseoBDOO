from persistent import Persistent
from persistent.list import PersistentList


class Sala(Persistent):

    def __init__(self, id_sala, nombre, capacidad, ubicacion):
        self.id_sala = id_sala
        self.nombre = nombre
        self.capacidad = capacidad
        self.ubicacion = ubicacion
        self.exposiciones = PersistentList()

    def tiene_capacidad(self):
        return len(self.exposiciones) < self.capacidad

    def agregar_exposicion(self, exposicion):
        if exposicion not in self.exposiciones and self.tiene_capacidad():
            self.exposiciones.append(exposicion)
            return True
        return False

    def __str__(self):
        return f"{self.id_sala} - {self.nombre}"