import transaction

from modelos.artista import Artista
from modelos.obra import Obra
from modelos.coleccion import Coleccion
from modelos.exposicion import Exposicion
from modelos.sala import Sala
from modelos.prestamo import Prestamo
from modelos.visitante import Visitante


class GestionMuseo:

    def __init__(self, root):
        self.root = root

    def registrar_artista(
        self,
        id_artista,
        nombre,
        nacionalidad,
        anio_nacimiento
    ):
        if id_artista in self.root.artistas:
            return False

        artista = Artista(
            id_artista,
            nombre,
            nacionalidad,
            anio_nacimiento
        )

        self.root.artistas[id_artista] = artista
        transaction.commit()

        return True

    def registrar_obra(
        self,
        id_obra,
        titulo,
        anio,
        tipo,
        descripcion,
        id_artista=None
    ):
        if id_obra in self.root.obras:
            return False

        artista = None

        if id_artista:
            artista = self.root.artistas.get(id_artista)

        obra = Obra(
            id_obra,
            titulo,
            anio,
            tipo,
            descripcion,
            artista=artista
        )

        self.root.obras[id_obra] = obra
        transaction.commit()

        return True

    def registrar_coleccion(
        self,
        id_coleccion,
        nombre,
        descripcion
    ):
        if id_coleccion in self.root.colecciones:
            return False

        coleccion = Coleccion(
            id_coleccion,
            nombre,
            descripcion
        )

        self.root.colecciones[id_coleccion] = coleccion
        transaction.commit()

        return True

    def registrar_sala(
        self,
        id_sala,
        nombre,
        capacidad,
        ubicacion
    ):
        if id_sala in self.root.salas:
            return False

        sala = Sala(
            id_sala,
            nombre,
            capacidad,
            ubicacion
        )

        self.root.salas[id_sala] = sala
        transaction.commit()

        return True

    def registrar_exposicion(
        self,
        id_exposicion,
        nombre,
        fecha_inicio,
        fecha_fin,
        id_sala=None
    ):
        if id_exposicion in self.root.exposiciones:
            return False

        sala = None

        if id_sala:
            sala = self.root.salas.get(id_sala)

        exposicion = Exposicion(
            id_exposicion,
            nombre,
            fecha_inicio,
            fecha_fin,
            sala
        )

        self.root.exposiciones[id_exposicion] = exposicion

        if sala:
            sala.agregar_exposicion(exposicion)

        transaction.commit()

        return True

    def registrar_visitante(
        self,
        id_visitante,
        nombre,
        institucion,
        contacto
    ):
        if id_visitante in self.root.visitantes:
            return False

        visitante = Visitante(
            id_visitante,
            nombre,
            institucion,
            contacto
        )

        self.root.visitantes[id_visitante] = visitante
        transaction.commit()

        return True

    def registrar_prestamo(
        self,
        id_prestamo,
        fecha_prestamo,
        fecha_devolucion,
        destino,
        id_obra,
        id_visitante
    ):
        if id_prestamo in self.root.prestamos:
            return False

        obra = self.root.obras.get(id_obra)
        visitante = self.root.visitantes.get(id_visitante)

        if obra is None or visitante is None:
            return False

        if not obra.esta_disponible():
            return False

        prestamo = Prestamo(
            id_prestamo,
            fecha_prestamo,
            fecha_devolucion,
            destino,
            obra,
            visitante
        )

        prestamo.registrar_prestamo()

        self.root.prestamos[id_prestamo] = prestamo
        transaction.commit()

        return True

    def eliminar_obra(self, id_obra):
        if id_obra not in self.root.obras:
            return False

        del self.root.obras[id_obra]
        transaction.commit()

        return True

    def eliminar_exposicion(self, id_exposicion):
        if id_exposicion not in self.root.exposiciones:
            return False

        exposicion = self.root.exposiciones[id_exposicion]

        if exposicion.sala:
            if exposicion in exposicion.sala.exposiciones:
                exposicion.sala.exposiciones.remove(exposicion)

        del self.root.exposiciones[id_exposicion]
        transaction.commit()

        return True

    def asignar_obra_a_coleccion(
        self,
        id_obra,
        id_coleccion
    ):
        obra = self.root.obras.get(id_obra)
        coleccion = self.root.colecciones.get(id_coleccion)

        if obra is None or coleccion is None:
            return False

        obra.coleccion = coleccion
        transaction.commit()

        return True

    def asignar_obra_a_sala(
        self,
        id_obra,
        id_sala
    ):
        obra = self.root.obras.get(id_obra)
        sala = self.root.salas.get(id_sala)

        if obra is None or sala is None:
            return False

        obra.cambiar_ubicacion(sala)
        transaction.commit()

        return True