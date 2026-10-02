import transaction

from modelos.artista import Artista
from modelos.obra import Obra
from modelos.coleccion import Coleccion
from modelos.exposicion import Exposicion
from modelos.sala import Sala
from modelos.prestamo import Prestamo
from modelos.visitante import Visitante


class GestionMuseo:

    def __init__(self, db):
        self.db = db


    # -------------------------
    # CREATE
    # -------------------------

    def registrar_artista(
        self,
        id_artista,
        nombre,
        nacionalidad,
        anio_nacimiento
    ):
        if id_artista in self.db.root.artistas:
            return None

        artista = Artista(
            id_artista,
            nombre,
            nacionalidad,
            anio_nacimiento
        )

        self.db.root.artistas[id_artista] = artista
        self.db.guardar()

        return artista


    def registrar_obra(
        self,
        id_obra,
        titulo,
        anio,
        tipo,
        descripcion,
        id_artista=None
    ):
        if id_obra in self.db.root.obras:
            return None

        artista = None

        if id_artista:
            artista = self.db.root.artistas.get(id_artista)

        obra = Obra(
            id_obra,
            titulo,
            anio,
            tipo,
            descripcion,
            artista=artista
        )

        self.db.root.obras[id_obra] = obra
        self.db.guardar()

        return obra


    def registrar_coleccion(
        self,
        id_coleccion,
        nombre,
        descripcion
    ):
        if id_coleccion in self.db.root.colecciones:
            return None

        coleccion = Coleccion(
            id_coleccion,
            nombre,
            descripcion
        )

        self.db.root.colecciones[id_coleccion] = coleccion
        self.db.guardar()

        return coleccion


    def registrar_sala(
        self,
        id_sala,
        nombre,
        capacidad,
        ubicacion
    ):
        if id_sala in self.db.root.salas:
            return None

        sala = Sala(
            id_sala,
            nombre,
            capacidad,
            ubicacion
        )

        self.db.root.salas[id_sala] = sala
        self.db.guardar()

        return sala


    def registrar_exposicion(
        self,
        id_exposicion,
        nombre,
        fecha_inicio,
        fecha_fin,
        id_sala=None
    ):
        if id_exposicion in self.db.root.exposiciones:
            return None

        sala = None

        if id_sala:
            sala = self.db.root.salas.get(id_sala)

        exposicion = Exposicion(
            id_exposicion,
            nombre,
            fecha_inicio,
            fecha_fin,
            sala
        )

        self.db.root.exposiciones[id_exposicion] = exposicion

        if sala:
            sala.agregar_exposicion(exposicion)

        self.db.guardar()

        return exposicion


    def registrar_visitante(
        self,
        id_visitante,
        nombre,
        institucion,
        contacto
    ):
        if id_visitante in self.db.root.visitantes:
            return None

        visitante = Visitante(
            id_visitante,
            nombre,
            institucion,
            contacto
        )

        self.db.root.visitantes[id_visitante] = visitante
        self.db.guardar()

        return visitante


    def registrar_prestamo(
        self,
        id_prestamo,
        fecha_prestamo,
        fecha_devolucion,
        id_obra,
        id_visitante
    ):
        obra = self.db.root.obras.get(id_obra)
        visitante = self.db.root.visitantes.get(id_visitante)

        if obra and visitante and obra.esta_disponible():

            prestamo = Prestamo(
                id_prestamo,
                fecha_prestamo,
                fecha_devolucion,
                obra,
                visitante
            )

            prestamo.registrar_prestamo()

            self.db.root.prestamos[id_prestamo] = prestamo
            self.db.guardar()

            return prestamo

        return None


    # -------------------------
    # RELACIONES
    # -------------------------

    def asignar_obra_a_coleccion(
        self,
        id_obra,
        id_coleccion
    ):
        obra = self.db.root.obras.get(id_obra)
        coleccion = self.db.root.colecciones.get(id_coleccion)

        if obra is None or coleccion is None:
            return False

        obra.coleccion = coleccion
        coleccion.agregar_obra(obra)

        self.db.guardar()

        return True


    def asignar_obra_a_sala(
        self,
        id_obra,
        id_sala
    ):
        obra = self.db.root.obras.get(id_obra)
        sala = self.db.root.salas.get(id_sala)

        if obra is None or sala is None:
            return False

        obra.cambiar_ubicacion(sala)

        self.db.guardar()

        return True


    # -------------------------
    # UPDATE
    # -------------------------

    def modificar_artista(
        self,
        id_artista,
        nombre=None,
        nacionalidad=None,
        anio_nacimiento=None
    ):
        artista = self.db.root.artistas.get(id_artista)

        if artista is None:
            return False

        if nombre is not None:
            artista.nombre = nombre

        if nacionalidad is not None:
            artista.nacionalidad = nacionalidad

        if anio_nacimiento is not None:
            artista.anio_nacimiento = anio_nacimiento

        self.db.guardar()

        return True


    def modificar_obra(
        self,
        id_obra,
        titulo=None,
        anio=None,
        tipo=None,
        descripcion=None,
        estado=None
    ):
        obra = self.db.root.obras.get(id_obra)

        if obra is None:
            return False

        if titulo is not None:
            obra.titulo = titulo

        if anio is not None:
            obra.anio = anio

        if tipo is not None:
            obra.tipo = tipo

        if descripcion is not None:
            obra.descripcion = descripcion

        if estado is not None:
            obra.estado = estado

        self.db.guardar()

        return True


    def modificar_coleccion(
        self,
        id_coleccion,
        nombre=None,
        descripcion=None
    ):
        coleccion = self.db.root.colecciones.get(id_coleccion)

        if coleccion is None:
            return False

        if nombre is not None:
            coleccion.nombre = nombre

        if descripcion is not None:
            coleccion.descripcion = descripcion

        self.db.guardar()

        return True


    def modificar_sala(
        self,
        id_sala,
        nombre=None,
        capacidad=None,
        ubicacion=None
    ):
        sala = self.db.root.salas.get(id_sala)

        if sala is None:
            return False

        if nombre is not None:
            sala.nombre = nombre

        if capacidad is not None:
            sala.capacidad = capacidad

        if ubicacion is not None:
            sala.ubicacion = ubicacion

        self.db.guardar()

        return True


    def modificar_exposicion(
        self,
        id_exposicion,
        nombre=None,
        fecha_inicio=None,
        fecha_fin=None
    ):
        exposicion = self.db.root.exposiciones.get(id_exposicion)

        if exposicion is None:
            return False

        if nombre is not None:
            exposicion.nombre = nombre

        if fecha_inicio is not None:
            exposicion.fecha_inicio = fecha_inicio

        if fecha_fin is not None:
            exposicion.fecha_fin = fecha_fin

        self.db.guardar()

        return True


    def modificar_visitante(
        self,
        id_visitante,
        nombre=None,
        institucion=None,
        contacto=None
    ):
        visitante = self.db.root.visitantes.get(id_visitante)

        if visitante is None:
            return False

        if nombre is not None:
            visitante.nombre = nombre

        if institucion is not None:
            visitante.institucion = institucion

        if contacto is not None:
            visitante.contacto = contacto

        self.db.guardar()

        return True


    # -------------------------
    # DELETE
    # -------------------------

    def eliminar_artista(self, id_artista):

        if id_artista not in self.db.root.artistas:
            return False

        del self.db.root.artistas[id_artista]

        self.db.guardar()

        return True


    def eliminar_obra(self, id_obra):

        if id_obra not in self.db.root.obras:
            return False

        obra = self.db.root.obras[id_obra]

        if obra.coleccion and obra in obra.coleccion.obras:
            obra.coleccion.obras.remove(obra)

        del self.db.root.obras[id_obra]

        self.db.guardar()

        return True


    def eliminar_coleccion(self, id_coleccion):

        if id_coleccion not in self.db.root.colecciones:
            return False

        coleccion = self.db.root.colecciones[id_coleccion]

        for obra in coleccion.obras:
            obra.coleccion = None

        del self.db.root.colecciones[id_coleccion]

        self.db.guardar()

        return True


    def eliminar_sala(self, id_sala):

        if id_sala not in self.db.root.salas:
            return False

        sala = self.db.root.salas[id_sala]

        for obra in self.db.root.obras.values():
            if obra.sala == sala:
                obra.sala = None

        del self.db.root.salas[id_sala]

        self.db.guardar()

        return True


    def eliminar_exposicion(self, id_exposicion):

        if id_exposicion not in self.db.root.exposiciones:
            return False

        exposicion = self.db.root.exposiciones[id_exposicion]

        if exposicion.sala:
            if exposicion in exposicion.sala.exposiciones:
                exposicion.sala.exposiciones.remove(exposicion)

        for obra in exposicion.obras:
            obra.estado = "Disponible"

        del self.db.root.exposiciones[id_exposicion]

        self.db.guardar()

        return True


    def eliminar_visitante(self, id_visitante):

        if id_visitante not in self.db.root.visitantes:
            return False

        del self.db.root.visitantes[id_visitante]

        self.db.guardar()

        return True