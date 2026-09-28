from persistent import Persistent

class Prestamo(Persistent):

    def __init__(self, id_prestamo, fecha_prestamo, fecha_devolucion, obra, visitante):
        self.id_prestamo = id_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.obra = obra
        self.visitante = visitante
        self.estado = "Vigente"
        
        # Marcar la obra como prestada al crear el registro
        if self.obra:
            self.obra.prestar()

    def finalizar_prestamo(self):
        self.estado = "Devuelto"
        if self.obra:
            self.obra.devolver()

    def esta_vigente(self):
        return self.estado == "Vigente"

    def __str__(self):
        return f"Préstamo #{self.id_prestamo} - Obra: {self.obra.titulo}"