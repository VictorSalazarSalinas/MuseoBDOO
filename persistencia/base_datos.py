import ZODB
import ZODB.FileStorage
import transaction


class BaseDatos:

    def __init__(self, nombre_archivo="museo.fs"):
        self.storage = ZODB.FileStorage.FileStorage(nombre_archivo)
        self.db = ZODB.DB(self.storage)
        self.conexion = self.db.open()
        self.root = self.conexion.root()

        if not hasattr(self.root, "artistas"):
            self.root.artistas = {}

        if not hasattr(self.root, "obras"):
            self.root.obras = {}

    def guardar(self):
        transaction.commit()

    def cerrar(self):
        self.conexion.close()
        self.db.close()
        self.storage.close()