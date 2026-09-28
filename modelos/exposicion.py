from persistent import Persistent

class Exposicion(Persistent):

    def __init__(self, id_exposicion, nombre, fecha_inicio, fecha_fin, sala=None):
        self.id_exposicion = id_exposicion
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.sala = sala
        self.obras = []
        self.activa = True

    def agregar_obra(self, obra):
        if obra not in self.obras:
            self.obras.append(obra)
            return True
        return False

    def retirar_obra(self, obra):
        if obra in self.obras:
            self.obras.remove(obra)
            return True
        return False

    def esta_activa(self):
        return self.activa

    def __str__(self):
        return f"Exposición: {self.nombre}"