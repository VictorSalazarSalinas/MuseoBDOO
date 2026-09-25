from persistencia.base_datos import BaseDatos
from modelos.artista import Artista
from modelos.obra import Obra
from consultas.consultas import ConsultasMuseo

def prueba_fase1_creacion_y_guardado():
    print("--- FASE 1: Creando objetos y guardando en ZODB ---")
    db = BaseDatos()
    
    # 1. Crear objetos
    artista1 = Artista("A01", "Leonardo da Vinci", "Italiana", 1452)
    obra1 = Obra("O01", "La Gioconda", 1503, "Pintura", "Óleo sobre tabla", artista=artista1)
    
    # 2. Guardar en ZODB
    db.root.artistas[artista1.id_artista] = artista1
    db.root.obras[obra1.id_obra] = obra1
    
    # 3. Guardar cambios (transaction.commit)
    db.guardar()
    print("Objetos creados y transaccion guardada exitosamente.")
    
    # 4. Cerrar la aplicación
    db.cerrar()
    print("Conexión a ZODB cerrada.\n")

def prueba_fase2_recuperacion_y_modificacion():
    print("--- FASE 2: Reabriendo base de datos y verificando persistencia ---")
    # 5. Volver a abrir la aplicación
    db = BaseDatos()
    
    # 6. Recuperar los objetos
    consultas = ConsultasMuseo(db.root)
    obra = consultas.buscar_obra_por_id("O01")
    
    # 7. Comprobar que la información continúa disponible
    if obra:
        print(f"Obra recuperada: {obra.titulo}")
        print(f"Artista asociado (navegación): {obra.artista.nombre}")
        print(f"Estado inicial: {obra.estado}")
        
        # 8. Modificar estado del objeto mediante comportamiento
        print("\nEjecutando comportamiento: Prestar obra...")
        obra.prestar()
        db.guardar()
        print(f"Nuevo estado guardado: {obra.estado}")
    else:
        print("Error: El objeto no persistió.")
        
    db.cerrar()

if __name__ == "__main__":
    prueba_fase1_creacion_y_guardado()
    prueba_fase2_recuperacion_y_modificacion()