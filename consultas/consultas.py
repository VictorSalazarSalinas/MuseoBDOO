class ConsultasMuseo:

    def __init__(self, root):
        self.root = root

    def buscar_obra_por_id(self, id_obra):
        return self.root.obras.get(id_obra)

    def buscar_artista_por_id(self, id_artista):
        return self.root.artistas.get(id_artista)

    def listar_obras(self):
        return list(self.root.obras.values())

    def listar_artistas(self):
        return list(self.root.artistas.values())