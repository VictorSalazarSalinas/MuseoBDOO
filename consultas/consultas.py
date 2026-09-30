class ConsultasMuseo:

    def __init__(self, root):
        self.root = root

    def buscar_obra_por_id(self, id_obra):
        """Busca una obra por su identificador."""
        return self.root.obras.get(id_obra)

    def buscar_artista_por_id(self, id_artista):
        """Busca un artista por su identificador."""
        return self.root.artistas.get(id_artista)

    def listar_obras(self):
        """Devuelve todas las obras almacenadas."""
        return list(self.root.obras.values())

    def listar_artistas(self):
        """Devuelve todos los artistas almacenados."""
        return list(self.root.artistas.values())

    def buscar_obras_por_titulo(self, titulo):
        """Busca obras cuyo título contenga el texto indicado."""
        titulo = titulo.lower()
        return [
            obra for obra in self.root.obras.values()
            if titulo in obra.titulo.lower()
        ]

    def buscar_obras_por_tipo(self, tipo):
        """Busca obras por tipo, por ejemplo: Pintura, Escultura, etc."""
        tipo = tipo.lower()
        return [
            obra for obra in self.root.obras.values()
            if obra.tipo.lower() == tipo
        ]

    def buscar_obras_por_estado(self, estado):
        """Busca obras por su estado actual."""
        estado = estado.lower()
        return [
            obra for obra in self.root.obras.values()
            if obra.estado.lower() == estado
        ]

    def listar_obras_disponibles(self):
        """Devuelve únicamente las obras que están disponibles."""
        return self.buscar_obras_por_estado("Disponible")

    def buscar_obras_por_artista(self, id_artista):
        """Busca las obras asociadas a un artista."""
        return [
            obra for obra in self.root.obras.values()
            if obra.artista and obra.artista.id_artista == id_artista
        ]

    def buscar_artistas_por_nacionalidad(self, nacionalidad):
        """Busca artistas por nacionalidad."""
        nacionalidad = nacionalidad.lower()
        return [
            artista for artista in self.root.artistas.values()
            if artista.nacionalidad.lower() == nacionalidad
        ]
