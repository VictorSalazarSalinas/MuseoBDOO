from persistent import Persistent
from persistent.list import PersistentList


class Exposicion(Persistent):

    def __init__(
        self,
        id_exposicion,
        nombre,
        fecha_inicio,
        fecha_fin,
        sala=None
    ):
        self.id_exposicion = id_exposicion
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.sala = sala
        self.obras = PersistentList()

    def agregar_obra(self, obra):
        if obra not in self.obras:
            self.obras.append(obra)
            obra.estado = "En Exposición"
            obra.sala = self.sala
            return True
        return False

    def retirar_obra(self, obra):
        if obra in self.obras:
            self.obras.remove(obra)
            obra.estado = "Disponible"
            return True
        return False

    def esta_activa(self, fecha_actual):
        return self.fecha_inicio <= fecha_actual <= self.fecha_fin

    def __str__(self):
        return f"{self.id_exposicion} - {self.nombre}"