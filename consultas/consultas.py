class ConsultasMuseo:

    def __init__(self, root):
        self.root = root

    # ==========================================
    # BUSQUEDAS POR ID
    # ==========================================

    def buscar_obra_por_id(self, id_obra):
        return self.root.obras.get(id_obra)

    def buscar_artista_por_id(self, id_artista):
        return self.root.artistas.get(id_artista)

    # ==========================================
    # LISTADOS GENERALES
    # ==========================================

    def listar_obras(self):
        return list(self.root.obras.values())

    def listar_artistas(self):
        return list(self.root.artistas.values())

    def listar_colecciones(self):
        return list(self.root.colecciones.values())

    def listar_exposiciones(self):
        return list(self.root.exposiciones.values())

    def listar_salas(self):
        return list(self.root.salas.values())

    # ==========================================
    # CONSULTA 3: OBRAS POR ARTISTA
    # ==========================================

    def listar_obras_por_artista(self, id_artista):
        return [
            obra
            for obra in self.root.obras.values()
            if obra.artista is not None
            and obra.artista.id_artista == id_artista
        ]

    # ==========================================
    # CONSULTA 4: OBRAS POR COLECCION
    # ==========================================

    def listar_obras_por_coleccion(self, id_coleccion):
        return [
            obra
            for obra in self.root.obras.values()
            if obra.coleccion is not None
            and obra.coleccion.id_coleccion == id_coleccion
        ]

    # ==========================================
    # CONSULTA 5: OBRAS DISPONIBLES
    # ==========================================

    def mostrar_obras_disponibles(self):
        return [
            obra
            for obra in self.root.obras.values()
            if obra.estado == "Disponible"
        ]

    # ==========================================
    # CONSULTA 6: OBRAS PRESTADAS
    # ==========================================

    def mostrar_obras_prestadas(self):
        return [
            obra
            for obra in self.root.obras.values()
            if obra.estado == "Prestada"
        ]

    # ==========================================
    # CONSULTA 7: OBRAS DE UNA EXPOSICION
    # ==========================================

    def mostrar_obras_de_exposicion(self, id_exposicion):
        exposicion = self.root.exposiciones.get(id_exposicion)

        if exposicion is None:
            return []

        return list(exposicion.obras)

    # ==========================================
    # EXPOSICIONES ACTIVAS
    # ==========================================

    def listar_exposiciones_activas(self, fecha_actual):
        return [
            exposicion
            for exposicion in self.root.exposiciones.values()
            if exposicion.esta_activa(fecha_actual)
        ]

    # ==========================================
    # OBRAS POR SALA
    # ==========================================

    def listar_obras_por_sala(self, id_sala):
        return [
            obra
            for obra in self.root.obras.values()
            if obra.sala is not None
            and obra.sala.id_sala == id_sala
        ]

    # ==========================================
    # OBRAS SIN EXPOSICION
    # ==========================================

    def listar_obras_sin_exposicion(self):
        obras_expuestas = set()

        for exposicion in self.root.exposiciones.values():
            for obra in exposicion.obras:
                obras_expuestas.add(obra.id_obra)

        return [
            obra
            for obra in self.root.obras.values()
            if obra.id_obra not in obras_expuestas
        ]

    # ==========================================
    # ESTADISTICAS DE ARTISTAS
    # ==========================================

    def contar_obras_por_artista(self, id_artista):
        return sum(
            1
            for obra in self.root.obras.values()
            if obra.artista is not None
            and obra.artista.id_artista == id_artista
        )

    def artistas_con_mas_obras(self):
        artistas = self.listar_artistas()

        if not artistas:
            return []

        cantidades = {
            artista.id_artista: self.contar_obras_por_artista(
                artista.id_artista
            )
            for artista in artistas
        }

        maximo = max(cantidades.values())

        return [
            artista
            for artista in artistas
            if cantidades[artista.id_artista] == maximo
        ]

    # ==========================================
    # ESTADISTICAS DE COLECCIONES
    # ==========================================

    def contar_obras_por_coleccion(self, id_coleccion):
        return len(
            self.listar_obras_por_coleccion(id_coleccion)
        )

    # ==========================================
    # CONSULTA COMPLEJA:
    # OBRAS DISPONIBLES PARA EXHIBICION
    # ==========================================

    def listar_obras_disponibles_para_exhibicion(self, id_coleccion):
        return [
            obra
            for obra in self.listar_obras_por_coleccion(id_coleccion)
            if obra.estado == "Disponible"
        ]