from persistent import Persistent

class Sala(Persistent):

    def __init__(self, id_sala, nombre, capacidad, ubicacion):
        self.id_sala = id_sala
        self.nombre = nombre
        self.capacidad = capacidad
        self.ubicacion = ubicacion
        self.exposiciones = []

    def tiene_capacidad(self):
        return len(self.exposiciones) < self.capacidad

    def agregar_exposicion(self, exposicion):
        if self.tiene_capacidad():
            if exposicion not in self.exposiciones:
                self.exposiciones.append(exposicion)
                exposicion.sala = self
                return True
        return False

    def __str__(self):
        return f"Sala {self.nombre} (Capacidad: {self.capacidad})"