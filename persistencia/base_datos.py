import ZODB
import ZODB.FileStorage
import transaction
from persistent.mapping import PersistentMapping


class BaseDatos:

    def __init__(self, archivo="museo.fs"):
        self.storage = ZODB.FileStorage.FileStorage(archivo)
        self.db = ZODB.DB(self.storage)
        self.conexion = self.db.open()
        self.root = self.conexion.root()

        if "artistas" not in self.root:
            self.root.artistas = PersistentMapping()

        if "obras" not in self.root:
            self.root.obras = PersistentMapping()

        if "colecciones" not in self.root:
            self.root.colecciones = PersistentMapping()

        if "exposiciones" not in self.root:
            self.root.exposiciones = PersistentMapping()

        if "salas" not in self.root:
            self.root.salas = PersistentMapping()

        if "prestamos" not in self.root:
            self.root.prestamos = PersistentMapping()

        if "visitantes" not in self.root:
            self.root.visitantes = PersistentMapping()

        transaction.commit()

    def guardar(self):
        transaction.commit()

    def cerrar(self):
        self.conexion.close()
        self.db.close()
        self.storage.close()