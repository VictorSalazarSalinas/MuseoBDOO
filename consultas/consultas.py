"""Consultas orientadas al dominio sobre la BDOO del museo.
1.  Listar todas las obras.
2.  Buscar una obra mediante su identidad.
3.  Listar obras de un artista.
4.  Listar obras de una colección.
5.  Mostrar obras actualmente disponibles.
6.  Mostrar obras prestadas.
7.  Mostrar obras de una exposición.
8.  Mostrar exposiciones activas.
9.  Mostrar obras ubicadas en una sala.
10. Identificar artistas con mayor número de obras.
11. Contabilizar obras por colección.
12. Mostrar obras sin exposición asignada.
13. Consulta compleja del equipo.
"""
from datetime import date


class ConsultasMuseo:
    """Agrupa todas las consultas sobre los objetos persistentes del museo."""

    def __init__(self, root):
        self.root = root

    # ---------------------------------------------------------------
    # Consulta 1 - Recuperación general
    # ---------------------------------------------------------------
    def listar_obras(self):
        """Consulta 1: muestra todas las obras registradas."""
        print("\n===== CONSULTA 1: TODAS LAS OBRAS =====")
        for obra in self.root.obras.values():
            artista = obra.artista.nombre if obra.artista else "Sin artista"
            print(f"{obra.id_obra} | {obra.titulo} ({obra.anio}) | "
                  f"{obra.tipo} | {artista} | {obra.estado}")
        print(f"Total: {len(self.root.obras)} obras")

    # ---------------------------------------------------------------
    # Consulta 2 - Identidad
    # ---------------------------------------------------------------
    def buscar_obra_por_id(self, id_obra):
        """Consulta 2: búsqueda por identidad. Devuelve la obra o None."""
        return self.root.obras.get(id_obra)

    def buscar_artista_por_id(self, id_artista):
        """Búsqueda por identidad de artista. Devuelve el artista o None."""
        return self.root.artistas.get(id_artista)

    # ---------------------------------------------------------------
    # Consulta 3 - Filtrado
    # ---------------------------------------------------------------
    def listar_obras_de_artista(self, id_artista):
        """Consulta 3: muestra las obras de un artista dado su id."""
        artista = self.buscar_artista_por_id(id_artista)
        print(f"\n===== CONSULTA 3: OBRAS DE {artista.nombre if artista else id_artista} =====")
        if not artista:
            print("Artista no encontrado.")
            return
        encontradas = 0
        for obra in self.root.obras.values():
            if obra.artista is not None and obra.artista.id_artista == id_artista:
                print(f"{obra.id_obra} | {obra.titulo} ({obra.anio}) | {obra.estado}")
                encontradas += 1
        print(f"Total: {encontradas} obras")

    # ---------------------------------------------------------------
    # Consulta 4 - Filtrado por colección
    # ---------------------------------------------------------------
    def listar_obras_de_coleccion(self, id_coleccion):
        """Consulta 4: muestra las obras pertenecientes a una colección."""
        coleccion = self.root.colecciones.get(id_coleccion)
        print(f"\n===== CONSULTA 4: OBRAS DE LA COLECCIÓN "
              f"{coleccion.nombre if coleccion else id_coleccion} =====")
        if not coleccion:
            print("Colección no encontrada.")
            return
        encontradas = 0
        for obra in self.root.obras.values():
            if obra.coleccion is not None and obra.coleccion.id_coleccion == id_coleccion:
                print(f"{obra.id_obra} | {obra.titulo} | {obra.estado}")
                encontradas += 1
        print(f"Total: {encontradas} obras")

    # ---------------------------------------------------------------
    # Consulta 5 - Filtrado por estado (comportamiento)
    # ---------------------------------------------------------------
    def listar_obras_disponibles(self):
        """Consulta 5: obras disponibles usando obra.esta_disponible()."""
        print("\n===== CONSULTA 5: OBRAS DISPONIBLES =====")
        for obra in self.root.obras.values():
            if obra.esta_disponible():
                print(f"{obra.id_obra} | {obra.titulo} | {obra.tipo}")

    # ---------------------------------------------------------------
    # Consulta 6 - Filtrado por estado
    # ---------------------------------------------------------------
    def listar_obras_prestadas(self):
        """Consulta 6: obras cuyo estado es 'Prestada'."""
        print("\n===== CONSULTA 6: OBRAS PRESTADAS =====")
        for obra in self.root.obras.values():
            if obra.estado == "Prestada":
                print(f"{obra.id_obra} | {obra.titulo} | {obra.tipo}")

    # ---------------------------------------------------------------
    # Consulta 7 - Relación Obra -> Exposición
    # ---------------------------------------------------------------
    def listar_obras_de_exposicion(self, id_exposicion):
        """Consulta 7: obras de una exposición, navegando la relación."""
        exposicion = self.root.exposiciones.get(id_exposicion)
        print(f"\n===== CONSULTA 7: OBRAS DE LA EXPOSICIÓN "
              f"{exposicion.nombre if exposicion else id_exposicion} =====")
        if not exposicion:
            print("Exposición no encontrada.")
            return
        for obra in exposicion.obras:
            print(f"{obra.id_obra} | {obra.titulo} | {obra.estado}")
        print(f"Total: {len(exposicion.obras)} obras")

    # ---------------------------------------------------------------
    # Consulta 8 - Comportamiento de Exposición
    # ---------------------------------------------------------------
    def listar_exposiciones_activas(self, fecha_actual=None):
        """Consulta 8: exposiciones activas usando exposicion.esta_activa()."""
        if fecha_actual is None:
            fecha_actual = date.today()
        print(f"\n===== CONSULTA 8: EXPOSICIONES ACTIVAS AL {fecha_actual} =====")
        for exposicion in self.root.exposiciones.values():
            if exposicion.esta_activa(fecha_actual):
                print(f"{exposicion.id_exposicion} | {exposicion.nombre} | "
                      f"{exposicion.fecha_inicio} a {exposicion.fecha_fin}")

    # ---------------------------------------------------------------
    # Consulta 9 - Relación Obra -> Sala
    # ---------------------------------------------------------------
    def listar_obras_en_sala(self, id_sala):
        """Consulta 9: obras ubicadas actualmente en una sala."""
        sala = self.root.salas.get(id_sala)
        print(f"\n===== CONSULTA 9: OBRAS EN LA SALA {sala.nombre if sala else id_sala} =====")
        if not sala:
            print("Sala no encontrada.")
            return
        encontradas = 0
        for obra in self.root.obras.values():
            if obra.sala is not None and obra.sala.id_sala == id_sala:
                print(f"{obra.id_obra} | {obra.titulo} | {obra.estado}")
                encontradas += 1
        print(f"Total: {encontradas} obras")

    # ---------------------------------------------------------------
    # Consulta 10 - Estadística: artistas con más obras
    # ---------------------------------------------------------------
    def artistas_con_mas_obras(self, limite=3):
        """Consulta 10: artistas con mayor número de obras (top N)."""
        print(f"\n===== CONSULTA 10: ARTISTAS CON MÁS OBRAS (TOP {limite}) =====")
        contador = {}
        for obra in self.root.obras.values():
            if obra.artista is not None:
                nombre = obra.artista.nombre
                contador[nombre] = contador.get(nombre, 0) + 1
        ordenados = sorted(contador.items(), key=lambda x: x[1], reverse=True)
        for nombre, cantidad in ordenados[:limite]:
            print(f"{nombre}: {cantidad} obra(s)")
        if not ordenados:
            print("No hay obras con artista asignado.")

    # ---------------------------------------------------------------
    # Consulta 11 - Estadística: obras por colección
    # ---------------------------------------------------------------
    def contar_obras_por_coleccion(self):
        """Consulta 11: cantidad de obras agrupadas por colección."""
        print("\n===== CONSULTA 11: OBRAS POR COLECCIÓN =====")
        contador = {}
        for obra in self.root.obras.values():
            if obra.coleccion is not None:
                nombre = obra.coleccion.nombre
                contador[nombre] = contador.get(nombre, 0) + 1
        for nombre, cantidad in contador.items():
            print(f"{nombre}: {cantidad} obra(s)")
        if not contador:
            print("No hay obras con colección asignada.")

    # ---------------------------------------------------------------
    # Consulta 12 - Filtrado negativo
    # ---------------------------------------------------------------
    def listar_obras_sin_exposicion(self):
        """Consulta 12: obras que no pertenecen a ninguna exposición."""
        print("\n===== CONSULTA 12: OBRAS SIN EXPOSICIÓN =====")
        en_exposicion = set()
        for exposicion in self.root.exposiciones.values():
            for obra in exposicion.obras:
                en_exposicion.add(obra.id_obra)
        for obra in self.root.obras.values():
            if obra.id_obra not in en_exposicion:
                print(f"{obra.id_obra} | {obra.titulo} | {obra.estado}")

    # ---------------------------------------------------------------
    # Consulta 13 - Consulta compleja del equipo
    # ---------------------------------------------------------------
    def reporte_gestion_prestamos(self, fecha_actual=None):
        """Consulta 13 (compleja del equipo).

        Reporte de gestión: para cada sala, cuenta las obras que contiene,
        cuántas de ellas están prestadas y el promedio de antigüedad de las
        obras de la sala. Combina las relaciones Obra->Sala, Obra->Artista,
        el comportamiento esta_disponible() y una estadística (promedio).
        """
        if fecha_actual is None:
            fecha_actual = date.today()
        print("\n===== CONSULTA 13: REPORTE DE GESTIÓN POR SALA =====")
        for sala in self.root.salas.values():
            obras_sala = [o for o in self.root.obras.values()
                          if o.sala is not None and o.sala.id_sala == sala.id_sala]
            prestadas = len([o for o in obras_sala if not o.esta_disponible()])
            if obras_sala:
                antiguedad_prom = sum(fecha_actual.year - o.anio for o in obras_sala) / len(obras_sala)
            else:
                antiguedad_prom = 0.0
            print(f"Sala: {sala.nombre} ({sala.ubicacion})")
            print(f"  Obras: {len(obras_sala)} | Prestadas: {prestadas} | "
                  f"Antigüedad promedio: {antiguedad_prom:.1f} años")

    # Alias para compatibilidad con main.py previo
    def listar_artistas(self):
        return list(self.root.artistas.values())