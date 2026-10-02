import ZODB
import ZODB.FileStorage
from persistent.mapping import PersistentMapping


class BaseDatos:

    def __init__(self, archivo="museo.fs"):
        self.storage = ZODB.FileStorage.FileStorage(archivo)
        self.db = ZODB.DB(self.storage)
        self.conexion = self.db.open()
        self.root = self.conexion.root()

        if not hasattr(self.root, "artistas"):
            self.root.artistas = PersistentMapping()

        if not hasattr(self.root, "obras"):
            self.root.obras = PersistentMapping()

        if not hasattr(self.root, "colecciones"):
            self.root.colecciones = PersistentMapping()

        if not hasattr(self.root, "exposiciones"):
            self.root.exposiciones = PersistentMapping()

        if not hasattr(self.root, "salas"):
            self.root.salas = PersistentMapping()

        if not hasattr(self.root, "prestamos"):
            self.root.prestamos = PersistentMapping()

        if not hasattr(self.root, "visitantes"):
            self.root.visitantes = PersistentMapping()

        self.conexion.transaction_manager.commit()

    def guardar(self):
        self.conexion.transaction_manager.commit()

    def cerrar(self):
        self.conexion.close()
        self.db.close()
        self.storage.close()