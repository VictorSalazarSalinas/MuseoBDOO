"""Punto de entrada del sistema de gestión de museo (BDOO con ZODB).

Ejecuta la demostración completa del proyecto:
  FASE 1: Creación de objetos y guardado (transaction.commit).
  FASE 2: Reapertura y verificación de persistencia.
  FASE 3: CRUD completo (create, read, update, delete).
  FASE 4: Ejecución de las 13 consultas obligatorias.
"""
from datetime import date

from persistencia.base_datos import BaseDatos
from modelos.artista import Artista
from modelos.obra import Obra
from modelos.coleccion import Coleccion
from modelos.exposicion import Exposicion
from modelos.sala import Sala
from modelos.visitante import Visitante
from modelos.prestamo import Prestamo
from servicios.gestion_museo import GestionMuseo
from consultas.consultas import ConsultasMuseo


def poblar_datos(db):
    """Registra datos de ejemplo usando el CRUD del gestor."""
    gestion = GestionMuseo(db)

    gestion.registrar_artista("A01", "Leonardo da Vinci", "Italiana", 1452)
    gestion.registrar_artista("A02", "Frida Kahlo", "Mexicana", 1907)
    gestion.registrar_artista("A03", "Diego Rivera", "Mexicana", 1886)

    gestion.registrar_obra("O01", "La Gioconda", 1503, "Pintura",
                           "Óleo sobre tabla", id_artista="A01")
    gestion.registrar_obra("O02", "Hombre de Vitruvio", 1490, "Dibujo",
                           "Tinta sobre papel", id_artista="A01")
    gestion.registrar_obra("O03", "Las dos Fridas", 1939, "Pintura",
                           "Óleo sobre lienzo", id_artista="A02")
    gestion.registrar_obra("O04", "La casa azul", 1944, "Pintura",
                           "Óleo sobre masonite", id_artista="A02")
    gestion.registrar_obra("O05", "Diego y yo", 1949, "Pintura",
                           "Óleo sobre lienzo", id_artista="A02")
    gestion.registrar_obra("O06", "El vendedor de alcatraces", 1938, "Muralismo",
                           "Óleo sobre lienzo", id_artista="A03")

    gestion.registrar_coleccion("C01", "Renacimiento", "Obras del renacimiento europeo")
    gestion.registrar_coleccion("C02", "Muralismo Mexicano", "Arte mexicano del siglo XX")

    gestion.registrar_sala("S01", "Sala Renacimiento", 5, "Planta baja")
    gestion.registrar_sala("S02", "Sala México", 4, "Planta alta")

    gestion.registrar_visitante("V01", "Juan Pérez", "UV", "juan@gmail.com")
    gestion.registrar_visitante("V02", "María López", "UX", "maria@gmail.com")

    gestion.asignar_obra_a_coleccion("O01", "C01")
    gestion.asignar_obra_a_coleccion("O02", "C01")
    gestion.asignar_obra_a_coleccion("O03", "C02")
    gestion.asignar_obra_a_coleccion("O04", "C02")
    gestion.asignar_obra_a_coleccion("O05", "C02")

    gestion.asignar_obra_a_sala("O01", "S01")
    gestion.asignar_obra_a_sala("O02", "S01")
    gestion.asignar_obra_a_sala("O03", "S02")

    return gestion


def prueba_fase1_creacion_y_guardado():
    """FASE 1: creación de objetos y transacción."""
    print("--- FASE 1: Creando objetos y guardando en ZODB ---")
    db = BaseDatos()
    gestion = poblar_datos(db)

    # Exposición con obras
    exposicion = Exposicion("E01", "Maestros del Renacimiento",
                            date(2026, 9, 1), date(2026, 12, 31),
                            sala=db.root.salas["S01"])
    db.root.exposiciones["E01"] = exposicion
    exposicion.agregar_obra(db.root.obras["O01"])
    exposicion.agregar_obra(db.root.obras["O02"])
    db.guardar()

    # Préstamo de una obra a un visitante
    prestamo = Prestamo("P01", date(2026, 9, 15), date(2027, 3, 15),
                        db.root.obras["O05"], db.root.visitantes["V01"])
    db.root.prestamos["P01"] = prestamo
    db.guardar()

    print(f"Objetos registrados: {len(db.root.artistas)} artistas, "
          f"{len(db.root.obras)} obras, {len(db.root.colecciones)} colecciones, "
          f"{len(db.root.salas)} salas, {len(db.root.exposiciones)} exposiciones, "
          f"{len(db.root.visitantes)} visitantes, {len(db.root.prestamos)} préstamos.")
    db.cerrar()
    print("Conexión a ZODB cerrada.\n")
    return prestamo


def prueba_fase2_recuperacion_y_modificacion():
    """FASE 2: reapertura y verificación de persistencia."""
    print("--- FASE 2: Reabriendo base de datos y verificando persistencia ---")
    db = BaseDatos()
    consultas = ConsultasMuseo(db.root)
    obra = consultas.buscar_obra_por_id("O01")

    if obra:
        print(f"Obra recuperada: {obra.titulo}")
        print(f"Artista asociado (navegación): {obra.artista.nombre}")
        # Uso una obra disponible para demostrar el cambio de estado
        obra_test = db.root.obras["O06"]
        print(f"\nEstado inicial de {obra_test.titulo}: {obra_test.estado}")
        print("Ejecutando comportamiento: Prestar obra...")
        obra_test.prestar()
        db.guardar()
        print(f"Nuevo estado guardado: {obra_test.estado}")
        print("Persistencia verificada: el objeto sobrevivió al cierre del programa.")
    else:
        print("Error: El objeto no persistió.")

    db.cerrar()
    print()


def prueba_fase3_crud():
    """FASE 3: demostración completa del CRUD."""
    print("--- FASE 3: CRUD completo ---")
    db = BaseDatos()
    gestion = GestionMuseo(db)

    # CREATE
    artista = gestion.registrar_artista("A99", "Artista de Prueba", "Mexicana", 1990)
    print(f"CREATE: artista {artista.id_artista} registrado")

    # READ
    leido = gestion.registrar_artista("A99", "Otro", "Otra", 2000)  # id duplicado -> None
    print(f"READ/CREATE duplicado: {'correctamente rechazado' if leido is None else 'ERROR'}")
    consultas = ConsultasMuseo(db.root)
    print(f"READ: {consultas.buscar_artista_por_id('A99').nombre}")

    # UPDATE
    gestion.modificar_artista("A99", nombre="Artista Modificado")
    print(f"UPDATE: nuevo nombre = {consultas.buscar_artista_por_id('A99').nombre}")

    # DELETE
    gestion.eliminar_artista("A99")
    print(f"DELETE: existe A99 después de eliminar? "
          f"{'Sí (ERROR)' if 'A99' in db.root.artistas else 'No (correcto)'}")

    # Comportamiento: préstamo y devolución
    obra = consultas.buscar_obra_por_id("O06")
    obra.prestar()
    db.guardar()
    print(f"\nCOMPORTAMIENTO prestar(): O06 = {obra.estado}")
    obra.devolver()
    db.guardar()
    print(f"COMPORTAMIENTO devolver(): O06 = {obra.estado}")

    db.cerrar()
    print()


def prueba_fase4_consultas():
    """FASE 4: ejecución de las 13 consultas obligatorias."""
    print("--- FASE 4: Consultas obligatorias ---")
    db = BaseDatos()
    consultas = ConsultasMuseo(db.root)

    consultas.listar_obras()                                             # 1
    obra = consultas.buscar_obra_por_id("O03")                           # 2
    print(f"\n===== CONSULTA 2: BÚSQUEDA POR IDENTIDAD =====")
    print(f"Encontrada: {obra.id_obra} | {obra.titulo} | {obra.artista.nombre}")
    consultas.listar_obras_de_artista("A02")                             # 3
    consultas.listar_obras_de_coleccion("C02")                           # 4
    consultas.listar_obras_disponibles()                                 # 5
    consultas.listar_obras_prestadas()                                   # 6
    consultas.listar_obras_de_exposicion("E01")                          # 7
    consultas.listar_exposiciones_activas(date(2026, 10, 1))             # 8
    consultas.listar_obras_en_sala("S01")                                # 9
    consultas.artistas_con_mas_obras()                                   # 10
    consultas.contar_obras_por_coleccion()                               # 11
    consultas.listar_obras_sin_exposicion()                              # 12
    consultas.reporte_gestion_prestamos(date(2026, 10, 1))               # 13

    db.cerrar()
    print()


def main():
    print("=" * 60)
    print("   SISTEMA DE GESTIÓN DE MUSEO - BDOO con ZODB")
    print("=" * 60)
    prueba_fase1_creacion_y_guardado()
    prueba_fase2_recuperacion_y_modificacion()
    prueba_fase3_crud()
    prueba_fase4_consultas()
    print("=" * 60)
    print("   PROGRAMA FINALIZADO CORRECTAMENTE")
    print("=" * 60)


if __name__ == "__main__":
    main()