from persistent import Persistent


class Prestamo(Persistent):

    def __init__(
        self,
        id_prestamo,
        fecha_prestamo,
        fecha_devolucion,
        destino,
        obra,
        visitante,
        estado="Activo"
    ):
        self.id_prestamo = id_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.destino = destino
        self.estado = estado
        self.obra = obra
        self.visitante = visitante

    def registrar_prestamo(self):
        if self.obra.esta_disponible():
            self.obra.prestar()
            self.estado = "Activo"
            return True
        return False

    def finalizar_prestamo(self):
        self.obra.devolver()
        self.estado = "Devuelto"

    def esta_vigente(self):
        return self.estado == "Activo"

    def __str__(self):
        return f"{self.id_prestamo} - {self.obra.titulo} - {self.estado}"